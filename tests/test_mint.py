from brownie import *
import pytest

def test_mint(accounts, token):
	tx = token.mintToken(accounts[1], "Heart", "FL", "Colorless", "4", "GIA", "1", {"from": accounts[0]})
	print(tx)
	assert False