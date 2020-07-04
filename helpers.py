import datetime

# HELPER FUNCTIONS
# test_int
# Accepts single parameter of is_int
# is_int is tested as a vaild integer


def test_int(is_int):
    try:
        int(is_int)
        return True
    except ValueError:
        return False


# eval_user_yes
# Takes a user input and evaluates against is True, is "Yes", is "Y" or is "y".
# If found to be true, returns True, else returns False
def eval_user_yes(input):
    if input == True or input == "Yes" or input == "Y" or input == "y":
        return True
    else:
        return False


# get_datetime
# Return current datetime
def get_datetime():
    now = datetime.datetime.now()
    now_date_time = now.strftime("%H:%M  %m-%d-%Y")
    return now_date_time
