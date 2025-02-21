
#Problem 1: Oski being a thief :(
def computePower(x,y):
    result = 1
    for oski in range(y):
        result *= x
    return result

print(computePower(2,3))

#Problem 2: Choosing what to wear so i can look slay
def temprange(readings):
    min_temp = readings[0]
    max_temp = readings[0]
    for temp in readings:
        if temp < min_temp: 
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
    return (min_temp, max_temp)

readings = [15,14,17,20,23,28,20]
print(temprange(readings))

#Problem 3: Weekend Problems :<
def weekend(day):
    return day == 6 or day == 7
day = 6 # Saturday
print(weekend(day))

#Problem 4: Fuel Calculator
def fuel_efficiency(distance, fuel): 
    return distance/fuel
distance = 70 #miles
fuel = 21.5 #gallons
print(fuel_efficiency(distance, fuel))

#Problem 5: decoding who is secretly stalking my insta
def decoding(n):
    last_digit = n%10
    remaining_number = n // 10
    multiplier = 1
    while remaining_number > 0:
        multiplier *= 10
        remaining_number //= 10
    return last_digit * multiplier + (n // 10)
n = 12345 
print(decoding(n))

#Problem 6: oski needs to stop hacking
#problem 6.1: for fruit loops
def find_min_with_for_loop(nums):
    min_value = nums [0]
    for num in nums:
        if num < min_value :
            min_value = num
    return min_value

def find_max_with_for_loops(nums):
    max_value = nums [0]
    for num in nums:
        if num > max_value: 
            max_value = num
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))
print(find_max_with_for_loops(nums))

#problem 6.2: while my head loops abracadabra over and over again
def find_min_with_while_loop(nums):
    i = 0
    min_value = nums[0]
    while i < len(nums):
        if nums[i] < min_value:
            min_value = nums[i]
        i += 1
    return min_value

def find_max_with_while_loops(nums):
    i = 0
    max_value = nums[0]
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]
        i += 1
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))
print(find_max_with_while_loops(nums))

#problem 7: counting vowels because why not
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)
text = 'UC Berkeley, founded in 1868!'
print(vowel_and_consonant_count(text))

#problem 8: calculating the root of my problems
def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
num = 2468
print(digital_root(num))
