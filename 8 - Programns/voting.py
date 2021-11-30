def voting(user_age: int) -> str:
    MIN_AGE: int = 18
    MAX_AGE: int = 65

    if user_age > 0:
        if user_age < MIN_AGE:
            return f'You dont have to vote yet! Wait {MIN_AGE - user_age} years.'
        elif user_age <= MAX_AGE:
            return 'You must vote this year!'
        return 'Your vote is optional.'

    return "Invalid age."


try:
    user_age = int(input('How old are you? '))
    print(voting(user_age))
except ValueError:
    print('Invalid digit!')
except Exception as err:
    print(f'Ops {err}!')
