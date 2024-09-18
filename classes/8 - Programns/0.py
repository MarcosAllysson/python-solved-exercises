class SimpleMath:

    def sum_number(self, number_one: int, number_two: int) -> int:
        if number_one is not None and number_two is not None:
            return number_one + number_two

        return 0

    def sub_number(self, number_one: int, number_two: int) -> int:
        if number_one is not None and number_two is not None:
            return number_one - number_two

        return 0

    def mul_number(self, number_one: int, number_two: int) -> float:
        if number_one is not None and number_two is not None:
            return number_one * number_two

        return 0

    def div_number(self, number_one: int, number_two: int) -> float:
        if number_one is not None and number_two is not None:
            try:
                return number_one / number_two
            except ZeroDivisionError:
                print('Can not divide by 1.')

        return 0

    def for_loop_between_range(self, initial_value: int, stop_value: int) -> int:
        sum_total_numbers: int = 0

        for i in range(initial_value, stop_value):
            sum_total_numbers += i

        return sum_total_numbers


simple_math = SimpleMath()
print(simple_math.for_loop_between_range(1, 10))
