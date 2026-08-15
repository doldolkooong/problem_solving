from .constants import rock_sissor_paper
import random
from .inputs import get_user_input
from .constants import mukchippa_attack

def mukchippa_game() -> dict:
    user_choice = get_user_input()
    computer_choice = random.choice(list(rock_sissor_paper.__members__))

    print(f"User 선택: {user_choice}") # 사용자의 선택 출력
    print(f"Computer 선택: {computer_choice}") # 컴퓨터의 선택 출력

    result = user_choice.is_win(rock_sissor_paper[computer_choice])
    attacker = mukchippa_attack.user_shield
    attacker = attacker.get_attacker(result)

    while True:

        if attacker == mukchippa_attack.user_attack:
            print("User은 공격을 하셔야 합니다.")
        else:
            print("User은 수비를 하셔야 합니다.")

        user_choice = get_user_input()
        computer_choice = random.choice(list(rock_sissor_paper.__members__))

        print(f"User 선택: {user_choice}") # 사용자의 선택 출력
        print(f"Computer 선택: {computer_choice}") # 컴퓨터의 선택 출력

        if user_choice.name == computer_choice:
            if attacker == mukchippa_attack.user_attack:
                return{
                        "게임 결과" : "승리",
                        "User 선택" : user_choice.name,
                        "Computer 선택" : computer_choice
                }
            else:
                return{
                        "게임 결과" : "패배",
                        "User 선택" : user_choice.name,
                        "Computer 선택" : computer_choice
                }

        result = user_choice.is_win(rock_sissor_paper[computer_choice])
        attacker = attacker.get_attacker(result)

