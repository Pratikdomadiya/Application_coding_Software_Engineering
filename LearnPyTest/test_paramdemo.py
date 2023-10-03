import pytest

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)

# def testLogin(demo_fixture):
#     print("Login Successful")

##############################  pytest - Parametrize - 2nd way ####################

@pytest.mark.parametrize("a, b, final",[(2,6,8),(5,8,15),(5,10,15)])
def testAdd(a,b,final):
    print("ADD Test")
    assert a+b == final
