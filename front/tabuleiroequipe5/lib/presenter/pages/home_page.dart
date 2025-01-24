import 'package:flutter/material.dart';


class HomePage extends StatefulWidget {
  // Classe que representa a tela de formulário que estende de StatefulWidget que é um widget que pode ser atualizado diferente de StatelessWidget
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState(); // retorna uma instância da classe _FormPageState que gerencia o estado da tela FormPage
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 50, 57, 100),
        appBar: AppBar(
          centerTitle: true,  
        title: Text('Jogo de Damas - Equipe 5'),
        backgroundColor: Colors.white,
      ),

      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            // Container(
            //   padding: EdgeInsets.all(16.0),
            //   margin: EdgeInsets.only(top: 20.0),
            //   decoration: BoxDecoration(
            //     color: Colors.white,
            //     boxShadow: [
            //       BoxShadow(
            //         color: Colors.black12,
            //         blurRadius: 0.0,
            //         spreadRadius: 0.0,
            //       ),
            //     ],
            //   ),
            //   child: Text(
            //     'Jogo de Damas: Equipe 5',
            //     style: TextStyle(
            //       fontSize: 18.0,
            //       fontWeight: FontWeight.normal,
                  
            //     ),
            //   ),
            // ),
            SizedBox(height: 50.0),
            Image(
                  image: AssetImage('assets/image/tabuleiro2.png'),
                  width: 500,
                  height: 350,
            ),
            Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () {Navigator.pushNamed(context, 'game_page');},
                  child: Text('Robo'),
                ),
                SizedBox(width: 20.0),
                ElevatedButton(
                  onPressed: () {Navigator.pushNamed(context, 'game_page');},
                  child: Text('Humano'),
                ),
                SizedBox(width: 20.0),
                ElevatedButton(
                  onPressed: () {Navigator.pushNamed(context, 'game_page');},
                  child: Text('Aleatorio'),
                ),
              ],
            ),
            SizedBox(height: 30.0),
          ],
        ),
      ),
    );
  }
}
