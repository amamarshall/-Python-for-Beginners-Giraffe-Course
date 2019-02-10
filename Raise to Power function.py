def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


base_num = float(input("Enter base number: "))
power_num = int(input("Enter power number: "))

print(raise_to_power(base_num, power_num))
