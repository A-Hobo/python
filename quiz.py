class Employees(object):
    hours = 40
    raise_amount = 1.04
    def __init__(self, first, last, pay, hours):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    def printName(self):
        return self.first + ' ' + self.last
    def weeklyPay(self):
        return self.pay * self.hours
    def bonusCheck(self):
        bonus = self.weeklyPay() * self.raise_amount
        return bonus
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def fromString(cls, empStr):
        first, last, pay = empStr.split("-")
        return cls(first, last, float(pay))
class Developer(Employees):
    def __init__(self, first, last, pay, hours, lan):
        super(Developer, self).__init__(first, last, pay, hours)
        self.lan = lan
class Manager(Employees):
    def __init__(self, first, last, pay, hours, employees = None):
        super(Manager, self).__init__(first, last, pay, hours)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def addEmp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remEmp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)


dev_1 = Developer("Andrew", "Shedd", .0001, 48, "python")
man_1 = Manager("Davey", "Schoenberger",50, 48 , [dev_1])
dev_2 = Developer("Ella", "Tippits", 40, 48, "python")

print dev_1.weeklyPay()
print man_1.printName()
print man_1.weeklyPay()
man_1.addEmp(dev_2)
man_1.remEmp(dev_1)

print "%s works for %s and is his worst worker" % (dev_1.first, man_1.first)
print "%s is sick and tired of %s's crap, so he fires him and hires %s, who becomes his best employee" % (man_1.first, dev_1.first, dev_2.first)
