from __future__ import annotations
import enum

# 가위 바위 보 저장한 상수
# 가위 바위 보 낸 것을 토대로 게임 결과를 저장하는 함수 생성
class rock_sissor_paper(enum.Enum):
    가위 = 1
    바위 = 2
    보 = 0

    def is_win(self, computer : rock_sissor_paper) -> str:
        result = (self.value - computer.value) % 3

        return game_result(result).name

# 게임 결과를 저장한 상수 game_result
# 1이면 이김, 2면 짐, 0이면 비김
class game_result(enum.Enum):
    win = 1 
    lose = 2
    draw = 0

class game_type(enum.Enum):
    가위바위보 = enum.auto()
    하나빼기 = enum.auto()
    묵찌빠 = enum.auto()

class mukchippa_attack(enum.Enum):
    user_attack = 1
    user_shield = 0

    def get_attacker(self, result):
        if result == game_result.win.name:
            return self.user_attack
        elif result == game_result.lose.name:
            return self.user_shield
        return self
