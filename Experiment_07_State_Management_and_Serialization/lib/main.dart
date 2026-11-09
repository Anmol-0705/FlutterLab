import 'package:flutter/material.dart';
import 'student.dart';

void main() {
  runApp(const StateApp());
}

class StateApp extends StatelessWidget {
  const StateApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'State Management',
      home: StudentPage(),
    );
  }
}

class StudentPage extends StatefulWidget {
  const StudentPage({super.key});

  @override
  State<StudentPage> createState() => _StudentPageState();
}

class _StudentPageState extends State<StudentPage> {
  List<String> students = [];
  Student student = Student(
    id: 1,
    name: 'Raj',
    course: 'CSE',
  );

  @override
  void initState() {
    super.initState();
    Map<String, dynamic> data = student.toJson();
    debugPrint('$data');
    Student newStudent = Student.fromJson(data);
    debugPrint(newStudent.name);
  }

  void addStudent() {
    setState(() {
      students.add('Raj (${students.length + 1})');
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student State Management & Serialization'),
      ),
      body: Column(
        children: [
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: addStudent,
            child: const Text('Add Student'),
          ),
          const SizedBox(height: 10),
          Expanded(
            child: ListView.builder(
              itemCount: students.length,
              itemBuilder: (context, index) {
                return ListTile(
                  leading: CircleAvatar(
                    child: Text('${index + 1}'),
                  ),
                  title: Text(students[index]),
                  subtitle: const Text('Course: CSE'),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
