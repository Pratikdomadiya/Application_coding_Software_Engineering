import pytest


# @pytest.fixture(scope="session", autouse=True) # autouse = automatically recognized by all the TEST function.
@pytest.fixture(scope="function", autouse=True) # autouse = automatically recognized by all the TEST function.
def setUpAndTearDown():
    #set up steps
    print(" Launch Setup ")
    print(" Open up browser")
    print(" Browse products")

    yield # this will yield the execution

    #tear down steps : these are the steps that will run after running the test case
    print("Test has been executed successfully")
    print("Logoff")
    print("Close Browser")