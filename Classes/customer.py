class CustomerRewards:
    def __init__(self, hasDiscount=False, currentCycleDollars=0, totalDollarsSpent=0):
        self.hasDiscount = hasDiscount
        self.currentCycleDollars = currentCycleDollars
        self.totalDollarsSpent = totalDollarsSpent

    def resetCycle(self):
        self.hasDiscount = True
        self.currentCycleDollars = 0

    def useDiscount(self):
        self.hasDiscount = False

    def incrementCycleDollars(self, amt):
        self.currentCycleDollars = self.currentCycleDollars + int(amt)

    def incrementTotalDollars(self, amt):
        self.totalDollarsSpent = self.totalDollarsSpent + int(amt)

    def getCycleDollars(self):
        return self.currentCycleDollars

    def getTotalDollars(self):
        return self.totalDollarsSpent

    def hasDiscount(self):
        return self.hasDiscount

    def totalMinusDiscount(self, amount):
        return int(amount) * .90

    def totalDiscount(self, amount):
        return int(amount) * .10


class Customer:
    def __init__(self, firstName, lastName, email, rewards=CustomerRewards()):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.transactions = []
        self.rewards = rewards

    def get_fullname(self):
        return f'{self.firstName} {self.lastName}'

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def transactionCount(self):
        return len(self.transactions)

    def getTransactions(self):
        return self.transactions
