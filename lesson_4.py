class SavingAccount():...

class CheckingAccount():...

class BankAccount(SavingAccount,CheckingAccount):...
class Stock():...
class Bond():...
class Security(Bond,Stock):...
class InterestBearingitem(BankAccount,Security):...
class RealEstate():...
class Asset(BankAccount,RealEstate,Security):...

class Insurableltem(BankAccount,RealEstate):...

print(BankAccount.mro(), InterestBearingitem.mro(),Asset.mro(),Insurableltem)