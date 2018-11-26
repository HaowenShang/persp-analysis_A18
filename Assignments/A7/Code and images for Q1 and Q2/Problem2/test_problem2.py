import Problem2 as p2

def test_month_length():
    assert p2.month_length("January") == 31, "failed on January"
    assert p2.month_length("February") == 28, "failed on February"
    assert p2.month_length("February",leap_year=True) == 29, "failed on February(leap year)"
    assert p2.month_length("March") == 31, "failed on March"
    assert p2.month_length("April") == 30, "failed on April"
    assert p2.month_length("May") == 31, "failed on May"
    assert p2.month_length("June") == 30, "failed on June"
    assert p2.month_length("July") == 31, "failed on July"
    assert p2.month_length("August") == 31, "failed on August"
    assert p2.month_length("September") == 30, "failed on September"
    assert p2.month_length("October") == 31, "failed on Octuber"
    assert p2.month_length("November") == 30, "failed on November"
    assert p2.month_length("December") == 31, "failed on December"
    assert p2.month_length("abc") == None, "failed on invalid input"
    
    
