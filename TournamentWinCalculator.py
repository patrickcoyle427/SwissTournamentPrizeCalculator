#!/usr/bin/python3

'''
TournamentWinCalculator - Simulates a tournament to determine best-case scenario
final standings, which assumes the paired-down player always wins.

Asks the user for the number of participants, and whether or not they wish to cap
the number of rounds played. Displays the final results at the end.
'''

def win_calc():

    # holds and runs through the functions that make the win calcualtor work

    players = get_players()
    # gets the number of players in the event, stored as an int
    
    forced_rounds = get_rounds()
    # Gets the number of rounds if it is capped, otherwise is 0
    # stored as an int

    results = calculate_results(players, forced_rounds)
    # Gets the final results of the tournament either after n rounds or
    # when there is 1 undefeated player.
    # Function returns a tuple that contains the final results saved as a dict,
    # along with the number of rounds played, stored as an int

    print_standings(results)
    # Displays the final results of the event and the number of rounds played.

def get_players():

    players = 0

    while players < 4:

        try:

            print('Please enter a number of players.')
            print('Number of players must be greater than 3')

            players = int(input('> '))

        except ValueError:

            print('\nERROR! That was not a number!\n')

    return players

def get_rounds():

    # if set to a number greater than 0, the results after n number of rounds
    # will be calculated instead of playing out til there is 1 undefeated player

    while True:

        try:
            
            print('Enter a forced number of rounds. Otherwise type 0 to play the event')
            print('out until there is 1 undefeated player.')

            forced_rounds = int(input('> '))

            if forced_rounds < 0:

                print('Round number must be greater than 0')

                continue

            else:

                break

        except ValueError:

            print('\nERROR! That was not a number!\n')

    return forced_rounds        

def check_for_1(to_check, rounds_forced = False):

    # check to see if a winner has been determined. Returns True if so

    if rounds_forced == True:

        return False

        # returns false if rounds_forced is True. This will play the event out
        # until the number of rounds specified is reached instead of checking
        # for a win bracket with only 1 player in it.

    for wins, players in to_check.items():

        if players == 1 and wins > 1 :

            return True
            # only returns true if a value in the dict has only 1 player in it
            # a value of 1 indicates that a winner for a tournament has been
            # determined, as there is no other player with the same number of
            # wins

    return False

def calculate_results(players, forced_rounds):

    # runs the tournament simulation and determines the results of the event
    # after n number of rounds or until there is 1 undefeated player.

    rounds = 0

    wins_dict = {0: players}

    if forced_rounds > 0:

        forced = forced_rounds
        
        set_rounds = True
        # set_rounds is passed into check_for_1. If set_rounds is true,
        # it makes that function always return false, instead using
        # a rounds == forced check to break the loop

    else:

        forced = 0

        set_rounds = False

    while check_for_1(wins_dict, set_rounds) == False:

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

        if rounds == forced:

            break

    return (wins_dict, rounds)

def print_standings(event_info):

    # displays the final results

    results = reversed(list(event_info[0].items()))
    # reversed so that players with the most wins are displayed first

    rounds = event_info[1]

    print(f'Results after {rounds} rounds:')

    for k, i in results:
        
        print(f'{k}-{rounds-k}: {i}')

if __name__ == '__main__':

    win_calc()
