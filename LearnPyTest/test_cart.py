import pytest

# @pytest.fixture(scope='function') # (default): The fixture is created and destroyed for each test function that uses it.   This is the most common scope and is suitable for most use cases.
# def setUpAndTearDown():
#     #set up steps
#     print(" Launch Setup ")
#     print(" Open up browser")
#     print(" Browse products")
#
#     yield # this will yield the execution
#
#     #tear down steps : these are the steps that will run after running the test case
#     print("Test has been executed successfully")
#     print("Logoff")
#     print("Close Browser")






def testAddItemtoCart():
    '''
    Required to execute some predefined fixtures/test before executing this test
    :param setUp: This fixture will run before executing this test
    :return:print the statement below
    '''
    print("testing add items from cart")

def testRemoveItemtoCart():
    print('testing remove items from cart')