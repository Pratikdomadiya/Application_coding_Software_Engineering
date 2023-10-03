import pytest

@pytest.mark.skip #skip the test
def test_Login():
    print("testing logins")

@pytest.mark.tagName # USE TO CREATE GROUPS BASED ON tagName // RUN : pytest -m tagName
def testLogoff():
    print('testing logoff')



@pytest.mark.xfail #
def testCalculation():
    assert 2+2 == 8