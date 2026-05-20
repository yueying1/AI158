count = 0
temperature = 0
print('摄氏温度\t\t华氏温度')
while count < 10 and 0 <= temperature <= 250 :
    fahrenheit = (temperature * 9 ) / 5.0 + 32
    print(f'{temperature:<12}{fahrenheit}')
    temperature += 20
    count += 1