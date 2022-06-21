import unittest
from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_exists(self):
        uba = account.Account
        self.assertIsNotNone(uba)

    def test_that_account_has_name(self):
        uba = account.Account("funmi", 12, "12345")
        self.assertEqual("funmi", uba.name)

    def test_that_account_has_age(self):
        uba = account.Account("funmi", 12, "12345")
        self.assertEqual(12, uba.age)

    def test_that_account_has_number(self):
        uba = account.Account("funmi",12, "12345")
        self.assertEqual("12345", uba.number)
        
    def test_that_account_can_deposit(self):
        uba = account.Account("funmi", 12, "12345")
        self.assertEqual(0, uba.balance)
        uba.deposit(500)
        self.assertEqual(500, uba.balance)

    def test_that_account_can_withdraw(self):
        uba = account.Account("funmi", 12, "12345")
        uba.deposit(3000)
        uba.withdraw(2000)
        self.assertEqual(1000, uba.balance)


    def test_that_account_can_transfer(self):
        uba = account.Account("funmi", 12, "12345")
        uba.deposit(2000)
        uba.transfer(4000, "other")
        self.assertEqual(2000, uba.balance)



        










#
#     def account_can_be_created(self):
#         account1 = account_package.Account("Dolapo")
#         self.assertIsNotNone(account1)
