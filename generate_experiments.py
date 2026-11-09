# -*- coding: utf-8 -*-
import os
import shutil

EXP_DATA = {
    1: {
        "title": "Basic Widgets and Layouts",
        "folder": "Experiment_01_Basic_Widgets",
        "aim": "To develop a Flutter application using basic widgets and layout widgets such as Container, Row, Column, Expanded, Card, and ListView.",
        "description": "This experiment demonstrates the development of a Flutter student profile/dashboard application using basic widgets and layout widgets. The main concepts include MaterialApp, Scaffold, StatelessWidget, AppBar, Column, Row, Container, Icon, Card, ListTile, and ListView.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

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
'''
        },
        "dependencies": ["flutter"]
    },
    2: {
        "title": "Adaptive and Responsive UI Design",
        "folder": "Experiment_02_Responsive_UI",
        "aim": "To create a Flutter application that automatically adapts its layout according to the available screen size.",
        "description": "This experiment demonstrates the development of a responsive Flutter application that automatically changes its user interface according to the screen width. The application uses LayoutBuilder to provide different layouts for mobile, tablet, and desktop-sized screens.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Responsive UI',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const ResponsiveHomePage(),
    );
  }
}

class ResponsiveHomePage extends StatelessWidget {
  const ResponsiveHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Adaptive and Responsive UI'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          // Mobile layout
          if (constraints.maxWidth < 600) {
            return Column(
              children: const [
                Card(
                  margin: EdgeInsets.all(10),
                  child: ListTile(
                    leading: Icon(Icons.person),
                    title: Text('Student'),
                    subtitle: Text('Mobile Layout'),
                  ),
                ),
                Card(
                  margin: EdgeInsets.all(10),
                  child: ListTile(
                    leading: Icon(Icons.book),
                    title: Text('Courses'),
                    subtitle: Text('Mobile Layout'),
                  ),
                ),
              ],
            );
          }

          // Desktop / Tablet layout
          return Row(
            children: const [
              Expanded(
                child: Card(
                  margin: EdgeInsets.all(10),
                  child: ListTile(
                    leading: Icon(Icons.people),
                    title: Text('Students'),
                    subtitle: Text('Desktop / Tablet Layout'),
                  ),
                ),
              ),
              Expanded(
                child: Card(
                  margin: EdgeInsets.all(10),
                  child: ListTile(
                    leading: Icon(Icons.school),
                    title: Text('Courses'),
                    subtitle: Text('Desktop / Tablet Layout'),
                  ),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    3: {
        "title": "Add Interactivity to App - Input and Forms",
        "folder": "Experiment_03_Input_and_Forms",
        "aim": "To create an interactive Flutter student registration form with input fields and validation for Student Name, Email, and Password, along with a Submit button.",
        "description": "This experiment demonstrates how to add interactivity to a Flutter application using input fields and forms. A Form is used to group input fields, GlobalKey<FormState> validates inputs, and SnackBar provides user feedback.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const StudentFormApp());
}

class StudentFormApp extends StatelessWidget {
  const StudentFormApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Student Registration',
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: Colors.blue,
      ),
      home: const StudentForm(),
    );
  }
}

class StudentForm extends StatefulWidget {
  const StudentForm({super.key});

  @override
  State<StudentForm> createState() => _StudentFormState();
}

class _StudentFormState extends State<StudentForm> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Student Registration',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Card(
            elevation: 6,
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(Icons.school, size: 60),
                    const SizedBox(height: 15),
                    const Text(
                      'Create Student Account',
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 25),
                    TextFormField(
                      decoration: const InputDecoration(
                        labelText: 'Student Name',
                        prefixIcon: Icon(Icons.person),
                        border: OutlineInputBorder(),
                      ),
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Enter student name';
                        }
                        return null;
                      },
                    ),
                    const SizedBox(height: 18),
                    TextFormField(
                      decoration: const InputDecoration(
                        labelText: 'Email',
                        prefixIcon: Icon(Icons.email),
                        border: OutlineInputBorder(),
                      ),
                      keyboardType: TextInputType.emailAddress,
                    ),
                    const SizedBox(height: 18),
                    TextFormField(
                      obscureText: true,
                      decoration: const InputDecoration(
                        labelText: 'Password',
                        prefixIcon: Icon(Icons.lock),
                        border: OutlineInputBorder(),
                      ),
                    ),
                    const SizedBox(height: 25),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {
                          if (_formKey.currentState!.validate()) {
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content: Text('Form submitted successfully'),
                              ),
                            );
                          }
                        },
                        child: const Text('Submit'),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    4: {
        "title": "Utilize Assets and Media",
        "folder": "Experiment_04_Assets_and_Media",
        "aim": "To add and display image, audio and video assets in a Flutter application.",
        "description": "This experiment demonstrates how to add and display image, audio, and video assets in a Flutter application. Assets are stored in the assets folder, declared in pubspec.yaml, and rendered via Flutter widgets with interactive video controls.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';

void main() {
  runApp(const MediaApp());
}

class MediaApp extends StatelessWidget {
  const MediaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MediaDemo(),
    );
  }
}

class MediaDemo extends StatefulWidget {
  const MediaDemo({super.key});

  @override
  State<MediaDemo> createState() => _MediaDemoState();
}

class _MediaDemoState extends State<MediaDemo> {
  late VideoPlayerController _controller;
  bool isVideoReady = false;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.asset('assets/video/sample.mp4');
    _controller.initialize().then((_) {
      setState(() {
        isVideoReady = true;
      });
    }).catchError((_) {
      // Graceful fallback for web/missing asset
      setState(() {});
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Flutter Assets and Media')),
      body: SingleChildScrollView(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                const Text(
                  'Hello World',
                  style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 30),
                const Text(
                  'Image Asset',
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),
                Image.asset(
                  'assets/images/flutter.png',
                  width: 250,
                  height: 250,
                  fit: BoxFit.contain,
                  errorBuilder: (context, error, stackTrace) {
                    return Container(
                      width: 250,
                      height: 200,
                      decoration: BoxDecoration(
                        color: Colors.blue.shade50,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: Colors.blue.shade200),
                      ),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: const [
                          Icon(Icons.image, size: 80, color: Colors.blue),
                          SizedBox(height: 10),
                          Text('Flutter Asset Logo', style: TextStyle(fontWeight: FontWeight.bold)),
                        ],
                      ),
                    );
                  },
                ),
                const SizedBox(height: 40),
                const Text(
                  'Video Asset',
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),
                isVideoReady
                    ? SizedBox(
                        width: 600,
                        child: AspectRatio(
                          aspectRatio: _controller.value.aspectRatio,
                          child: VideoPlayer(_controller),
                        ),
                      )
                    : Container(
                        width: 400,
                        height: 220,
                        decoration: BoxDecoration(
                          color: Colors.black87,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Center(
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(Icons.videocam, size: 64, color: Colors.white70),
                              SizedBox(height: 10),
                              Text('Sample Video Asset Player', style: TextStyle(color: Colors.white70)),
                            ],
                          ),
                        ),
                      ),
                const SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      if (_controller.value.isPlaying) {
                        _controller.pause();
                      } else {
                        _controller.play();
                      }
                    });
                  },
                  child: Text(
                    _controller.value.isPlaying ? 'Pause Video' : 'Play Video',
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter", "video_player"]
    },
    5: {
        "title": "Implementation of Navigation and Routing",
        "folder": "Experiment_05_Navigation_and_Routing",
        "aim": "To implement navigation between multiple Flutter screens using Navigator and named routes.",
        "description": "This experiment demonstrates how to navigate between multiple screens in a Flutter application. The application contains Home, Profile, and Details screens. Named routes are used for forward navigation and Navigator.pop for backward navigation.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';
import 'home.dart';
import 'profile.dart';
import 'details.dart';

void main() {
  runApp(const NavigationApp());
}

class NavigationApp extends StatelessWidget {
  const NavigationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Navigation App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.purple,
        ),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const HomePage(),
        '/profile': (context) => const ProfilePage(),
        '/details': (context) => const DetailsPage(),
      },
    );
  }
}
''',
            "lib/home.dart": '''import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Home',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.purple,
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Colors.purple,
              Colors.pink,
              Colors.lightBlue,
            ],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Center(
          child: Card(
            elevation: 10,
            margin: const EdgeInsets.all(30),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(25),
            ),
            child: Padding(
              padding: const EdgeInsets.all(35),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(
                    Icons.home_rounded,
                    size: 80,
                    color: Colors.purple,
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Welcome Home!',
                    style: TextStyle(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                      color: Colors.purple,
                    ),
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'Explore the different screens',
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.grey,
                    ),
                  ),
                  const SizedBox(height: 30),
                  ElevatedButton.icon(
                    onPressed: () {
                      Navigator.pushNamed(context, '/profile');
                    },
                    icon: const Icon(Icons.person),
                    label: const Text('Go to Profile'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.pink,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 25,
                        vertical: 15,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
''',
            "lib/profile.dart": '''import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Profile',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.pink,
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Colors.pink,
              Colors.purple,
              Colors.lightBlue,
            ],
            begin: Alignment.topRight,
            end: Alignment.bottomLeft,
          ),
        ),
        child: Center(
          child: Card(
            elevation: 10,
            margin: const EdgeInsets.all(30),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(25),
            ),
            child: Padding(
              padding: const EdgeInsets.all(35),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const CircleAvatar(
                    radius: 50,
                    backgroundColor: Colors.pink,
                    child: Icon(
                      Icons.person,
                      size: 60,
                      color: Colors.white,
                    ),
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Student Profile',
                    style: TextStyle(
                      fontSize: 27,
                      fontWeight: FontWeight.bold,
                      color: Colors.purple,
                    ),
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'Welcome to your profile page!',
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.grey,
                    ),
                  ),
                  const SizedBox(height: 30),
                  ElevatedButton.icon(
                    onPressed: () {
                      Navigator.pushNamed(context, '/details');
                    },
                    icon: const Icon(Icons.info_outline),
                    label: const Text('View Details'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.lightBlue,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 25,
                        vertical: 15,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
''',
            "lib/details.dart": '''import 'package:flutter/material.dart';

class DetailsPage extends StatelessWidget {
  const DetailsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Details',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.lightBlue,
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Colors.lightBlue,
              Colors.purple,
              Colors.pink,
            ],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Center(
          child: Card(
            elevation: 10,
            margin: const EdgeInsets.all(30),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(25),
            ),
            child: Padding(
              padding: const EdgeInsets.all(35),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(
                    Icons.school_rounded,
                    size: 80,
                    color: Colors.lightBlue,
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Student Details',
                    style: TextStyle(
                      fontSize: 27,
                      fontWeight: FontWeight.bold,
                      color: Colors.purple,
                    ),
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Name: Arsath Ahamed URK23CS1203\\n'
                    'Course: Computer Science\\n'
                    'Department: CSE',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 17,
                      height: 1.7,
                      color: Colors.black87,
                    ),
                  ),
                  const SizedBox(height: 30),
                  ElevatedButton.icon(
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    icon: const Icon(Icons.arrow_back),
                    label: const Text('Back to Profile'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 25,
                        vertical: 15,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    6: {
        "title": "Integrate Animations and Transitions",
        "folder": "Experiment_06_Animations_and_Transitions",
        "aim": "To Implement animations and smooth transitions in a Flutter application using AnimatedContainer.",
        "description": "This experiment demonstrates the use of Flutter's AnimatedContainer to create a smooth size transition. A button is provided to change the size of the widget dynamically using setState().",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const AnimationApp());
}

class AnimationApp extends StatelessWidget {
  const AnimationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Animation',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.deepPurple,
        ),
        useMaterial3: true,
      ),
      home: const AnimationPage(),
    );
  }
}

class AnimationPage extends StatefulWidget {
  const AnimationPage({super.key});

  @override
  State<AnimationPage> createState() => _AnimationPageState();
}

class _AnimationPageState extends State<AnimationPage> {
  bool isLarge = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Flutter Animations',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.deepPurple,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        color: const Color(0xFFEDE7F6),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              AnimatedContainer(
                duration: const Duration(seconds: 1),
                curve: Curves.easeInOut,
                width: isLarge ? 300 : 150,
                height: isLarge ? 300 : 150,
                decoration: BoxDecoration(
                  color: const Color(0xFFB39DDB),
                  borderRadius: BorderRadius.circular(
                    isLarge ? 50 : 20,
                  ),
                  boxShadow: const [
                    BoxShadow(
                      blurRadius: 15,
                      spreadRadius: 3,
                      offset: Offset(0, 8),
                    ),
                  ],
                ),
                child: const Center(
                  child: Text(
                    'Flutter',
                    style: TextStyle(
                      fontSize: 28,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 40),
              ElevatedButton.icon(
                onPressed: () {
                  setState(() {
                    isLarge = !isLarge;
                  });
                },
                icon: const Icon(Icons.animation),
                label: const Text(
                  'Animate',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepPurple,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(
                    horizontal: 35,
                    vertical: 16,
                  ),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30),
                  ),
                ),
              ),
              const SizedBox(height: 20),
              Text(
                isLarge ? 'Widget is Large' : 'Widget is Small',
                style: const TextStyle(
                  color: Colors.deepPurple,
                  fontSize: 18,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    7: {
        "title": "Application State Management and Serialization",
        "folder": "Experiment_07_State_Management_and_Serialization",
        "aim": "To manage application state and serialize/deserialize data using JSON in a Flutter application.",
        "description": "This experiment demonstrates application state management using setState() and JSON serialization/deserialization using a Student model. Student data is converted from a Dart object into JSON format using toJson() and converted back into a Dart object using fromJson(). A list of students is displayed dynamically using ListView.builder().",
        "files": {
            "lib/student.dart": '''class Student {
  final int id;
  final String name;
  final String course;

  Student({
    required this.id,
    required this.name,
    required this.course,
  });

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'course': course,
    };
  }

  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      id: json['id'],
      name: json['name'],
      course: json['course'],
    );
  }
}
''',
            "lib/main.dart": '''import 'package:flutter/material.dart';
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
'''
        },
        "dependencies": ["flutter"]
    },
    8: {
        "title": "Data Persistence using SQLite and Firebase",
        "folder": "Experiment_08_Data_Persistence_SQLite_Firebase",
        "aim": "To Implement data persistence in a Flutter application using SQLite for local storage and Firebase Cloud Firestore for cloud storage, to perform basic data operations such as insertion, retrieval, updating, and deletion.",
        "description": "This experiment demonstrates how Flutter applications can store data permanently using SQLite for local device storage and Firebase Cloud Firestore for cloud persistence.",
        "files": {
            "lib/database_helper.dart": '''import 'package:flutter/foundation.dart';
