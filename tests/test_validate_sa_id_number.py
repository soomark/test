from sa_idnumber.validate_sa_id_number import valid_id_length, id_is_numeric, valid_year, valid_month,valid_day,valid_gender,valid_citizen,valid_race,valid_checksum_digit


def test_id_length():
    assert valid_id_length("20010148000867") == False


def test_id_numeric():
    assert id_is_numeric("20010A4800086") == False


def test_valid_year():
    assert valid_year("A209035800085") == False


def test_valid_month():
    assert valid_month("2013305800085") == False


def test_valid_day():
    assert valid_day("2908435800085") == False


def test_valid_gender():
    assert valid_gender("2908241480085") == False


def test_valid_citizen():
    assert valid_citizen("2908343580285") == False


def test_valid_race():
    assert valid_race("2908241480075") == False
