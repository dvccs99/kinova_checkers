import 'package:flutter/material.dart';

class GamePage extends StatefulWidget {
  const GamePage({super.key});

  @override
  _CheckersBoardState createState() => _CheckersBoardState();
}

class _CheckersBoardState extends State<GamePage> {
  final int boardSize = 8;
  List<List<String>> board = [];
  List<List<String>> pieces = [];

  @override
  void initState() {
    super.initState();
    _initializeBoard();
    _initializePieces();
  }

  void _initializeBoard() {
    board = List.generate(boardSize, (i) {
      return List.generate(boardSize, (j) {
        return (i + j) % 2 != 0 ? 'empty' : 'black';
      });
    });
  }

  void _initializePieces() {
    pieces = List.generate(boardSize, (i) {
      return List.generate(boardSize, (j) {
        if (i < 3 && (i + j) % 2 != 0) return 'verde'; // Peças verdes
        if (i > 4 && (i + j) % 2 != 0) return 'roxo'; // Peças roxas
        return '';
      });
    });

    // Adicionar damas verdes e roxas
    pieces[0][1] = 'verde_dama';
    pieces[0][3] = 'verde_dama';
    pieces[0][5] = 'verde_dama';
    pieces[0][7] = 'verde_dama';
    pieces[7][0] = 'roxo_dama';
    pieces[7][2] = 'roxo_dama';
    pieces[7][4] = 'roxo_dama';
    pieces[7][6] = 'roxo_dama';
  }

  void _onTileTap(int i, int j) {
    setState(() {
      _showPopup();
    });
  }

  void _showPopup() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Jogo de damas Equipe 5'),
          content: Text('??????????????????????'),
          actions: <Widget>[
            TextButton(
              child: Text('Fechar'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 50, 57, 100),
      appBar: AppBar(
        centerTitle: true,
        title: Text('Tabuleiro - Equipe 5'),
        backgroundColor: Colors.white,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            SizedBox(height: 50.0),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                
                Column(
                   children: [
                    Image.asset('assets/image/humano2.png', width: 150, height: 150),
                    Text(
                      'Peças: 12',
                      style: TextStyle(
                        fontSize: 16.0,
                        color: Colors.white,
                      ),
                    ),
                   ],
                ),
                SizedBox(width: 35),
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    for (int i = 0; i < boardSize; i++)
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          for (int j = 0; j < boardSize; j++) _buildTile(i, j),
                        ],
                      ),
                  ],
                ),
                SizedBox(width: 35),
                Column(
                   children: [
                    Image.asset('assets/image/robo.jpg', width: 150, height: 150),
                    Text(
                      'Peças: 12',
                      style: TextStyle(
                        fontSize: 16.0,
                        color: Colors.white,
                      ),
                    ),
                   ],
                ),
              ],
            ),
            // Column(
            //   children: [
            //     TextField(
            //       decoration: InputDecoration(
            //         labelText: 'Jogada',
            //         border: OutlineInputBorder(
            //           borderRadius: BorderRadius.all(
            //             Radius.circular(5),
            //           )
            //         ), 
            //       ),
            //     ),
            //   ],
            // ),
            Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () {
                    Navigator.pushNamed(context, 'game_page');
                  },
                  child: Text('Vez do Robo'),
                ),
              ],
            ),
            SizedBox(height: 50.0),
          ],
        ),
      ),
    );
  }

  Widget _buildTile(int i, int j) {
    bool isWhiteTile = board[i][j] == 'empty';
    Color tileColor = isWhiteTile ? Colors.white : Colors.black;
    Color pieceColor;
    Widget pieceWidget;

    if (pieces[i][j] == 'verde') {
      pieceColor = Colors.green;
      pieceWidget = _buildPiece(pieceColor);
    } else if (pieces[i][j] == 'roxo') {
      pieceColor = Colors.purple;
      pieceWidget = _buildPiece(pieceColor);
    } else if (pieces[i][j] == 'verde_dama') {
      pieceWidget = _buildQueen(Colors.green);
    } else if (pieces[i][j] == 'roxo_dama') {
      pieceWidget = _buildQueen(Colors.purple);
    } else {
      pieceWidget = SizedBox.shrink(); // sem peça
    }

    return GestureDetector(
      onTap: () => _onTileTap(i, j),
      child: Container(
        width: 40.0,
        height: 40.0,
        color: tileColor,
        child: Center(child: pieceWidget),
      ),
    );
  }

  Widget _buildPiece(Color color) {
    return Container(
      width: 30.0,
      height: 30.0,
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.circle,
      ),
    );
  }

  Widget _buildQueen(Color color) {
    return Container(
      width: 30.0,
      height: 30.0,
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.rectangle,
        borderRadius: BorderRadius.circular(15.0),
      ),
      child: Center(
        child: Icon(Icons.star, color: Colors.white),
      ),
    );
  }
}
