import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'database_helper.dart';
import 'firebase_options.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  initializeSQLite();
  try {
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );
  } catch (e) {
    debugPrint('Firebase init notice: $e');
  }
  runApp(const StudentDataApp());
}

class StudentDataApp extends StatelessWidget {
  const StudentDataApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Student Data Persistence',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const StudentHomePage(),
    );
  }
}

class StudentHomePage extends StatefulWidget {
  const StudentHomePage({super.key});

  @override
  State<StudentHomePage> createState() => _StudentHomePageState();
}

class _StudentHomePageState extends State<StudentHomePage> {
  final nameController = TextEditingController();
  final courseController = TextEditingController();
  List<Map<String, dynamic>> sqliteStudents = [];
  List<Map<String, dynamic>> firebaseStudents = [];
  bool loadingSQLite = false;
  bool loadingFirebase = false;

  @override
  void initState() {
    super.initState();
    loadSQLiteStudents();
    loadFirebaseStudents();
  }

  // SQLite
  Future<void> loadSQLiteStudents() async {
    setState(() => loadingSQLite = true);
    try {
      final data = await DatabaseHelper.instance.getStudents();
      if (!mounted) return;
      setState(() {
        sqliteStudents = data;
        loadingSQLite = false;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() => loadingSQLite = false);
    }
  }

  Future<void> addSQLiteStudent(String name, String course) async {
    await DatabaseHelper.instance.insertStudent(name, course);
    await loadSQLiteStudents();
  }

  Future<void> updateSQLiteStudent(int id, String name, String course) async {
    await DatabaseHelper.instance.updateStudent(id, name, course);
    await loadSQLiteStudents();
  }

  Future<void> deleteSQLiteStudent(int id) async {
    await DatabaseHelper.instance.deleteStudent(id);
    await loadSQLiteStudents();
  }

  // Firebase
  Future<void> loadFirebaseStudents() async {
    setState(() => loadingFirebase = true);
    try {
      final snapshot = await FirebaseFirestore.instance
          .collection('students')
          .orderBy('name')
          .get();
      final data = snapshot.docs.map((doc) {
        final student = doc.data();
        return {
          'id': doc.id,
          'name': student['name'] ?? '',
          'course': student['course'] ?? '',
        };
      }).toList();
      if (!mounted) return;
      setState(() {
        firebaseStudents = data;
        loadingFirebase = false;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() => loadingFirebase = false);
    }
  }

  Future<void> addFirebaseStudent(String name, String course) async {
    try {
      await FirebaseFirestore.instance.collection('students').add({
        'name': name,
        'course': course,
        'createdAt': FieldValue.serverTimestamp(),
      });
      await loadFirebaseStudents();
    } catch (e) {
      showMessage('Firebase note: $e');
    }
  }

  Future<void> updateFirebaseStudent(String id, String name, String course) async {
    await FirebaseFirestore.instance.collection('students').doc(id).update({
      'name': name,
      'course': course,
      'updatedAt': FieldValue.serverTimestamp(),
    });
    await loadFirebaseStudents();
  }

  Future<void> deleteFirebaseStudent(String id) async {
    await FirebaseFirestore.instance.collection('students').doc(id).delete();
    await loadFirebaseStudents();
  }

  Future<void> addStudent() async {
    final name = nameController.text.trim();
    final course = courseController.text.trim();
    if (name.isEmpty || course.isEmpty) {
      showMessage('Please enter student name and course');
      return;
    }
    try {
      await addSQLiteStudent(name, course);
      await addFirebaseStudent(name, course);
      nameController.clear();
      courseController.clear();
      showMessage('Student saved to SQLite and Firebase');
    } catch (e) {
      showMessage('Error: $e');
    }
  }

  void showMessage(String message) {
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(message)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student Data Persistence'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'SQLite + Firebase',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 6),
            Text(
              kIsWeb ? 'Web: SQLite WASM + Firebase' : 'Desktop: SQLite + Firebase',
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.grey.shade700),
            ),
            const SizedBox(height: 25),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  children: [
                    const Text(
                      'Add Student',
                      style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                    ),
                    const SizedBox(height: 15),
                    TextField(
                      controller: nameController,
                      decoration: const InputDecoration(
                        labelText: 'Student Name',
                        prefixIcon: Icon(Icons.person),
                        border: OutlineInputBorder(),
                      ),
                    ),
                    const SizedBox(height: 12),
                    TextField(
                      controller: courseController,
                      decoration: const InputDecoration(
                        labelText: 'Course',
                        prefixIcon: Icon(Icons.school),
                        border: OutlineInputBorder(),
                      ),
                    ),
                    const SizedBox(height: 15),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: addStudent,
                        icon: const Icon(Icons.add),
                        label: const Text('Save to SQLite + Firebase'),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 25),
            const Text(
              'SQLite - Local Storage',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            if (loadingSQLite)
              const Center(child: CircularProgressIndicator())
            else if (sqliteStudents.isEmpty)
              const Card(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: Text('No SQLite students found.'),
                ),
              )
            else
              ...sqliteStudents.map(
                (student) => Card(
                  child: ListTile(
                    leading: CircleAvatar(child: Text('${student['id']}')),
                    title: Text(student['name']),
                    subtitle: Text(student['course']),
                    trailing: IconButton(
                      icon: const Icon(Icons.delete),
                      onPressed: () => deleteSQLiteStudent(student['id']),
                    ),
                  ),
                ),
              ),
            const SizedBox(height: 15),
            OutlinedButton.icon(
              onPressed: loadSQLiteStudents,
              icon: const Icon(Icons.refresh),
              label: const Text('Refresh SQLite'),
            ),
            const SizedBox(height: 25),
            const Divider(),
            const SizedBox(height: 25),
            const Text(
              'Firebase - Cloud Storage',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            if (loadingFirebase)
              const Center(child: CircularProgressIndicator())
            else if (firebaseStudents.isEmpty)
              const Card(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: Text('No Firebase students found.'),
                ),
              )
            else
              ...firebaseStudents.map(
                (student) => Card(
                  child: ListTile(
                    leading: const CircleAvatar(child: Icon(Icons.cloud)),
                    title: Text(student['name']),
                    subtitle: Text(student['course']),
                    trailing: IconButton(
                      icon: const Icon(Icons.delete),
                      onPressed: () => deleteFirebaseStudent(student['id']),
                    ),
                  ),
                ),
              ),
            const SizedBox(height: 15),
            OutlinedButton.icon(
              onPressed: loadFirebaseStudents,
              icon: const Icon(Icons.refresh),
              label: const Text('Refresh Firebase'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    nameController.dispose();
    courseController.dispose();
    super.dispose();
  }
}
