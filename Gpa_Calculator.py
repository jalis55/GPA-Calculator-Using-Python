# calculate gpa
def get_gpa(avg_score):
    if avg_score>=91:
        return 'A+'
    elif avg_score>=81:
        return 'A'
    elif avg_score>=71:
        return 'B'
    elif avg_score>=61:
        return 'C'
    elif avg_score>=41:
        return 'D'
    else:
        return 'F'
    

#Subject list
subject_list=['Bangla','English','Math','Science']

# save total score
score=0

for subject in subject_list:
    print(f'Enter marks of {subject}:',end="")
    marks=float(input())
    # storing marks
    score +=marks

# calculate average score 
avg_score=score/len(subject_list)

# store grade
result=get_gpa(avg_score)

print(f'Your grade is:{result}')


