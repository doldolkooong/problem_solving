import random
from .constants import rock_sissor_paper

def get_user_input() -> rock_sissor_paper:
    user_input = input("가위, 바위, 보 중 하나를 선택하세요").strip()

    if user_input not in rock_sissor_paper.__members__:
        print("다시 선택해주세요..^^;;")
        return get_user_input()

    return rock_sissor_paper[user_input]

if __name__ == "__main__":
    print(get_user_input())
