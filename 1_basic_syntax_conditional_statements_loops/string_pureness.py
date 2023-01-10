num = int(input())

for _ in range(num):
    text = input()
    for char in text:
        if (char == ",") or (char == ".") or (char == "_"):
            print(f"{text} is not pure!")
            break
    else:
        print(f"{text} is pure.")
