import Problem1 as p1

def test_smallest_factor():
    assert p1.smallest_factor(1) == 1, "failed on 1"
    assert p1.smallest_factor(2) == 2, "failed on smallest prime number case"
    assert p1.smallest_factor(3) == 3, "failed on small prime number cases"
    assert p1.smallest_factor(4) == 2, "failed on smallest composite number case"
    assert p1.smallest_factor(6) == 2, "failed on small composite number cases"
    assert p1.smallest_factor(9) == 3, "failed when n is the square of prime number cases"
    assert p1.smallest_factor(16) == 2, "failed when n is the square of composite number cases"
    assert p1.smallest_factor(17) == 17, "failed on large prime number cases"
    assert p1.smallest_factor(18) == 2, "failed on large composite number cases"
    
    
