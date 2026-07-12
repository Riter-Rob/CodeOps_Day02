temp_input = input("Enter a temperature in °C: ")
temperature = int(temp_input)

if temperature < 15:
    print("cold")
elif 15 <= temperature <= 28:
    print("warm")
else:
    print("hot")

  


for number in range(1, 11):
    print(f"Receipt #{number}")




for num in range(1, 21):
    if num % 2 == 0:
        print(num)

print("-" * 20)


def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    return price - discount_amount


print(f"Original 100, default 10% discount: {apply_discount(100)}")
print(f"Original 100, custom 25% discount: {apply_discount(100, 25)}")

print("-" * 20)

count = 5
while count > 0:
    print(count)
    count -= 1  
print("Liftoff!")