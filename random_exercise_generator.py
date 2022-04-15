import random

#Input the number of students in your class on this day
students = list(range(int(input('Number of students? '))))

#Input the number of exercises 
exercises = list(range(int(input('Number of exercises? '))))

sample_size = exercises[-1] + 1

def randomizer(students, exercises, sample_size):
    """This function is a teaching tool to be used in randomly assigning
students exercises to be worked on the board. For each exercise assigned
by the teacher, three students will be charged with presenting this assignment
in the following manner: The first set of students work the problem on the
board. The second set of students correct any mistakes made by the first
student. The third set of students explain to the class the solution to the
problem worked on the board. Some students may be shy about presenting (being
in the third set). For these students, I stipulate they be in the first set
of students every time. Further, some students may have been absent on days
the topic(s) was (were) discussed. Finally, some students may be absent on
the day presentations are expected. Prompting within this function has been
included to handle these situations."""
    
    #Account for absences either when learning the topic(s) or on presentation
    #day
    absences = []
    flag = True
    while flag:
        student_absence = input('Student number for that student '
                                    'who is/was absent: ')
        if not student_absence:
            flag = False
        else:
            absences.append(int(student_absence))
    
    #First set pulled from the total population, with special exceptions
    
    #Students who wish not to be in group three must be in group one
    num_of_shy = int(input('How many students will be left out of the '
                           'third set? '))
    shy_students = []
    shys = 0
    while shys < num_of_shy:
        shy_student = int(input('For the next shy student, enter their student '
                                'number: '))
        shy_students.append(shy_student)
        shys += 1
    #Student population after the absences have been removed
    remaining_students = []
    for those in students:
        if those not in absences and those not in shy_students:
            remaining_students.append(those)
    todays_population = shy_students + remaining_students
    
    student_sample = shy_students + random.sample(remaining_students, sample_size-num_of_shy)
            
    exercise_sample = random.sample(exercises, sample_size)

    mapping = {}
    for i in range(len(student_sample)):
        mapping[sorted(student_sample)[i]] = sorted(exercise_sample)[i]
    
    #Removing those pulled from the total population to create the remaining
        #population
    for j in student_sample:
        todays_population.remove(j)
    
    #Second set pulled from the remaining population after first round of
        #removals
    students_subset_1 = todays_population
    student_sample_subset_1 = random.sample(students_subset_1, sample_size)

    mapping_subset_1 = {}
    for k in range(len(student_sample_subset_1)):
        mapping_subset_1[sorted(student_sample_subset_1)[k]] = sorted(exercise_sample)[k]

    #Removing those pulled from the remaining population after the first round
        #of removals to create another, smaller remaining population
    for l in student_sample_subset_1:
        students_subset_1.remove(l)
    
    #Third set pulled from the remaining population after second round of
        #removals
    students_subset_2 = students_subset_1
    student_sample_subset_2 = random.sample(students_subset_2, sample_size)

    mapping_subset_2 = {}
    for m in range(len(student_sample_subset_2)):
        mapping_subset_2[sorted(student_sample_subset_2)[m]] = sorted(exercise_sample)[m]

    #Removing those pulled from the other, smaller remaining population after
        #the second round of removals to create a still smaller remaining
        #population, for the purposes of completion
    for n in student_sample_subset_2:
        students_subset_2.remove(n)
        
    return mapping, mapping_subset_1, mapping_subset_2, students_subset_2

set_1, set_2, set_3, remaining = randomizer(students, exercises, sample_size)
print(f'\n')
print('Here is the first set of students: ')
print(set_1)
print(f'\n')
print('Here is the second set of students: ')
print(set_2)
print(f'\n')
print('Here is the third set of students: ')
print(set_3)
print(f'\n')
print('These students are safe: ')
print(remaining)