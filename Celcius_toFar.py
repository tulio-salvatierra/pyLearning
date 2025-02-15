celcius_value = int(input("Enter the temperature in Celcius between 0 and 20: "))

print("Number    Celcius     Fahrenheit")
print("------    -------     ----------")

for celcius in range(celcius_value, 31):
    fahrenheit = (9/5) * celcius + 32
    celcius_from_F = (fahrenheit - 32) * 5/9
    print(f"{celcius:2} {celcius:8.2f} {fahrenheit:12.2f} {celcius_from_F:12.2f}")

