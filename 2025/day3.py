total_joltage = 0
with open('day3_input.txt', 'r') as file:
    for line in file:
        bank = line.strip()
        battery1_joltage = -1
        barry1_ind = -1
        for battery_ind in range(len(bank[:-1])):
            battery_joltage = int(bank[battery_ind])
            if battery_joltage > battery1_joltage:
                battery1_joltage = battery_joltage
                battery1_ind = battery_ind
        battery2_joltage = -1
        for battery_ind in range(battery1_ind + 1, len(bank)):
            battery_joltage = int(bank[battery_ind])
            if battery_joltage > battery2_joltage:
                battery2_joltage = battery_joltage
        bank_joltage = battery1_joltage*10 + battery2_joltage
        total_joltage += bank_joltage
print(total_joltage)