# an alternative to using multiple 'elif' statements

def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case "tuesday":
            return False
        case "wed":
            return False
        case "thurs":
            return False
        case "fri":
            return False
        case "sat":
            return True
        case _:                   # for all others values
            return False

print(is_weekend("sunday"))

print(is_weekend("fri"))


def is_weekend_v2(day):
    match day:
        case "sunday"|"sat":
            return True
        case "monday"|"tues"|"wed"|"thurs"|"fri":
            return False
        case _:
            return False

print(is_weekend_v2("fri"))
print(is_weekend_v2("sat"))
print(is_weekend_v2("xxxx"))