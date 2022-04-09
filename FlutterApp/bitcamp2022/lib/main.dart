import 'package:flutter/material.dart';
import 'package:mdi/mdi.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bitcamp 2022',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);

  static final sampleResponse = [
    "Andrew Yuan",
    "Vibhu Agrawal",
    "Varun Ramani",
    "Arjun Akkiraju",
    "Andrew Trackim",
    "William Liao",
    "Kanye West",
    "Jay Z",
    "Drakey Drake",
    "Tom Cruise",
    "Will Smith",
    "Chris Rock",
    "Chris Hemsworth",
    "Bradley Cooper",
    "Chris Pratt",
    "Chris Evans",
    "Robert Downey Jr.",
    "Taylor Swift",
    "Katy Perrys"
  ];

  initialLogo(name) {
    var initial = name[0];

    initial = initial.toUpperCase();

    switch (initial) {
      case "A":
        {
          return Icon(Mdi.alphaACircle);
        }
        break;

      case "B":
        {
          return Icon(Mdi.alphaBCircle);
        }
        break;

      case "C":
        {
          return Icon(Mdi.alphaCCircle);
        }
        break;

      case "D":
        {
          return Icon(Mdi.alphaDCircle);
        }
        break;

      case "E":
        {
          return Icon(Mdi.alphaECircle);
        }
        break;

      case "F":
        {
          return Icon(Mdi.alphaFCircle);
        }
        break;

      case "G":
        {
          return Icon(Mdi.alphaGCircle);
        }
        break;

      case "H":
        {
          return Icon(Mdi.alphaHCircle);
        }
        break;

      case "I":
        {
          return Icon(Mdi.alphaICircle);
        }
        break;

      case "J":
        {
          return Icon(Mdi.alphaJCircle);
        }
        break;

      case "K":
        {
          return Icon(Mdi.alphaKCircle);
        }
        break;

      case "L":
        {
          return Icon(Mdi.alphaLCircle);
        }
        break;

      case "M":
        {
          return Icon(Mdi.alphaMCircle);
        }
        break;

      case "N":
        {
          return Icon(Mdi.alphaNCircle);
        }
        break;

      case "O":
        {
          return Icon(Mdi.alphaOCircle);
        }
        break;

      case "P":
        {
          return Icon(Mdi.alphaPCircle);
        }
        break;

      case "Q":
        {
          return Icon(Mdi.alphaQCircle);
        }
        break;

      case "R":
        {
          return Icon(Mdi.alphaRCircle);
        }
        break;

      case "S":
        {
          return Icon(Mdi.alphaSCircle);
        }
        break;

      case "T":
        {
          return Icon(Mdi.alphaTCircle);
        }
        break;

      case "U":
        {
          return Icon(Mdi.alphaUCircle);
        }
        break;

      case "V":
        {
          return Icon(Mdi.alphaVCircle);
        }
        break;

      case "W":
        {
          return Icon(Mdi.alphaWCircle);
        }
        break;

      case "X":
        {
          return Icon(Mdi.alphaXCircle);
        }
        break;

      case "Y":
        {
          return Icon(Mdi.alphaYCircle);
        }
        break;

      case "Z":
        {
          return Icon(Mdi.alphaZCircle);
        }
        break;

      default:
        {
          return Icon(Mdi.accountCircle);
        }
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('BitCamp 2022'),
      ),
      body: SizedBox.expand(
        child: DraggableScrollableSheet(
          builder: (BuildContext context, ScrollController scrollController) {
            return Container(
              color: Color.fromARGB(255, 218, 218, 218),
              child: ListView.builder(
                controller: scrollController,
                itemCount: sampleResponse.length,
                itemBuilder: (BuildContext context, int index) {
                  return ListTile(
                      leading: initialLogo(sampleResponse[index]),
                      title: Text(sampleResponse[index]),
                      onTap: () => Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => const SecondRoute()),
                          ));
                },
              ),
            );
          },
        ),
      ),
    );
  }
}

class SecondRoute extends StatelessWidget {
  const SecondRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('BitCamp 2022'),
        ),
        body: const Text("Hello"));
  }
}
