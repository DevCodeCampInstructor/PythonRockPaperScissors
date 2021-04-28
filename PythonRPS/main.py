import random
player_one_score = 0
player_two_score = 0


def run_game():
    game_type = choose_game_type()
    player_one_name = set_player_name()
    player_two_name = set_player_name()

    while player_one_score < 2 and player_two_score < 2:
        if game_type == "1":
            player_one_gesture = choose_gesture(player_one_name)
            player_two_gesture = choose_gesture(player_two_name)
            determine_round_winner(player_one_name, player_one_gesture, player_two_name, player_two_gesture)
            display_scoreboard(player_one_name, player_two_name)
            check_if_game_winner(player_one_name, player_two_name)
        elif game_type == "2":
            player_one_gesture = choose_gesture(player_one_name)
            player_two_gesture = get_random_gesture(player_two_name)
            determine_round_winner(player_one_name, player_one_gesture, player_two_name, player_two_gesture)
            display_scoreboard(player_one_name, player_two_name)
            check_if_game_winner(player_one_name, player_two_name)


def choose_game_type():
    game_type = input("Please choose Player vs Player or Player vs Computer. Type 1 for PvP or 2 for PvC")
    return game_type


def set_player_name():
    name = input("Please enter a name")
    print('Hello, {name}!'.format(name=name))
    return name


def choose_gesture(player_name):
    gesture_choice = input("Please choose a gesture. Type R for rock, P for paper, or S for scissors")
    print('{player_name} chose {gesture_choice}'.format(player_name=player_name, gesture_choice=gesture_choice))
    return gesture_choice


def get_random_gesture(player_name):
    gestures = ['R', 'P', 'S']
    random_number = random.randint(0, 2)
    random_gesture = gestures[random_number]
    print('{player_name} chose {random_gesture}'.format(player_name=player_name, random_gesture=random_gesture))
    return random_gesture


def determine_round_winner(player_one_name, player_one_gesture, player_two_name, player_two_gesture):
    global player_one_score
    global player_two_score
    if player_one_gesture == player_two_gesture:
        print('Tie!')
    elif player_one_gesture == 'R' and player_two_gesture == 'S':
        print('{player_one_name} wins the round!'.format(player_one_name=player_one_name))
        player_one_score += 1
    elif player_one_gesture == 'P' and player_two_gesture == 'R':
        print('{player_one_name} wins the round!'.format(player_one_name=player_one_name))
        player_one_score += 1
    elif player_one_gesture == 'S' and player_two_gesture == 'P':
        print('{player_one_name} wins the round!'.format(player_one_name=player_one_name))
        player_one_score += 1
    else:
        print('{player_two_name} wins the round!'.format(player_two_name=player_two_name))
        player_two_score += 1


def display_scoreboard(player_one_name, player_two_name):
    print('{player_one_name} score: {player_one_score}'.format(player_one_name=player_one_name, player_one_score=player_one_score))
    print('{player_two_name} score: {player_two_score}'.format(player_two_name=player_two_name, player_two_score=player_two_score))


def check_if_game_winner(player_one_name, player_two_name):
    global player_one_score
    global player_two_score
    if player_one_score == 2:
        print('{player_one_name} wins the game!!'.format(player_one_name=player_one_name))
    elif player_two_score == 2:
        print('{player_two_name} wins the game!!'.format(player_two_name=player_two_name))


run_game()
