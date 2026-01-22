# test_calc.py
import calc
 
def test_add():
    assert calc.add(2, 3) == 5
 
def test_subtract():
    assert calc.subtract(10, 5) == 5
 
if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All tests passed!")
