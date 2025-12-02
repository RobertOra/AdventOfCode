with open("day2_input.txt", 'r') as f:
    line = next(f)

invalid_id_sum = 0
for id_range in line.split(','):
    first_id, last_id = map(int, id_range.split('-'))

    # sum all invalid ids between first_id and last_id (inclusive)
    # invalid id - digits repeated twice

    #brute force
    for id in range(first_id, last_id + 1):
        id_str = str(id)
        for sub_len in range(len(id_str) // 2, 0, -1):
            if len(id_str) % sub_len == 0:
                sub = id_str[:sub_len]
                ind = 0

                invalid = True
                while ind < len(id_str):
                    if id_str[ind:ind + sub_len] != sub:
                        invalid = False
                        break
                    ind += sub_len

                if invalid:
                    invalid_id_sum += id
                    break

        '''
        part 1
        if len(id_str) % 2 == 1:
            continue
        mid = len(id_str) // 2
        left_half = id_str[:mid]
        right_half = id_str[mid:]
        if left_half == right_half:
            invalid_id_sum += id
        '''
print(invalid_id_sum)

