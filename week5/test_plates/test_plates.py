from plates import is_valid


def test_character_amount():
    assert is_valid("e") == False
    assert is_valid("oiwejroijwrj") == False
    assert is_valid("hi") == True
    assert is_valid("helloo") == True


def test_start_with_2_letters():
    assert is_valid("12") == False
    assert is_valid("h1") == False
    assert is_valid("p1zza") == False
    assert is_valid("12eee") == False
    assert is_valid("ie") == True


def test_letter_after_number():
    assert is_valid("hi1i") == False
    assert is_valid("h0000e") == False
    assert is_valid("he110") == True


def test_first_num_is_0():
    assert is_valid("0bee") == False
    assert is_valid("eee0") == False
    assert is_valid("jj00") == False
    assert is_valid("by01") == False
    assert is_valid("op100") == True
    assert is_valid("evv909") == True
    assert is_valid("vv1001") == True


def test_punctuation_marks():
    assert is_valid("wowie!") == False
    assert is_valid("hi?") == False
    assert is_valid("(2%*&)") == False
    assert is_valid("ere...") == False
    assert is_valid("wa we") == False
