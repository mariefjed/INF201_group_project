
def calculate_grade_stats(student_list, pass_threshold=50):
    """ creates a list of students who have passed the course and finds the total score and the avreage score"""
    total_score = 0
    passed_students = []

    for s in student_list:
        score = float(s['score'])
        if score >= pass_threshold:
            passed_students.append(s['name'])
        total_score += score
    avg = total_score / len(student_list) if len(student_list) > 0 else 0.0

    return {'average':avg,
            'passed':passed_students,
            'total_count':len(student_list)}

def print_summary(stats_dict, course_name = "Python 101"):
    """ prints a summary for the average  scores and students who have passed"""
    print("=== Summary for " + course_name + " ===")
    print("Average Score: " + str(stats_dict['average']))
    print("Passed Students: " + ", ".join(stats_dict['passed']))

data = [{'name':'Charlie','score':'85.5'},
        {'name':'River','score':'42.0'},
        {'name':'Jordan','score':'68.0'}]

res = calculate_grade_stats(data)
print_summary(res)