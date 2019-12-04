def check_pw(number) :
    num_string = str(number)
    is_incrementing, has_double = True, False
    last_character = num_string[0]
    for char in num_string[1:] :
        has_double = has_double or (char == last_character and num_string.find(str(char)*3) == -1)
        is_incrementing = is_incrementing and char >= last_character
        last_character = char
    return is_incrementing and has_double

lower_threshold, upper_threshold = 278384, 824795
count = 0
for num in range(lower_threshold,upper_threshold) :
    if check_pw(num) :
        count += 1
print(count)