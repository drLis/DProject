import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass

@pytest.fixture(scope="module")
def token(ERC721Asset, accounts):
    return accounts[0].deploy(ERC721Asset, "Diasset", "DIAS", "diasset.space")