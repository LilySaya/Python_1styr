# -*- coding: utf-8 -*-
"""HW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R8czc_Q8lgkbk-uBbqyO3HmruqYOYJEO
"""

import matplotlib.pyplot as plt
import random
def two_dice(nb_simulations):
  counter = [0]*12
  for _ in range(nb_simulations):
    x=random.randint(1,6)
    y=random.randint(1,6)
    counter[x+y-1] += 1
  print("Raw values:", counter)

  for i in range(12):
    counter[i]= round( counter[i]*100 / nb_simulations, 2)

  print("Simulation results:")
  
  percentage = []
  percentage = [0]*13
  for j in range(1,13):
    percentage[j] += counter[j-1]
    print(f"The dice value was {j} {percentage[j]}% of times")
  print(percentage)

  number = list(range(13))
  
  plt.bar(number,percentage)
  plt.xlabel("sum of two dices")
  plt.ylabel("percentage of the sum")
  plt.title("Probability of sum of two dices")

two_dice(100000)

""" **Homework part 2**"""

import random
import matplotlib.pyplot as plt

random.seed(20)

NB_PLAYERS = 32

STRENGTH = [random.randint(0, 100) for _ in range(NB_PLAYERS)]

def compute_winner(player1, player2):
  """ Compute the winner between two players.
  
  This function is deterministic.
  The strongest player always wins against a weaker opponent.
  In case of tie (same strength), the first player wins.
  """
  s1 = STRENGTH[player1]
  s2 = STRENGTH[player2]
  p1 = s1/(s1+s2)
  p2 = s2/(s1+s2)

  if random.choices([s1,s2],weights = [p1,p2]) == [s1]:
    return player1
  else:
    return player2


def simulate_tournament():
  """ Simulate a tournament with all NB_PLAYERS players
  
  1) Generate a random bracket
  2) Simulate the competition
  3) Return the identities of the players ranked 1 to 4
  
  Note 1: This function works only when NB_PLAYERS is a power of 2.
  Note 2: This function does not take arguments.
          It will consider NB_PLAYERS players with their strength given in the global variable STRENGTH.
  """
  players = list(range(NB_PLAYERS))  # List containing all players = [0,1,...,31]
  random.shuffle(players)            # Shuffle to generate random bracket

  n = NB_PLAYERS                     # Number of players not yet eliminated
  
  # This loop simulates all games of a given round until semi-final (excluded)
  while n > 4: # Not yet semi-final
    next_round_players = []         # List that will contain all winners of this round, i.e. players of the next round

    for k in range(n//2):           # Given n players at the begining of the round,
      p1 = players[2*k]             # there are n//2 games to be played
      p2 = players[2*k+1]           # players[0]-vs-players[1], players[2]-vs-players[3], ...
      win_p1_vs_p2 = compute_winner(p1, p2)
      next_round_players.append(win_p1_vs_p2)
    
    # Prepare for the next round
    players = next_round_players
    n = n//2
    
  # Now there are only 4 players
  # first semi-final
  p1 = players[0]
  p2 = players[1]
  win_first_semi = compute_winner(p1, p2)
  loose_first_semi = p1 + p2 - win_first_semi     # A "nice" hack to obtain the loser player
    
  # second semi-final
  p1 = players[2]
  p2 = players[3]
  win_second_semi = compute_winner(p1, p2)
  loose_second_semi = p1 + p2 - win_second_semi
  
  # final
  rank_1 = compute_winner(win_first_semi, win_second_semi)
  rank_2 = win_first_semi + win_second_semi - rank_1
    
  # third-place game
  rank_3 = compute_winner(loose_first_semi, loose_second_semi)
  rank_4 = loose_first_semi + loose_second_semi - rank_3
  
  # Return the result of the simulation
  return (rank_1, rank_2, rank_3, rank_4)   # parenthesis are optional here


def compute_stats(nb_simu):
  """ Compute statistics based on nb_simu tournaments 
  
  Let's give the following points to the top players:
      - 100 points to the winner
      - 60  points to the runner-up
      - 30  points for 3rd position
      - 10  point  for 4th position
  """
  average_point_per_player = [0]*NB_PLAYERS
  
  for _ in range(nb_simu):
    result = simulate_tournament()       # result is a tuple of four players
    rank1, rank2, rank3, rank4 = result
    average_point_per_player[rank1] += 100
    average_point_per_player[rank2] += 60
    average_point_per_player[rank3] += 30
    average_point_per_player[rank4] += 10
  
  average_point_per_player = [round(x/nb_simu,2) for x in average_point_per_player] # Again, list comprehension here
  
  # data is a *bad* name. But I did not find a good name yet...
  # Create a list of triplet. Each triplet contains:
  #     - the average points of a player
  #     - the strength of the player
  #     - the identity of the player
  # Note that the order of elements (in the triplet) is important for sorting
  data = [(average_point_per_player[i], STRENGTH[i], i) for i in range(NB_PLAYERS)]
  data.sort(reverse=True)  # Sort in reverse order to place first the player with more points
  for t in data:
    print(f"Player {t[2]} with strength {t[1]} got {t[0]} points in average")
  plt.bar(STRENGTH,average_point_per_player)
  plt.xlabel("Strength of the player")
  plt.ylabel("Average points of the player")
  plt.title("Stregth of the player vs Average points of the player")

compute_stats(1000)
