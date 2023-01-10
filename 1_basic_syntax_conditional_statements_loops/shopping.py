budget = int(input())
sum = 0

while budget >= sum:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        sum += int(command)

else:
    print("You went in overdraft!")