import 'package:flutter/material.dart';
import 'package:tabuleiroequipe5/presenter/pages/home_page.dart';
import 'package:tabuleiroequipe5/presenter/pages/game_page.dart';
void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {
        'home_page': (context) => HomePage(),
        'game_page': (context) => const GamePage(),
      },
      home: HomePage(),
    );
  }
}