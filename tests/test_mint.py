from brownie import *
import pytest

def test_mint(accounts, erc721Asset):
	tx = erc721Asset.mint(accounts[1], "Heart", "FL", "Colorless", "4", "GIA", "1", {"from": accounts[0]})
	print(tx)
	assert False