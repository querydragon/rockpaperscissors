import random


def game(player_choice):
    choices = ['가위', '바위', '보']
    computer_choice = random.choice(choices)

    print(f"플레이어: {player_choice}")
    print(f"컴퓨터: {computer_choice}")

    if player_choice == computer_choice:
        print("비겼습니다!")
    elif (player_choice == "가위" and computer_choice == "보") or \
            (player_choice == "바위" and computer_choice == "가위") or \
            (player_choice == "보" and computer_choice == "바위"):
        print("플레이어가 이겼습니다!")
    else:
        print("컴퓨터가 이겼습니다!")


while True:
    user_input = input("가위, 바위, 보 중 하나를 선택하세요 (종료하려면 '끝'을 입력하세요): ")

    if user_input == '끝':
        print("게임을 종료합니다.")
        break

    if user_input not in ['가위', '바위', '보']:
        print("가위, 바위, 보 중에서 선택해주세요.")
        continue

    game(user_input)