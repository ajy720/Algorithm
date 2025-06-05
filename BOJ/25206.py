scoreTable = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}


if __name__ == "__main__":
    totalPoint, totalScore = 0.0, 0.0
    for _ in " " * 20:
        _, point, score = input().split()

        if score != "P":
            totalPoint += float(point)
            totalScore += scoreTable.get(score) * float(point)

    print(totalScore / totalPoint)