import 'package:path/path.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:sqflite_common_ffi_web/sqflite_ffi_web.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._privateConstructor();
  static Database? _database;

  DatabaseHelper._privateConstructor();

  Future<Database> get database async {
    if (_database != null) {
      return _database!;
    }
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    if (kIsWeb) {
      databaseFactory = databaseFactoryFfiWeb;
      return await openDatabase(
        'students_web.db',
        version: 1,
        onCreate: (db, version) async {
          await db.execute(\'\'\'
            CREATE TABLE students(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              course TEXT NOT NULL
            )
          \'\'\');
        },
      );
    }
    final path = join(await getDatabasesPath(), 'students.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute(\'\'\'
          CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL
          )
        \'\'\');
      },
    );
  }

  Future<int> insertStudent(String name, String course) async {
    final db = await database;
    return await db.insert(
      'students',
      {
        'name': name,
        'course': course,
      },
    );
  }

  Future<List<Map<String, dynamic>>> getStudents() async {
    final db = await database;
    return await db.query(
      'students',
      orderBy: 'id DESC',
    );
  }

  Future<int> updateStudent(int id, String name, String course) async {
    final db = await database;
    return await db.update(
      'students',
      {
        'name': name,
        'course': course,
      },
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<int> deleteStudent(int id) async {
    final db = await database;
    return await db.delete(
      'students',
      where: 'id = ?',
      whereArgs: [id],
    );
  }
}

void initializeSQLite() {
  if (kIsWeb) {
    databaseFactory = databaseFactoryFfiWeb;
  } else {
    sqfliteFfiInit();
    databaseFactory = databaseFactoryFfi;
  }
}
''',
            "lib/firebase_options.dart": '''import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart' show defaultTargetPlatform, kIsWeb, TargetPlatform;

class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        return windows;
      case TargetPlatform.linux:
        throw UnsupportedError('DefaultFirebaseOptions have not been configured for linux.');
      default:
        throw UnsupportedError('DefaultFirebaseOptions are not supported for this platform.');
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyD2_SqRHdwOFdhzLDy5cbXKFpjdPgGuhHg',
    appId: '1:291139208558:web:3ce393b0c2f589fbafed7f',
    messagingSenderId: '291139208558',
    projectId: 'student-firebase-app-b68fd',
    authDomain: 'student-firebase-app-b68fd.firebaseapp.com',
    storageBucket: 'student-firebase-app-b68fd.firebasestorage.app',
    measurementId: 'G-HP1425X0DQ',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyAMHi3_F9LRqqkHCU2wPsrFKMDcrwfAeLA',
    appId: '1:291139208558:android:4103cdb00632d5baafed7f',
    messagingSenderId: '291139208558',
    projectId: 'student-firebase-app-b68fd',
    storageBucket: 'student-firebase-app-b68fd.firebasestorage.app',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyCDi8mRM1HjcyfX_8RfeQ4GHMdkhG99V2s',
    appId: '1:291139208558:ios:6bd582928a142796afed7f',
    messagingSenderId: '291139208558',
    projectId: 'student-firebase-app-b68fd',
    storageBucket: 'student-firebase-app-b68fd.firebasestorage.app',
    iosBundleId: 'com.example.sqliteApp',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyCDi8mRM1HjcyfX_8RfeQ4GHMdkhG99V2s',
    appId: '1:291139208558:ios:6bd582928a142796afed7f',
    messagingSenderId: '291139208558',
    projectId: 'student-firebase-app-b68fd',
    storageBucket: 'student-firebase-app-b68fd.firebasestorage.app',
    iosBundleId: 'com.example.sqliteApp',
  );

  static const FirebaseOptions windows = FirebaseOptions(
    apiKey: 'AIzaSyD2_SqRHdwOFdhzLDy5cbXKFpjdPgGuhHg',
    appId: '1:291139208558:web:707da545013202cbafed7f',
    messagingSenderId: '291139208558',
    projectId: 'student-firebase-app-b68fd',
    authDomain: 'student-firebase-app-b68fd.firebaseapp.com',
    storageBucket: 'student-firebase-app-b68fd.firebasestorage.app',
    measurementId: 'G-5TNZX9RJ3M',
  );
}
''',
            "lib/main.dart": '''import 'package:cloud_firestore/cloud_firestore.dart';
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
'''
        },
        "dependencies": ["flutter", "sqflite_common_ffi", "sqflite_common_ffi_web", "path", "firebase_core", "cloud_firestore"]
    },
    9: {
        "title": "Access REST API using HTTP",
        "folder": "Experiment_09_REST_API",
        "aim": "To access a REST API using HTTP and retrieve and display JSON data in a Flutter application.",
        "description": "This experiment demonstrates how Flutter communicates with a REST API using the http package. The application sends a GET request to the JSONPlaceholder API, converts the JSON response into Dart data, and displays the posts using ListView.builder.",
        "files": {
            "lib/main.dart": '''import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const ApiApp());
}

