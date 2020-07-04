class Email:
    def __init__(self, toEmail="", fromEmail="", subject="", body=""):
        self.toEmail = toEmail
        self.fromEmail = fromEmail
        self.subject = subject
        self.body = body

    def ToString(self):
        return(f'From: BlueSky\nTo: {self.toEmail}\n\n{self.subject}\n{self.body}')

    def appendToString(self, message):
        self.body = f'{str(self.body)}\n\n{str(message)}'
