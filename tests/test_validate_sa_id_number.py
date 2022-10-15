import pytest
from sa_id_validation.sa_id_number import is_id_number_valid

@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086', 'Valid ID number'),
        ('2909035800085', 'Valid ID number'),
        ('29090358000851','Invalid ID number'),
        ('2909035800','Invalid ID number'),
    ),
)


def test_correct_lenght(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086','Valid ID number'),
        ('2909035800085','Valid ID number'),
        ('20A1014800086','Invalid ID number'),
        ('2001s14800086','Invalid ID number'),
        ('2001+148"0086','Invalid ID number'),
        
    ),
)


def test_number_character_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086','Valid ID number'),
        ('2909035800085','Valid ID number'),
        ('2!01014800086','Invalid ID number'),
        ('2=09035800085','Invalid ID number'),        
    ),
)


def test_year_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086','Valid ID number'),
        ('2909035800085','Valid ID number'),
        ('20r1014800086','Invalid ID number'),
        ('290-035800085','Invalid ID number'),
        ('2013014800086','Invalid ID number'),
        ('0000014800086','Invalid ID number'),
    ),
)


def test_month_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086','Valid ID number'),
        ('2909035800085','Valid ID number'),
        ('2004314800086','Invalid ID number'),
        ('2002304800086','Invalid ID number'),
        ('2904315800085','Invalid ID number'),
        ('0000004800086','Invalid ID number'),
    ),
)


def test_day_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086','Valid ID number'),
        ('2909035800085','Valid ID number'),
        ('2909030000085','Valid ID number'),
    ),
)


def test_gender_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted               


@pytest.mark.parametrize(
    'test_input,excepted',
    (
        ('2001014800086', 'Valid ID number'),
        ('2909035800085', 'Valid ID number'),
        ('2909035800285', 'Invalid ID number'),
        ('2909035800585', 'Invalid ID number'),
    ),

 )

def test_citizen_check(test_input,excepted):
    assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086', 'Valid ID number'),
        ('2909035800085', 'Valid ID number'),
        ('2001014800076', 'Invalid ID number'),
        ('2909035800065', 'Invalid ID number'),
    ),
)


def test_race_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted


@pytest.mark.parametrize(
    'test_input, excepted',
    (
        ('2001014800086', 'Valid ID number'),
        ('2909035800085', 'Valid ID number'),
        ('2001014800087', 'Invalid ID number'),
        ('2909035800086', 'Invalid ID number'),
    ),

)

def test_checksum_check(test_input,excepted):
        assert is_id_number_valid(test_input) == excepted