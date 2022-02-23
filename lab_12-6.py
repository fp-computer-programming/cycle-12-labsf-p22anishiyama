# Author: ATN 2/23/22

grades = {
    'End S1 Labs': 100, 'Start S2 Labs': 100, 'Mid-year Project Proposal': 100, 'Cycle 10 Practice Quiz': 100,
    'Cycle 10 Quiz': 100
    }

print(grades.items())

for i, v in grades.items():
    if v > 70:
        print("{0}: {1}%".format(i, v))

for i, v in grades.items():
    if v < 50:
        print("{0}: {1}%".format(i, v))
    else:
        print("Grade not below 50%")