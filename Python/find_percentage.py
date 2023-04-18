# The provided code stub will read in a dictionary containing key/value pairs of
# name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2
# places after the decimal.
#
# Input Format:
# The first line contains the integer n, the number of students' records.
# The next n lines contain the names and marks obtained by a student, each value
# separated by a space. The final line contains query_name, the name of a student to query.
#
# Output Format:
# Print one line: The average of the marks obtained by the particular student
# correct to 2 decimal places.
#
# Sample Input 0:#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0:
# 56.00



# Import decimal
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


# Extract the values into a list: query_scores
query_scores = student_marks[query_name]
# Sum the scores in the list: scores_sum
scores_sum = sum(query_scores)
# Convert the floats to decimals and average the scores: avg_marks
avg_marks = Decimal(scores_sum/len(scores))
# Print the mean of the scores, correct to two decimals
print(round(avg_marks,2))