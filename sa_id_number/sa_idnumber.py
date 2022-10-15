def is_length_correct(id_number):
    test_size = len(id_number)
    id_constant = 13
    if test_size != id_constant:
        return False
    else:
        return True  


def numbers_only_check(id_number):
    if id_number.isdigit() == False:  
        return False
    else:
        return True


def year_check(id_number):       
    if '00' < str(id_number[0:2]) > '99':
        return False
    else:
        return True


def month_check(id_number):
    if '01' > str(id_number[2:4]) < '12':
        return False
    else:
        return True


def day_check(id_number):
    check_year = int(id_number[0:2])
    check_month = int(id_number[2:4])
    check_day = int(id_number[4:6])

    if  check_month in ["01", "03", "05", "07", "08", "10", "12"]:
        max_days = 31
    elif check_month in ["04", "06", "09", "11"]:
        max_days = 30
    elif (check_year) % 4 == 0 and (check_year) % 100 != 0 or (check_year) % 400 == 0:
        max_days = 29
    else:
        max_days = 28

    if (check_day < 1 or check_day > max_days):
        return False
    else:
        return True        


def gender_check(id_number):
    #gender_input = id_number[6:-3]
    #if (gender_input.isdigit() == False or (0 < int(gender_input) > 9999)):
    gender_min_value = 0
    gender_max_value = 9999
    if int(id_number[6:10]) >= gender_min_value or int(id_number[6:10]) <= gender_max_value:
        return False
    else:
        return True


def citizen_check(id_number):
    if '1' < str(id_number[10]) > '0' :
        return False
    else:
        return True        


def race_check(id_number):
    if id_number[11] != '8':
        return False
    else:
        return True


def checksum_check(id_number):
    number = [int(digits) for digits in str(id_number)][::-1]
    if (
        sum(number[0::2]) + sum(sum(divmod(d * 2, 10)) for d in number[1::2])
    ) % 10 != 0:
        return False
    else:
        return True
    

def is_id_number_valid(sa_id_number):
    if not (is_length_correct(sa_id_number)):
        return 'Invalid ID number'  
    if not (numbers_only_check(sa_id_number)):
        return 'Invalid ID number'
    if not (year_check(sa_id_number)):
        return 'Invalid ID number'
    if not (month_check(sa_id_number)):
          return 'Invalid ID number'
    if not (day_check(sa_id_number)):
        return 'Invalid ID number'
    if not (gender_check(sa_id_number)):
        return 'Invalid ID number'
    if not (citizen_check(sa_id_number)):
        return 'Invalid ID number'
    if not (race_check(sa_id_number)):
        return 'Invalid ID number'
    if not (checksum_check(sa_id_number)):
        return 'Invalid ID number'
    else:
        return 'Valid ID number'
