import math
def gradingStudent(grades):

    rounded = []

    for grade in grades:
        floor_digit = math.floor(grade / 5)
        next_mutliple = (5 * (1 + floor_digit))

        difference = next_mutliple - grade

        # if grade < 37:
        #     rounded.append(grade)

        if difference < 3:
            if grade < 37:
                rounded.append(grade)
            rounded.append(next_mutliple)

        if difference >= 3:
            rounded.append(grade)

    return rounded

grades = [2, 3, 56, 34, 78, 90]

data = gradingStudent(grades)
print(data)