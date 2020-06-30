class CustomerRewards:
    def __init__(self, hasDiscount=False, currentCycleDollars=0, totalDollarsSpent=0):
        self.hasDiscount = hasDiscount
        self.currentCycleDollars = currentCycleDollars
        self.totalDollarsSpent = totalDollarsSpent


class Customer:
    def __init__(self, firstName, lastName, email, phone, rewards=CustomerRewards(), inMarketingCamp=False):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.rewards = rewards
        self.inMarketingCamp = inMarketingCamp

    def joinCampaign(self):
        self.inMarketingCamp = True
