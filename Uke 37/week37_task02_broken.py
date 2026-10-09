def process_class_scores(scores: list[float], pass_threshold: float = 50.0) -> float:
    """Removes failing scores and returns the average of passing students."""

    # Make new list with passed students
    passed_students=[]
    for score in scores:
        if score >= pass_threshold:
            passed_students.append(score)

    # Return the average of passing scores
    return sum(passed_students) / len(passed_students)

# Test dataset of scores
student_scores = [45, 30, 85, 90, 25, 10, 60]
avg = process_class_scores(student_scores)

# Print the average of passing scores (should be 78.33)
print(f"Average: {avg:.2f}")