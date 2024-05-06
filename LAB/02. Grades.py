grade = float(input())


def passing(_grade: float) -> str:
    if 2.00 <= _grade < 3.00:
        return 'Fail'
    elif 3.00 <= _grade < 3.50:
        return 'Poor'
    elif 3.50 <= _grade < 4.50:
        return 'Good'
    elif 4.50 <= _grade < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


print(passing(grade))