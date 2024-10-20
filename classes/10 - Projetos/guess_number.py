import random
from time import sleep


start_number: int = 1
end_number: int = 10


def initial_game_message() -> None:
    print(
        f"Bem-vindo(a) ao jogo onde eu vou escolher um número aleatório entre {start_number} e {end_number} e você vai tentar adivinhar qual é!!"
    )


def get_random_number() -> int:
    print(
        f"\nTô pensando num número aleatório entre {start_number} e {end_number} aqui..."
    )

    sleep(3)
    random_number: int = random.randint(start_number, end_number)

    print("\nOk. Escolhi!")

    return random_number


def get_random_number_from_user() -> int:
    while True:
        try:
            user_number: int
            user_number = int(
                input(
                    f"\nAgora é sua vez: digite um número entre {start_number} e {end_number}: "
                )
            )
        except Exception as err:
            print(
                f"\nOps, tem que ser um número entre {start_number} e {end_number}... \nVamos de novo "
            )
        else:
            if user_number >= start_number and user_number <= end_number:
                print(f"\nOk, sua escolha foi: {user_number}.")
                return user_number

            continue


def get_random_number_from_user_again() -> int:
    while True:
        try:
            user_number: int
            user_number = int(
                input(
                    f"\nERROOOOOOOOOOU. \nEscolha outro número entre {start_number} e {end_number}: "
                )
            )
        except Exception as err:
            print(
                f"\nOps, tem que ser um número entre {start_number} e {end_number}... \nVamos de novo "
            )
        else:
            print(f"\nAgora tu escolheu: {user_number}.")
            return user_number


def check_number(random_number: int, user_number: int) -> bool:
    if random_number == user_number:
        print(
            f"\n BOAAA!!! EU ESCOLHI O NÚMERO: {random_number}. \n ACERTOU MISERÁVI :D \n ----FIM----"
        )
        return True

    return False


def start_game() -> None:
    initial_game_message()
    robot_number: int = get_random_number()
    user_number: int = get_random_number_from_user()

    while True:
        if check_number(robot_number, user_number):
            break

        else:
            user_other_number: int = get_random_number_from_user_again()

            if check_number(robot_number, user_other_number):
                break

            else:
                continue
