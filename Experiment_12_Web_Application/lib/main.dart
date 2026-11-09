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
