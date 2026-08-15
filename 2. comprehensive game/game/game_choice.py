from .constants import game_type

def game_choice() -> game_type:
    user_game_choice = input("진행하고 싶은 게임을 골라주세요 : ").strip()

    if user_game_choice not in game_type.__members__:
        print("가위바위보, 묵찌빠, 하나빼기 중 골라주세요")
        return game_choice()

    return game_type[user_game_choice]

if __name__ == "__main__":
    print(game_choice())