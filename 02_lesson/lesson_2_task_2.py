def is_year_leap():
    year = int(input())
    znachenie = 0
    if year % 4 == 0:
        znachenie = True
    else:
        znachenie = False
    print("год", year, ":", znachenie)

is_year_leap()