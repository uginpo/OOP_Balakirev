from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_name(cls, name):
        names = name.split()
        if len(names) != 2:
            return False
        else:
            for nam in names:
                if not set(nam) < set(cls.CHARS_FOR_NAME):
                    return False
            return True

    @staticmethod
    def check_card_number(number):
        numbers = number.split('-')
        if len(numbers) != 4:
            return False
        else:
            for num in numbers:
                if not set(num) < set(digits):
                    return False
            return True


print(CardCheck.check_card_number('4563-4392-0364-3502'))
print(CardCheck.check_name('VASYA PLITKIN'))
