import pytest
import Problem3 as p3

def test_operate():
    assert p3.operate(5, 6, "+") == 11, "addition error"
    assert p3.operate(5, 6, "-") == -1, "subtraction error"
    assert p3.operate(5, 6, "*") == 30, "subtraction error"
    assert p3.operate(6, 5, "/") == 1.2, "division error"
    with pytest.raises(TypeError) as excinfo1:
        p3.operate(5, 6, 7)
    assert excinfo1.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo2:
        p3.operate(5, 0, "/")
    assert excinfo2.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo3:
        p3.operate(5, 6, "a")
    assert excinfo3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
    
