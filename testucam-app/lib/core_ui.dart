import 'package:flutter/material.dart';
import 'package:testucam/streamer.dart';

class CoreUI extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(child: Streamer()),
    );
  }
}
