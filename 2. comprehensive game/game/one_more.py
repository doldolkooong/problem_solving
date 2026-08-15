from .constants import rock_sissor_paper
import random
from .inputs import get_user_input




def one_more_game() -> dict:

    print("==가위 바위 보!==")

    user_choice = []
    for i in range(2):
        user_choice.append(get_user_input())
    computer_choice = random.choices(list(rock_sissor_paper.__members__), k = 2)

    print(f"User 선택: {[choice.name for choice in user_choice]}") # 사용자의 선택 출력
    print(f"Computer 선택: {computer_choice}") # 컴퓨터의 선택 출력 

    while True:
        final_user_choice = input(f"{[choice.name for choice in user_choice]} 중 하나 골라주세요.").strip()
        
        final_computer_choice = random.choice(list(computer_choice))

        print("~하나 빼기!~")

        if final_user_choice not in [choice.name for choice in user_choice]:
            print("다시 선택해주세요..^^;;")
            continue

        final_user_choice = rock_sissor_paper[final_user_choice]

        print(f"<ser의 선택: {final_user_choice.name}")
        print(f"computer의 선택 : {final_computer_choice}")

        return{
            "게임 결과" : final_user_choice.is_win(rock_sissor_paper[final_computer_choice]),
            "User 선택" : final_user_choice.name,
            "Computer 선택" : final_computer_choice
        }