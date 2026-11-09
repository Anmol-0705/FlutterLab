import 'package:flutter/material.dart';

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
