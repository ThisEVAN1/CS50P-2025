from numb3rs import validate

def test_validate_true():
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('100.100.100.100') == True
    assert validate('50.50.50.50') == True
    assert validate('150.150.150.150') == True
    assert validate('0.50.100.255') == True
    assert validate('140.247.235.144') == True


def test_validate_false():
    assert validate('-255.-255.-255.-255') == False
    assert validate('256.256.256.256') == False
    assert validate('300.300.300.300') == False
    assert validate('1000.1000.1000.1000') == False
    assert validate('1.2.3.1000') == False
    assert validate('255') == False
    assert validate('hi') == False
    assert validate('0.0..0.') == False
