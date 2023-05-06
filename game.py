import random

# 1부터 45까지의 숫자 리스트 생성
numbers = list(range(1, 46))

# 6개의 숫자 무작위로 선택하여 결과 리스트에 저장
lotto_numbers = random.sample(numbers, 6)

# 오름차순으로 정렬
lotto_numbers.sort()

# 결과 출력
print("로또 번호: ", end='')
for number in lotto_numbers:
    print(number, end=' ')