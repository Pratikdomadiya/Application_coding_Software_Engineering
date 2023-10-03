import pytest

def test_Login():
    print("testing logins")

def testLogoff():
    print('testing logoff')

@pytest.mark.tagName # USE TO CREATE GROUPS BASED ON tagName // RUN : pytest -m tagName
def testCalculation():
    assert 2+2 == 8