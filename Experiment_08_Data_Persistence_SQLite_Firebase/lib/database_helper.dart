import 'package:flutter/foundation.dart';
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
          await db.execute('''
            CREATE TABLE students(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              course TEXT NOT NULL
            )
          ''');
        },
      );
    }
    final path = join(await getDatabasesPath(), 'students.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL
          )
        ''');
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