class ApiApp extends StatelessWidget {
  const ApiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'API App',
      theme: ThemeData(
        scaffoldBackgroundColor: const Color(0xFFF8F4FC),
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF9C7AC7),
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: Color(0xFFBFA2DB),
          foregroundColor: Colors.white,
          centerTitle: true,
          elevation: 2,
        ),
        cardTheme: const CardThemeData(
          color: Color(0xFFF0E6F7),
          elevation: 2,
          margin: EdgeInsets.symmetric(
            horizontal: 12,
            vertical: 7,
          ),
        ),
      ),
      home: const ApiHomePage(),
    );
  }
}

class ApiHomePage extends StatefulWidget {
  const ApiHomePage({super.key});

  @override
  State<ApiHomePage> createState() => _ApiHomePageState();
}

class _ApiHomePageState extends State<ApiHomePage> {
  List<dynamic> posts = [];
  bool isLoading = true;
  String errorMessage = '';

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    setState(() {
      isLoading = true;
      errorMessage = '';
    });

    try {
      final response = await http.get(
        Uri.parse('https://jsonplaceholder.typicode.com/posts'),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          posts = data;
          isLoading = false;
        });
      } else {
        setState(() {
          errorMessage = 'Failed to load data';
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = 'Network error. Please try again.';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'REST API Posts',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: isLoading
          ? const Center(
              child: CircularProgressIndicator(
                color: Color(0xFF9C7AC7),
              ),
            )
          : errorMessage.isNotEmpty
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(
                        Icons.error_outline,
                        size: 60,
                        color: Color(0xFF9C7AC7),
                      ),
                      const SizedBox(height: 15),
                      Text(
                        errorMessage,
                        style: const TextStyle(
                          fontSize: 18,
                          color: Color(0xFF5E4A6E),
                        ),
                      ),
                      const SizedBox(height: 15),
                      ElevatedButton(
                        onPressed: fetchData,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFFBFA2DB),
                          foregroundColor: Colors.white,
                        ),
                        child: const Text('Retry'),
                      ),
                    ],
                  ),
                )
              : RefreshIndicator(
                  onRefresh: fetchData,
                  child: ListView.builder(
                    itemCount: posts.length,
                    itemBuilder: (context, index) {
                      final post = posts[index];
                      return Card(
                        child: ListTile(
                          leading: CircleAvatar(
                            backgroundColor: const Color(0xFF9C7AC7),
                            foregroundColor: Colors.white,
                            child: Text('${post['id']}'),
                          ),
                          title: Text(
                            post['title'],
                            style: const TextStyle(fontWeight: FontWeight.bold),
                          ),
                          subtitle: Text(post['body']),
                        ),
                      );
                    },
                  ),
                ),
    );
  }
}
'''
        },
        "dependencies": ["flutter", "http"]
    },
    10: {
        "title": "Configure and Build for Android",
        "folder": "Experiment_10_Android_Build_Target",
        "aim": "To configure and build a Flutter application for the Android platform.",
        "description": "This experiment demonstrates how to configure Flutter for Android development, check connected Android devices, accept Android SDK licenses, run the application on an Android device or emulator, and generate an APK file.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Experiment 10',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Experiment 10 - Android Target'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.android, size: 80, color: Colors.green),
            const SizedBox(height: 20),
            const Text(
              'You have pushed the button this many times:',
              style: TextStyle(fontSize: 16),
            ),
            Text(
              '$_counter',
              style: const TextStyle(fontSize: 38, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    11: {
        "title": "Add iOS as a Build Target",
        "folder": "Experiment_11_iOS_Build_Target",
        "aim": "To create a Flutter application with an iOS build target, test the application, and deploy its Flutter Web version using GitHub Pages.",
        "description": "This experiment demonstrates how a Flutter application can be configured with iOS as a target platform, tested across targets, and deployed on GitHub Pages.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'iOS Flutter App',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        scaffoldBackgroundColor: const Color(0xFFF3E5F5),
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'iOS Flutter Application',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.deepPurple,
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(
              Icons.phone_iphone,
              size: 80,
              color: Colors.deepPurple,
            ),
            const SizedBox(height: 15),
            const Text(
              'Flutter iOS App',
              style: TextStyle(
                fontSize: 26,
                fontWeight: FontWeight.bold,
                color: Colors.deepPurple,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Experiment 11\\nAdd iOS as a Build Target',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 25),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Button clicked successfully!'),
                  ),
                );
              },
              child: const Text('Test Button'),
            ),
            const SizedBox(height: 15),
            const Text(
              '✓ Application Ready',
              style: TextStyle(
                color: Colors.green,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    },
    12: {
        "title": "Build Web App using Flutter",
        "folder": "Experiment_12_Web_Application",
        "aim": "To develop, run, and build a responsive Flutter application for the Web using Flutter and Chrome.",
        "description": "This experiment demonstrates how Flutter allows developers to create web applications using the same Flutter framework used for mobile applications. A responsive web application adapts between mobile and desktop web views.",
        "files": {
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Web Application',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Web Application'),
        ),
        body: LayoutBuilder(
          builder: (context, constraints) {
            if (constraints.maxWidth < 600) {
              return const Center(
                child: Text(
                  'Mobile Web Layout',
                  style: TextStyle(fontSize: 24),
                ),
              );
            }
            return const Center(
              child: Text(
                'Desktop Web Layout',
                style: TextStyle(fontSize: 30),
              ),
            );
          },
        ),
      ),
    );
  }
}
'''
        },
        "dependencies": ["flutter"]
    }
}

