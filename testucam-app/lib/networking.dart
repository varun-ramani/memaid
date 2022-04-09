import 'dart:io';
import 'dart:typed_data';
import 'package:camera/camera.dart';

class ServerConn {
  final String remoteIP;
  final int remotePort;
  Socket? sock;

  ServerConn(this.remoteIP, this.remotePort);

  Future<bool> establishConnection() async {
    try {
      sock = await Socket.connect(remoteIP, remotePort);
      return true;
    } on SocketException catch (_) {
      return false;
    }
  }

  void sendImage(List<int> imageBytes) {
    // Write the message type - images are 0x01
    sock?.add([0x01]);

    // Write the image length
    sock?.add(Uint8List(4)
      ..buffer.asByteData().setUint32(0, imageBytes.length * 4, Endian.big));

    sock?.add(imageBytes);
  }
}
