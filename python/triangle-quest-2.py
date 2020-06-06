for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((123456789//(10**(9-i)) * 10**(i-1) + 87654321 - (87654321 // 10**(i-1) * 10**(i-1))) if i !=1 else 1)
