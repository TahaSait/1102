numbers = open("three_digit_numbers.txt")
num = numbers.read()
nums = num.split()
sort_nums = sorted(nums)
print(sort_nums)


numbers.close()