from brownie import *
import pytest

def test_token_information(accounts, token):
	assert token.name() == "Diasset"
	assert token.symbol() == "DIAS"
	assert token.baseURI() == "diasset.space"
	assert token.totalSupply() == 0
	assert token.hasRole(token.DEFAULT_ADMIN_ROLE(), accounts[0])
	assert token.hasRole(token.MINTER_ROLE(), accounts[0])
	assert token.hasRole(token.PAUSER_ROLE(), accounts[0])
	assert token.paused() == False

def test_multi_mint(accounts, token):
	total = token.totalSupply()
	balance = token.balanceOf(accounts[1])
	tx1 = token.mintToken(accounts[1], "Heart", "FL", "Colorless", "4", "GIA", "1", {"from": accounts[0]})
	tx2 = token.mintToken(accounts[1], "Heart", "FL", "Colorless", "4", "GIA", "2", {"from": accounts[0]})

	assert len(tx1.events) == 1
	assert len(tx2.events) == 1
	assert tx1.events["Transfer"]["from"] == "0x0000000000000000000000000000000000000000"
	assert tx1.events["Transfer"]["to"] == accounts[1].address
	assert tx1.events["Transfer"]["tokenId"] == 0
	assert token.totalSupply() == total + 2
	assert token.balanceOf(accounts[1]) == balance + 2

def test_single_mint(accounts, token):
	token.mintToken(accounts[1], "Heart", "FL", "Colorless", "4", "GIA", "1", {"from": accounts[0]})

	info = token.getDiamondInfoByTokenId(0)
	assert info[0] == "Heart"
	assert info[1] == "FL"
	assert info[2] == "4"
	assert info[3] == "GIA"
	assert info[4] == "Colorless"