def print_game_result(result:str, user_value:str=None, computer_value:str=None) -> None:
    if user_value and computer_value:
        print(f"User 선택 : {user_value} \nComputer 선택 : {computer_value}")

    print(f"게임 결과 :  {result}")

