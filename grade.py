def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade >= 38 and grade % 5 > 2:
            grade += 5 - grade % 5
        result.append(grade)
    return result


if __name__ == '__main__':
    grading_students_count = int(input().strip())
    grades = [int(input().strip()) for _ in range(grading_students_count)]
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))