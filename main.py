numbers = open("three_digit_numbers.txt", "r")
sorted_nums = open("sorted_numbers.txt", "w")
num = numbers.read()
nums = num.split()
for count in range(300, 501):
    if str(count) not in nums:
        missin = (f"{count} is missing\n")
        print(missin)
sort_nums = str(sorted(nums))
sorted_nums.write(sort_nums)
numbers.close()
sorted_nums.close()