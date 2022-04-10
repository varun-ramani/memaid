import 'package:flutter/material.dart';
import 'package:mdi/mdi.dart';
import 'package:sliding_up_panel/sliding_up_panel.dart';

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
    "Katy Perry"
  ];

  static final sampleBulletPoints = [
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"],
    ["point1", "point2", "point3", "point4"]
  ];

  static final testImage = Container(
    width: 200.0,
    height: 200.0,
    decoration: BoxDecoration(
        image:
            DecorationImage(fit: BoxFit.cover, image: AssetImage("trump.jpeg")),
        borderRadius: BorderRadius.all(Radius.circular(20.0))),
  );
  initialLogo(name) {
    var initial = name[0];

    initial = initial.toUpperCase();

    switch (initial) {
      case "A":
        {
          return Icon(Mdi.alphaACircle, size: 40);
        }
        break;

      case "B":
        {
          return Icon(Mdi.alphaBCircle, size: 40);
        }
        break;

      case "C":
        {
          return Icon(Mdi.alphaCCircle, size: 40);
        }
        break;

      case "D":
        {
          return Icon(Mdi.alphaDCircle, size: 40);
        }
        break;

      case "E":
        {
          return Icon(Mdi.alphaECircle, size: 40);
        }
        break;

      case "F":
        {
          return Icon(Mdi.alphaFCircle, size: 40);
        }
        break;

      case "G":
        {
          return Icon(Mdi.alphaGCircle, size: 40);
        }
        break;

      case "H":
        {
          return Icon(Mdi.alphaHCircle, size: 40);
        }
        break;

      case "I":
        {
          return Icon(Mdi.alphaICircle, size: 40);
        }
        break;

      case "J":
        {
          return Icon(Mdi.alphaJCircle, size: 40);
        }
        break;

      case "K":
        {
          return Icon(Mdi.alphaKCircle, size: 40);
        }
        break;

      case "L":
        {
          return Icon(Mdi.alphaLCircle, size: 40);
        }
        break;

      case "M":
        {
          return Icon(Mdi.alphaMCircle, size: 40);
        }
        break;

      case "N":
        {
          return Icon(Mdi.alphaNCircle, size: 40);
        }
        break;

      case "O":
        {
          return Icon(Mdi.alphaOCircle, size: 40);
        }
        break;

      case "P":
        {
          return Icon(Mdi.alphaPCircle, size: 40);
        }
        break;

      case "Q":
        {
          return Icon(Mdi.alphaQCircle, size: 40);
        }
        break;

      case "R":
        {
          return Icon(Mdi.alphaRCircle, size: 40);
        }
        break;

      case "S":
        {
          return Icon(Mdi.alphaSCircle, size: 40);
        }
        break;

      case "T":
        {
          return Icon(Mdi.alphaTCircle, size: 40);
        }
        break;

      case "U":
        {
          return Icon(Mdi.alphaUCircle, size: 40);
        }
        break;

      case "V":
        {
          return Icon(Mdi.alphaVCircle, size: 40);
        }
        break;

      case "W":
        {
          return Icon(Mdi.alphaWCircle, size: 40);
        }
        break;

      case "X":
        {
          return Icon(Mdi.alphaXCircle, size: 40);
        }
        break;

      case "Y":
        {
          return Icon(Mdi.alphaYCircle, size: 40);
        }
        break;

      case "Z":
        {
          return Icon(Mdi.alphaZCircle, size: 40);
        }
        break;

      default:
        {
          return Icon(Mdi.accountCircle, size: 40);
        }
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    BorderRadiusGeometry radius = BorderRadius.only(
      topLeft: Radius.circular(24.0),
      topRight: Radius.circular(24.0),
    );
    return Scaffold(
      body: SizedBox.expand(
        child: SlidingUpPanel(
          minHeight: 200,
          backdropEnabled: true,
          borderRadius: radius,
          panel: DraggableScrollableSheet(
            initialChildSize: 0.95,
            minChildSize: 0.95,
            expand: true,
            snap: true,
            builder: (BuildContext context, ScrollController scrollController) {
              return Container(
                decoration: BoxDecoration(
                  borderRadius: radius,
                  color: Colors.white,
                ),
                child: ListView.separated(
                    padding: const EdgeInsets.all(8),
                    controller: scrollController,
                    itemCount: sampleResponse.length,
                    itemBuilder: (BuildContext context, int index) {
                      return ListTile(
                          leading: initialLogo(sampleResponse[index]),
                          title: Text(sampleResponse[index]),
                          onTap: () => Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => new SecondRoute(
                                        sampleResponse[index],
                                        sampleBulletPoints[index],
                                        testImage)),
                              ));
                    },
                    separatorBuilder: (BuildContext context, int index) =>
                        const Divider(
                          color: Colors.black,
                        )),
              );
            },
          ),
          body: Center(
            child: Text("This is the Widget behind the sliding panel"),
          ),
        ),
      ),
    );
  }
}

class SecondRoute extends StatelessWidget {
  final String name;
  final List<String> bulletPoints;
  final Container image;

  const SecondRoute(this.name, this.bulletPoints, this.image);

  getBulletPoints() {
    List<Widget> ans = [];

    this.bulletPoints.forEach((String str) => ans.add(Text("• " + str)));

    return ans;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Info on " + this.name),
        ),
        body: Padding(
            padding: const EdgeInsets.all(25.0),
            child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Align(
                    alignment: Alignment.center,
                    child: this.image,
                  ),
                  Padding(padding: const EdgeInsets.all(10.0)),
                  Divider(),
                  Text("Name: " + this.name, style: TextStyle(fontSize: 20)),
                  Divider(),
                  Text(
                    "Bullet Points:",
                    style: TextStyle(fontSize: 20),
                  ),
                  Padding(padding: const EdgeInsets.all(10.0)),
                  Column(children: getBulletPoints())
                ])));
  }
}
