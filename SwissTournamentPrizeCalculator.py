'''
TODO:

Clean up code, make it less hacky

Add ability calculate prizes and profit
'''

def check_for_1(to_check):

    # check to see if a winner has been determined. Returns True if so

    for wins, players in to_check.items():

        if players == 1 and wins > 1 :

            return True
            # only returns true if a value in the dict has only 1 player in it
            # a value of 1 indicates that a winner for a tournament has been
            # determined, as there is no other player with the same number of
            # wins

    return False

forced_rounds = 0

# if set to a number greater than 0, the results after n number of rounds
# will be calculated instead of playing out til there is 1 undefeated player

players = 0

while players < 4:

    try:

        print('Please enter a number of players.')
        print('Number of players must be greater than 3')

        players = int(input('> '))

    except ValueError:

        print('\nERROR! That was not a number!\n')

rounds = 0

wins_dict = {0: players}

while check_for_1(wins_dict) == False:

    round_down = False
    # Every other time an odd number of players occurs in a round,
    # instead of rounding the number of winners up, they are rounded
    # down instead to help simulate real world tournament results

    rounds += 1

    hold_wins = []
    # holds tuples with the number of wins + number of players with that record

    # starts off all players in the 0 wins bracket

    most_wins_first = reversed(list(wins_dict.items()))
    # dict is built in ascending order. Tournament pairings are calculated
    # in decending order, so dict is reversed before being iterated over

    for wins, plyrs_w_wins in most_wins_first:

        # wins is the key, number of wins the player has
        # player is the number of players with that number of wins

        if plyrs_w_wins % 2 == 0:
            
            # check for even number of players

            winners = plyrs_w_wins // 2

        else:

            if round_down == False:
                
                winners = int(plyrs_w_wins / 2 + .5)
                # Counts for best case scenario where the winner always wins
                # when paired down, and counts byes

                round_down = True
                # When a round up occurs, the next result odd will be
                # rounded down

            else:

                winners = plyrs_w_wins // 2
                
                round_down = False

        hold_wins.append((wins + 1, winners))
        # increments the wins from the dict key by 1 and adds that and the number
        # of winners to the tuple

        hold_wins.append((wins, plyrs_w_wins - winners))
        # Keeps the current number of wins, aka the players that lost
        # and has the number of players who lost.

    wins_dict = wins_dict.fromkeys(wins_dict, 0)
    # clears all previous entries in the dictionary, to be updated
    # in the for loop below.

    for results in hold_wins:

        wins = results[0]
        players_in_bracket = results[1]

        if wins_dict.get(wins) == None:

            wins_dict[wins] = players_in_bracket

        else:

            wins_dict[wins] += players_in_bracket

    if rounds == forced_rounds:

        break

print(f'Results after {rounds} rounds:')

desc_standings = reversed(list(wins_dict.items()))
# reversed so that players with most wins are displayed first

for k, i in desc_standings:
    
    print(f'{k}-{rounds-k}: {i}')    
