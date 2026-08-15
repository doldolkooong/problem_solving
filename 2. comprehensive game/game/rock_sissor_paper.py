from .constants import rock_sissor_paper
import random
from .inputs import get_user_input

def rsp_game() -> dict:
    user_choice = get_user_input()
    computer_choice = random.choice(list(rock_sissor_paper.__members__))

    return{
        "게임 결과" : user_choice.is_win(rock_sissor_paper[computer_choice]),
        "User 선택" : user_choice.name,
        "Computer 선택" : computer_choice
    }