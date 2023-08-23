# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    """Function checking if user can drive a car."""
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if print(police_check(19)):
    print("Yoy may pass.")
else:
    print("Pay a fine.")
