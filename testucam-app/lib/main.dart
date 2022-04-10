import 'package:flutter/material.dart';

import 'dart:async';
import 'package:camera/camera.dart';
import 'package:testucam/core_ui.dart';
import 'package:testucam/image_processing.dart';
import 'package:testucam/networking.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(Testucam());
}

class Testucam extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(debugShowCheckedModeBanner: false, home: CoreUI());
  }
}