def generate_pubspec(title, exp_num, deps):
    name = f"exp_{exp_num}"
    dep_lines = "  flutter:\n    sdk: flutter\n"
    if "video_player" in deps:
        dep_lines += "  video_player: ^2.9.2\n"
    if "http" in deps:
        dep_lines += "  http: ^1.2.2\n"
    if "sqflite_common_ffi" in deps:
        dep_lines += "  sqflite_common_ffi: ^2.3.4\n  sqflite_common_ffi_web: ^0.4.5\n  path: ^1.9.0\n  firebase_core: ^3.6.0\n  cloud_firestore: ^5.4.4\n"
    
    asset_block = ""
    if exp_num == 4:
        asset_block = """
flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/video/
"""
    else:
        asset_block = """
flutter:
  uses-material-design: true
"""
    return f"""name: {name}
description: "{title} - Experiment {exp_num}"
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
{dep_lines}
dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0
{asset_block}
"""

def generate_readme(exp_num, info):
    return f"""# Experiment {exp_num}: {info['title']}

## Aim
{info['aim']}

## Description
{info['description']}

## Files
""" + "\n".join([f"- `{f}`" for f in info['files'].keys()]) + f"""

## How to Run Locally
```bash
cd {info['folder']}
flutter pub get
flutter run
```

## Hosted GitHub Pages
View the hosted demo: [https://anmol-0705.github.io/FlutterLab/exp{exp_num}/](https://anmol-0705.github.io/FlutterLab/exp{exp_num}/)
"""

