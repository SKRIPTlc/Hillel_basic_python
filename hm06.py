chess_players = {
  "Carlsen, Magnus": 1865,
  "Firouzja, Alireza": 2804,
  "Ding, Liren": 2799,
  "Caruana, Fabiano": 1792,
  "Nepomniachtchi, Ian": 2773
}

swapped_chess_players = {rating: f"{player.split(',')[0]} {player.split(',')[1][1]}."
                         for player, rating in chess_players.items() if rating > 2000}
