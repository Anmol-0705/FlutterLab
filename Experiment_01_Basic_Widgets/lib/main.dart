import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Student Profile',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        scaffoldBackgroundColor: Colors.grey[100],
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.indigo,
          foregroundColor: Colors.white,
        ),
      ),
      home: const StudentProfile(),
    );
  }
}

class StudentProfile extends StatelessWidget {
  const StudentProfile({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Student Profile',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Student Profile Container
          Container(
            padding: const EdgeInsets.all(20),
            margin: const EdgeInsets.only(bottom: 15),
            decoration: BoxDecoration(
              color: Colors.indigo,
              borderRadius: BorderRadius.circular(15),
              boxShadow: const [
                BoxShadow(
                  color: Colors.grey,
                  blurRadius: 6,
                  offset: Offset(0, 3),
                ),
              ],
            ),
            child: const Column(
              children: [
                CircleAvatar(
                  radius: 40,
                  backgroundColor: Colors.white,
                  child: Icon(
                    Icons.person,
                    size: 50,
                    color: Colors.indigo,
                  ),
                ),
                SizedBox(height: 12),
                Text(
                  'ARSATH AHAMED URK23CS1203',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 25,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 5),
                Text(
                  'Computer Science and Engineering',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                ),
                SizedBox(height: 5),
                Text(
                  'Flutter Laboratory',
                  style: TextStyle(
                    color: Colors.white70,
                    fontSize: 15,
                  ),
                ),
              ],
            ),
          ),

          // Row with Icons
          Card(
            elevation: 4,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15),
            ),
            child: const Padding(
              padding: EdgeInsets.all(18),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Icon(
                    Icons.home,
                    color: Colors.blue,
                    size: 35,
                  ),
                  Icon(
                    Icons.person,
                    color: Colors.green,
                    size: 35,
                  ),
                  Icon(
                    Icons.settings,
                    color: Colors.orange,
                    size: 35,
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 15),

          // Section Title
          const Text(
            'Subjects',
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.indigo,
            ),
          ),
          const SizedBox(height: 10),

          // Flutter Card
          Card(
            elevation: 4,
            color: Colors.blue[50],
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15),
            ),
            child: const ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.blue,
                child: Icon(
                  Icons.book,
                  color: Colors.white,
                ),
              ),
              title: Text(
                'Flutter',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                ),
              ),
              subtitle: Text(
                'Mobile Application Development',
              ),
            ),
          ),

          // Cloud Computing Card
          Card(
            elevation: 4,
            color: Colors.green[50],
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15),
            ),
            child: const ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.green,
                child: Icon(
                  Icons.cloud,
                  color: Colors.white,
                ),
              ),
              title: Text(
                'Cloud Computing',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                ),
              ),
              subtitle: Text(
                'Cloud Technologies and Services',
              ),
            ),
          ),

          // Programming Card
          Card(
            elevation: 4,
            color: Colors.orange[50],
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15),
            ),
            child: const ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.orange,
                child: Icon(
                  Icons.code,
                  color: Colors.white,
                ),
              ),
              title: Text(
                'Programming',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                ),
              ),
              subtitle: Text(
                'Programming Fundamentals',
              ),
            ),
          ),
          const SizedBox(height: 15),

          // Bottom Message
          Container(
            padding: const EdgeInsets.all(15),
            decoration: BoxDecoration(
              color: Colors.deepPurple,
              borderRadius: BorderRadius.circular(12),
            ),
            child: const Text(
              'Welcome to Flutter Laboratory!',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
