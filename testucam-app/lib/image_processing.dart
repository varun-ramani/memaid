import 'dart:typed_data';
import 'dart:async';
import 'dart:isolate';
import 'dart:io';

import 'package:camera/camera.dart';
import 'package:image/image.dart';

PngEncoder pngEncoder = PngEncoder(level: 9);
List<int> prepareCameraImage(CameraImage cameraImage) {
  var img = Image.fromBytes(
      cameraImage.width, cameraImage.height, cameraImage.planes[0].bytes,
      format: Format.bgra);

  var encodedBytes = pngEncoder.encodeImage(img);
  return encodedBytes;
}
