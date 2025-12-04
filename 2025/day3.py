total_joltage = 0
with open('day3_input.txt', 'r') as file:
    for line in file:
        bank = line.strip()
        joltages = []
        for i in range(len(bank)):
            remain = len(bank) - i
            space = 12 - len(joltages)
            while joltages and bank[i] > joltages[-1] and remain > space:
                joltages.pop()
                remain = len(bank) - i
                space = 12 - len(joltages)
            if len(joltages) < 12:
                joltages.append(bank[i])

        bank_joltage = 0
        for i in range(len(joltages)):
            bank_joltage += int(joltages[-i - 1]) * 10**i
        total_joltage += bank_joltage
print(total_joltage)