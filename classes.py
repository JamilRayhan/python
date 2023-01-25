def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    mx = numbers[0]
    for number in numbers:
        if number > mx:
            mx = number
    return  mx
