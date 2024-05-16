import pytest
from bank_account import BankAccount  # Replace with the actual module name

@pytest.fixture
def bank_account():
    return BankAccount()

@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100, 100),
    (50, 50),
    (10, 10),
])
def test_deposit(bank_account, deposit_amount, expected_balance):
    bank_account.deposit(deposit_amount)
    assert bank_account.get_balance() == expected_balance

@pytest.mark.parametrize("deposit_amount, withdraw_amount, expected_balance", [
    (100, 50, 50),
    (50, 25, 25),
    (200, 200, 0),
])
def test_withdraw(bank_account, deposit_amount, withdraw_amount, expected_balance):
    bank_account.deposit(deposit_amount)
    bank_account.withdraw(withdraw_amount)
    assert bank_account.get_balance() == expected_balance

@pytest.mark.parametrize("deposit_amount, exception, message", [
    (0, ValueError, "Deposit amount must be positive"),
    (-10, ValueError, "Deposit amount must be positive"),
])
def test_deposit_exceptions(bank_account, deposit_amount, exception, message):
    with pytest.raises(exception, match=message):
        bank_account.deposit(deposit_amount)

@pytest.mark.parametrize("initial_deposit, withdraw_amount, exception, message", [
    (100, 150, ValueError, "Insufficient funds"),
    (100, -10, ValueError, "Withdrawal amount must be positive"),
])
def test_withdraw_exceptions(bank_account, initial_deposit, withdraw_amount, exception, message):
    bank_account.deposit(initial_deposit)
    with pytest.raises(exception, match=message):
        bank_account.withdraw(withdraw_amount)
