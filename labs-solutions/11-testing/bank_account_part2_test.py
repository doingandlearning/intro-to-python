import pytest
from bank_account import BankAccount


@pytest.fixture
def bank_account():
    return BankAccount()

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 0

def test_deposit(bank_account):
    bank_account.deposit(100)
    assert bank_account.get_balance() == 100

def test_withdraw(bank_account):
    bank_account.deposit(100)
    bank_account.withdraw(50)
    assert bank_account.get_balance() == 50

def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bank_account.withdraw(50)

def test_negative_deposit(bank_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        bank_account.deposit(-10)

def test_negative_withdraw(bank_account):
    bank_account.deposit(100)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        bank_account.withdraw(-10)

def test_reset_account(bank_account):
    bank_account.deposit(100)
    bank_account.reset_account()
    assert bank_account.get_balance() == 0
