def loading_bar(integer):
    counter = int(integer / 10)
    percentage = str(integer) + "% "
    if counter == 10:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        special_chars = counter * "%"
        dots = (10 - counter) * "."
        print(f"{percentage}[{special_chars}{dots}]")
        print("Still loading...")

integer = int(input())
loading_bar(integer)
