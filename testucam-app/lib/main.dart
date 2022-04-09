import 'package:flutter/material.dart';

import 'dart:async';
import 'package:camera/camera.dart';
import 'package:testucam/image_processing.dart';
import 'package:testucam/networking.dart';

late List<CameraDescription> cameras;
ServerConn serverConn = ServerConn("172.20.10.2", 51285);

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
  late bool _cameraIsReady;
  late bool _networkIsReady;
  late bool _errorOccured;
  int _imagethrottle = 0;

  @override
  void initState() {
    super.initState();
    setState(() {
      _cameraIsReady = false;
      _networkIsReady = false;
      _errorOccured = false;
    });
    this.setupIO();
  }

  void setupIO() async {
    if (await serverConn.establishConnection())
      setState(() {
        this._networkIsReady = true;
      });
    else
      setState(() {
        this._errorOccured = true;
      });

    controller = CameraController(cameras[0], ResolutionPreset.low);
    await controller.initialize();
    await controller.startImageStream(this.handleImage);
    setState(() {
      this._cameraIsReady = true;
    });
  }

  Future<void> handleImage(CameraImage image) async {
    print("Preparing camera image");
    List<int> outputBytes = prepareCameraImage(image);
    print("Sending camera image");
    serverConn.sendImage(outputBytes);
  }

  void dispose() {
    controller.dispose();
    super.dispose();
  }

  Widget _scaffoldBody(BuildContext build) {
    if (this._errorOccured) {
      return Center(child: Text("Fatal error occured. Cannot proceed."));
    } else if (!this._networkIsReady) {
      print("Server connection not ready");
      return Container(child: Center(child: CircularProgressIndicator()));
    } else if (!this._cameraIsReady) {
      print("Camera not ready");
      return Container(
        child: Center(
          child: CircularProgressIndicator(),
        ),
      );
    } else {
      return CameraPreview(controller);
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: _scaffoldBody(context),
      ),
    );
  }
}
