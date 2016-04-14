__author__ = 'lyndsay.beaver'


def adding(a,b):
    return a + b

def test_adding():
    assert adding(3,4) == 7
    assert adding(3,2) == 5
    assert adding(99,49) != 7
    print("All tests pass for function addion()")
    return(adding(24, 12))

print(test_adding())

