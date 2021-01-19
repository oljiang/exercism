def is_armstrong_number(number):
    num_list = []
    
    for i in str(number):
        num_list.append(int(i))
    
    digit_count = len(num_list)
    
    power_list = [i ** digit_count for i in num_list]
    num_sum = sum(power_list)    

    return num_sum == number
