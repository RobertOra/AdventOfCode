with open("day2_input.txt", 'r') as f:
    line = next(f)

invalid_id_sum = 0
for id_range in line.split(','):
    first_id, last_id = map(int, id_range.split('-'))

    # sum all invalid ids between first_id and last_id (inclusive)
    # invalid id - digits repeated twice

    # optimized
    for id in range(first_id, last_id + 1):
        id_str = str(id)
        repeat_check_str = id_str*2
        repeat_check_str = repeat_check_str[1:-1]
        if id_str in repeat_check_str:
            invalid_id_sum += id
print(invalid_id_sum)

