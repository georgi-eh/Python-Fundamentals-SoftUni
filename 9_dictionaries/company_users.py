users_commands = input()
users = dict()
while users_commands != "End":
    company_name, user = users_commands.split(" -> ")
    if company_name not in users.keys():
        users[company_name] = []
    if user not in users[company_name]:
        users[company_name].append(user)

    users_commands = input()
for company, users in users.items():
    print(company)
    for user in users:
        print(f"-- {user}")
