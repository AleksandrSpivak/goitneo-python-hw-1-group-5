from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    congrats = {"Monday": '',
                 "Tuesday": '',
                 "Wednesday": '',
                 "Thursday": '',
                 "Friday": ''
    }

    today_is = datetime.now().date()
    day_of_week = today_is.weekday()
    next_monday = today_is + timedelta(7 - day_of_week)
    next_friday = next_monday + timedelta(4)
    saturday = next_monday - timedelta(2)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today_is.year)

        if (birthday_this_year < today_is) and ((today_is - birthday_this_year).days > 7):
            birthday_this_year = birthday.replace(year=today_is.year + 1)

        if birthday_this_year >= saturday and birthday_this_year <= next_friday:
            if birthday_this_year.weekday() in [0, 5, 6] :
                congrats["Monday"] = congrats["Monday"] + name + ', ' 
            if birthday_this_year.weekday() == 1:
                congrats["Tuesday"] = congrats["Tuesday"] + name + ', '
            if birthday_this_year.weekday() == 2:
                congrats["Wednesday"] = congrats["Wednesday"] + name +', '
            if birthday_this_year.weekday() == 3:
                congrats["Thursday"] = congrats["Thursday"] + name + ', '     
            if birthday_this_year.weekday() == 4:
                congrats["Friday"] = congrats["Friday"] + name + ', '    
 
    print(f'Monday: {congrats["Monday"][:-2]}\nTuesday: {congrats["Tuesday"][:-2]}\nWednesday: {congrats["Wednesday"][:-2]}\nThursday: {congrats["Thursday"][:-2]}\nFriday: {congrats["Friday"][:-2]}')

    return


def main():
    notepad = [[],
                [
                {"name": "E Eeeee", "birthday": datetime(1999, 10, 9)},
                {"name": "F Fffff", "birthday": datetime(1999, 10, 12)},
                {"name": "G Ggggg", "birthday": datetime(1999, 10, 14)},
                {"name": "H Hhhhh", "birthday": datetime(1999, 10, 16)},
                {"name": "I Iiiii", "birthday": datetime(1999, 10, 20)},
                {"name": "J Jjjjj", "birthday": datetime(1999, 10, 22)},
                ],
                [
                {"name": "A Aaaaa", "birthday": datetime(1999, 12, 30)},
                {"name": "B Bbbbb", "birthday": datetime(1999, 1, 1)},
                {"name": "C Ccccc", "birthday": datetime(1999, 1, 2)},
                {"name": "D Ddddd", "birthday": datetime(1999, 1, 4)},
                ],
    ]

    for user in notepad:
        get_birthdays_per_week(user)


if __name__ == '__main__':
    main()