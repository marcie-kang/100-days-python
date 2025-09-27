def zeros(n):
    zero = 0
    i = 5
    # 루프는 i가 n보다 작거나 같을 때까지 계속됩니다.
    # 5의 소인수 개수는 k >= 1에 대해 floor(n / 5^k)의 합입니다.
    while n // i > 0:
        zero += n // i
        i *= 5
    
    return zero

print(zeros(1200))