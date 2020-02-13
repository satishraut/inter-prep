from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def maximumWithdraw(self):
        pass

    @abstractmethod
    def dailyLimit(self):
        pass

    @abstractmethod
    def intrestRate(self):
        pass