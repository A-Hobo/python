class Customer(object):
    def __init__(self, first, last, cash, password):
        self.first =  first
        self.last = last
        self.cash = cash
        self.password = password
    def printName(self):
        return self.first + ' ' + self.last
    def printBalance(self):
        return self.cash
    def deposit(self, dep):
        self.cash += dep
        return self.cash
    def withdraw(self, wit):
        self.cash -= wit
        return self.cash
    def chngPass(self):
        if self.password == raw_input("Put in current password"):
            self.password = raw_input("Print new password")
            return self.password
        else:
            return "Error"
class Investor(Customer):
    def __init__(self, first, last, cash, password, shares = None):
        super(Investor, self).__init__(first, last, cash, password)
        if shares == None:
            self.shares = {}
        else:
            self.shares = shares
    def addStock(self, stock, share):
        if stock not in self.shares:
            self.shares.update({stock:share})
            return self.shares
    def printPort(self):
        return self.first + " " + self.last + " " + str(self.cash) + " " + self.password + " " + self.shares



cust_1 = Customer("Andrew","Shedd", 0, "Loserface")
inv_1 = Investor("Davey", "Schoenberger", 1000, "BigBoss123", {'Verizon': 18})
print cust_1.printName()
print cust_1.deposit(5)
print cust_1.withdraw(2)
print cust_1.chngPass()
print inv_1.shares
print inv_1.addStock("ATnT", 1)
print inv_1.printPort()
