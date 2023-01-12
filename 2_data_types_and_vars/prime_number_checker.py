number = int(input())
counter = 0
for num in range(2, number): # no need to check division by 1 and division by he num itself
    if number % num == 0:
        counter += 1

if counter >= 1:
    print("False")
else:
    print("True")
