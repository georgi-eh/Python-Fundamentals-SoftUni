class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        text = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        return text


command = input()
emails = []
while command != "Stop":
    tokens = command.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

emails_sent = list(map(int, input().split(", ")))

for idx in emails_sent:
    emails[idx].send()
for email in emails:
    print(email.get_info())
