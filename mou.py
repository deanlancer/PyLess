grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
jm = sum(grades[0]) / len(grades[0])
bm = sum(grades[1]) / len(grades[1])
sm = sum(grades[2]) / len(grades[2])
km = sum(grades[3]) / len(grades[3])
am = sum(grades[4]) / len(grades[4])
# print(jm, bm, sm, km, am)
sts = sorted(list(students))
# avg_marks = {
# sts.__getitem__(0): jm,
# sts.__getitem__(1): bm,
# sts.__getitem__(2): sm,
# sts.__getitem__(3): km,
# sts.__getitem__(4): am,
# }
avg_marks = {
    sts[0]: jm,
    sts[1]: bm,
    sts[2]: sm,
    sts[3]: km,
    sts[4]: am,
}

print(avg_marks)

# aaa = input ("Write a name: ")
# if aaa == "Johnny" :
# print(jm)
