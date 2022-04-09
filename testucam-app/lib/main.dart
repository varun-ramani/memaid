import 'package:flutter/material.dart';

import 'dart:async';
import 'package:camera/camera.dart';

late List<CameraDescription> cameras;
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  cameras = await availableCameras();
  runApp(Testucam());
}

class Testucam extends StatefulWidget {
  @override
  _TestucamState createState() => _TestucamState();
}

class _TestucamState extends State<Testucam> {
  late CameraController controller;
  bool _cameraIsReady = false;

  @override
  void initState() {
    super.initState();

    controller = CameraController(cameras[0], ResolutionPreset.high);
    controller.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {
        _cameraIsReady = true;
      });
    });
  }

  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_cameraIsReady) {
      return MaterialApp(home: CameraPreview(controller));
    } else {
      return Container();
    }
  }
}
