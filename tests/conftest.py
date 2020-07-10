import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass

@pytest.fixture(scope="module")
def erc721Asset(TestContract, accounts):
    return accounts[0].deploy(ERC721Asset, "Diasset", "DIAS", "diasset.space")