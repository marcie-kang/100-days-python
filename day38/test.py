def solution(hp):
    general_num = int(hp / 5)
    rest_hp = hp % 5
    soldier_num = int(rest_hp / 3)
    rest_hp = rest_hp % 3

    return general_num + soldier_num + rest_hp

print(solution(23))
print(solution(24))
print(solution(999))