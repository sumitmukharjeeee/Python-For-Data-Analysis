primeNumbers = [2,3,5,7]
for prime in primeNumbers:
    print(prime)

for i in range(1,5):
    print(i*2)

squares = ["red","yellow","green","purple","blue"]
# for i in range(0,5):
#     squares[i] = "white"
# print(squares)

for square in squares:
    print(square)

squares2 = ["red","yellow","green","purple","blue"]
for i,  color in enumerate(squares):
    print(f"{i}: {color}")
# This gives values with position

for number in range(11):
    print(number)

superheroes = ["Doom","F4","Superman"]
for i, hero in enumerate(superheroes):
    print(f"{i}: {hero}")

count = 1
while count<=20:
    print(count)
    count +=1

for x in ['A', 'B', 'C']:
    print(x + 'A')