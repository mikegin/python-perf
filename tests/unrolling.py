def test_sum_list_unrolled_0(size):
    total = 0.0
    numbers = [float(i) for i in range(size)]
    for i in range(size):
        total += numbers[i]
    return total

def test_sum_list_unrolled_2(size):
    total1 = 0.0
    total2 = 0.0
    numbers = [float(i) for i in range(size)]
    n = len(numbers)
    
    for i in range(0, n - 1, 2):
        total1 += numbers[i]
        total2 += numbers[i + 1]
    
    if n % 2 != 0:
        total1 += numbers[-1]
    
    return total1 + total2

def test_sum_list_unrolled_4(size):
    total1 = 0.0
    total2 = 0.0
    total3 = 0.0
    total4 = 0.0
    numbers = [float(i) for i in range(size)]
    n = len(numbers)
    
    for i in range(0, n - 3, 4):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
    
    for i in range(n - (n % 4), n):
        total1 += numbers[i]
    
    return total1 + total2 + total3 + total4

def test_sum_list_unrolled_8(size):
    total1 = 0.0
    total2 = 0.0
    total3 = 0.0
    total4 = 0.0
    total5 = 0.0
    total6 = 0.0
    total7 = 0.0
    total8 = 0.0
    numbers = [float(i) for i in range(size)]
    n = len(numbers)
    
    for i in range(0, n - 7, 8):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
        total5 += numbers[i + 4]
        total6 += numbers[i + 5]
        total7 += numbers[i + 6]
        total8 += numbers[i + 7]
    
    for i in range(n - (n % 8), n):
        total1 += numbers[i]
    
    return total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8

def test_sum_list_unrolled_16(size):
    total1 = 0.0
    total2 = 0.0
    total3 = 0.0
    total4 = 0.0
    total5 = 0.0
    total6 = 0.0
    total7 = 0.0
    total8 = 0.0
    total9 = 0.0
    total10 = 0.0
    total11 = 0.0
    total12 = 0.0
    total13 = 0.0
    total14 = 0.0
    total15 = 0.0
    total16 = 0.0
    numbers = [float(i) for i in range(size)]
    n = len(numbers)
    
    for i in range(0, n - 15, 16):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
        total5 += numbers[i + 4]
        total6 += numbers[i + 5]
        total7 += numbers[i + 6]
        total8 += numbers[i + 7]
        total9 += numbers[i + 8]
        total10 += numbers[i + 9]
        total11 += numbers[i + 10]
        total12 += numbers[i + 11]
        total13 += numbers[i + 12]
        total14 += numbers[i + 13]
        total15 += numbers[i + 14]
        total16 += numbers[i + 15]
    
    for i in range(n - (n % 16), n):
        total1 += numbers[i]
    
    return total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16