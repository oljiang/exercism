def classify(number):
    # factors = []
    divisor = 1

    if number <= 0:
        raise ValueError("ValueError exception thrown")
    
    # while divisor < number:
    #     remainder = number % divisor
    #     if remainder == 0:
    #         factors.append(divisor)
    #         divisor += 1
    #     else:
    #         divisor += 1

    factors = [i for i in range(1, int(number/2)+1) if number % i == 0]

    aliquot_sum = sum(factors)

    if number == aliquot_sum:
        answer = "perfect"
    elif number > aliquot_sum:
        answer = "deficient"
    else:
        answer = "abundant"

    return answer
