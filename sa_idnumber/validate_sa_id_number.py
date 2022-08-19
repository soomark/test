from calendar import isleap

rsa_id_lenght = 13
gender_female_min = 0
gender_female_max= 4999
gender_male_min = 5000
gender_male_max= 9999
sa_citizen_digit = "0"
permanment_resident_digit = "1"
race_digit = "8"


def valid_id_length(id_number):
    if len(id_number) < rsa_id_lenght or len(id_number) > rsa_id_lenght:
        return False


def id_is_numeric(id_number):
    if not id_number.isdigit():
        return False


def valid_year(id_number):
    year = id_number[0:2]
    if not year.isdigit():
        return False


def valid_month(id_number):
    if str(id_number[2:4]) > "12" or str(id_number[2:4]) <= "00":
        return False


def valid_day(id_number):
    months_list = ["01", "03", "05", "07", "08", "10", "12"]
    year = id_number[0:2]
    month_in_year = id_number[2:4]
    day = id_number[4:6]
    for month in months_list:
        if str(month_in_year) in month and str(day) > "31":
            return False
        elif not str(month_in_year) in month and str(day) >= "31":
            return False
        elif isleap(int(year)) == True and str(month_in_year) == "02" and day > "29":
            return False
        elif isleap(int(year)) == False and str(month_in_year) == "02" and day >= "29":
            return False


def valid_gender(id_number):
    if (
        int(id_number[6:10]) > gender_female_min
        or int(id_number[6:10]) > gender_male_max):
        return False


def valid_citizen(id_number):
    if (
        str(id_number[10]) > sa_citizen_digit
        or str(id_number[10]) > permanment_resident_digit
    ):
        return False


def valid_race(id_number):
    if id_number[11] != race_digit:
        return False


def valid_checksum_digit(id_number):
    number = [int(digits) for digits in str(id_number)][::-1]
    if (
        sum(number[0::2]) + sum(sum(divmod(d * 2, 10)) for d in number[1::2])
    ) % 10 != 0:
        return False