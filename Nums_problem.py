def nums(int_num, int_flo):
    int_text = input('give me a number: ')
    int_num = int(int_text)

    int_text1 = input('Give me a float number: ')
    int_flo = float(int_text1)

    result = int_num * int_flo
    print('Your result is: ' + result)

print(nums)