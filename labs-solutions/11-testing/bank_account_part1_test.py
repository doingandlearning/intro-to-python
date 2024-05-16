import pytest
from bank_account import BankAccount

def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

def test_withdraw():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.get_balance() == 50

def test_withdraw_insufficient_funds():
    account = BankAccount()
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(50)

def test_negative_deposit():
    account = BankAccount()
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-10)

def test_negative_withdraw():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-10)

def test_reset_account():
    account = BankAccount()
    account.deposit(100)
    account.reset_account()
    assert account.get_balance() == 0
