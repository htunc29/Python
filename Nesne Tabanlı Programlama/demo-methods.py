class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0.0
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withDraw(self,amount):
        self.balance-=amount
        return self.balance
hesap=BankAccount("Hüseyin Tunç")
sonuc=hesap.deposit(1000)
sonuc=hesap.withDraw(250.70)
print(f"{hesap.owner} bey hesabınızda anlık para miktarı:{hesap.balance}")

