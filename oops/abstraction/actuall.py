
'''

Abstraction is contract specifire which hold contract between abstract class and actual class
'''

from oops.abstraction.base import RBI

class Hdfc(RBI):

    def maximumWithdraw(self):
        return 'Maximum Limit of withdraw is 20k'

    def dailyLimit(self):
        return 'Daily Limit is 40K'

    def intrestRate(self):
        return 'Intrest rate is 9.9%'

cust1=Hdfc()


print(cust1.dailyLimit())