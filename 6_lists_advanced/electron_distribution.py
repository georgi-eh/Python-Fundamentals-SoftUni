number_of_electrons = int(input())
shell = 1
list_of_shells = []
while number_of_electrons > 0:
    max_electrons_in_shell = 2 * (shell ** 2)
    if number_of_electrons >= max_electrons_in_shell:
        number_of_electrons -= max_electrons_in_shell
        list_of_shells.append(max_electrons_in_shell)
    else:
        list_of_shells.append(number_of_electrons)
        break
    shell += 1
print(list_of_shells)