for exp_num, info in EXP_DATA.items():
    folder = info['folder']
    os.makedirs(folder, exist_ok=True)
    
    # Write files
    for rel_path, content in info['files'].items():
        full_path = os.path.join(folder, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    # Write pubspec.yaml
    pubspec_path = os.path.join(folder, 'pubspec.yaml')
    with open(pubspec_path, 'w', encoding='utf-8') as f:
        f.write(generate_pubspec(info['title'], exp_num, info['dependencies']))
        
    # Write README.md
    readme_path = os.path.join(folder, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(generate_readme(exp_num, info))

# Create assets for exp 4
exp4_img_dir = os.path.join(EXP_DATA[4]['folder'], 'assets', 'images')
exp4_vid_dir = os.path.join(EXP_DATA[4]['folder'], 'assets', 'video')
os.makedirs(exp4_img_dir, exist_ok=True)
os.makedirs(exp4_vid_dir, exist_ok=True)

# Generate a minimal valid PNG
import base64
png_1x1 = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==')
with open(os.path.join(exp4_img_dir, 'flutter.png'), 'wb') as f:
    f.write(png_1x1)
with open(os.path.join(exp4_vid_dir, 'sample.mp4'), 'wb') as f:
    f.write(b'sample-mp4-data')

print("Successfully created all 12 experiment directories!")
