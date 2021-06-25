for i in range(int(input())):
    player_a_semi_point = 0
    player_b_semi_point = 0
    for i in range(int(input())):
        choice_a, choice_b = input().split()
        if(choice_a == "R" and choice_b == "S" ):
            player_a_semi_point += 1
        elif(choice_a == "S" and choice_b == "P" ):
            player_a_semi_point += 1
        elif(choice_a == "P" and choice_b == "R" ):
            player_a_semi_point += 1
        elif(choice_a == "P" and choice_b == "S" ):
            player_b_semi_point += 1
        elif(choice_a == "R" and choice_b == "P" ):
            player_b_semi_point += 1
        elif(choice_a == "S" and choice_b == "R" ):
            player_b_semi_point += 1
    if(player_a_semi_point > player_b_semi_point):
        print("Player 1")
    elif(player_a_semi_point < player_b_semi_point):
        print("Player 2")
    elif(player_a_semi_point == player_b_semi_point):
        print("TIE")
            