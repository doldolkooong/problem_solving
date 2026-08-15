from game.constants import game_type
from game.prints import print_game_result
from game.rock_sissor_paper import rsp_game
from game.game_choice import game_choice
from game.mukchippa import mukchippa_game
from game.one_more import one_more_game

def run_game():
    game_style = game_choice()
    game_result = None

    # 선택한 게임
    if game_style == game_type.가위바위보:
        game_result = rsp_game()

    elif game_style == game_type.하나빼기:
        game_result = one_more_game()

    elif game_style == game_type.묵찌빠:
        game_result = mukchippa_game()


    if game_result:
        print_game_result(
            result = game_result['게임 결과'],
            user_value = game_result['User 선택'],
            computer_value = game_result['Computer 선택']
        )

if __name__ == "__main__":
    run_game()
