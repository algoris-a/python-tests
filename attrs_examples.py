# Source:
# https://www.attrs.org/en/stable/overview.html

from attrs import asdict, define, make_class, Factory

@define
class SomeClass:
    a_number: int = 42
    list_of_numbers: list[int] = Factory(list)

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number

sc = SomeClass(a_number=1, list_of_numbers=[1, 2, 3])
print(asdict(sc))

