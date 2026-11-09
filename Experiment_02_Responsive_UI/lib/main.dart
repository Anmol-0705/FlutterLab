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
