import random
import math
import pandas as pd

#########-------------KNOWN ISSUES-------------------############
#1. Only one option for splits at the moment
#2. No option for how long you want to spend in the gym
#3. generate_routine function just chooses 3 compounds movements and 2 accessory movements right now

#User choices
workout_days_per_week = 5
time_per_workout = 60 #Time in minutes, assume 2.5 minutes per set (not used as of 2023-02-05)
fitness_goal = 2 #1 = strength, 2 = body building, 3 = lean/endurance
user_experience = 3 #1 = beginner, 2 = intermediate, 3 = advanced
split_selection = 1 #Don't have options. Will make #1 be legs, shoulders, back, chest, arms.

#Given a muscle group, generate a workout plan for that day
def generate_routine(muscle_group):
    #Import data for excercises
    df = pd.read_excel(r'Exercise_List.xlsx')
    #Load first column (muscle group)
    column = df.iloc[:, 0].values
    
    #Lists to store all exercises that match muscle group, split into compound and accessory movements
    t_list_strength = []
    t_list_acc = []

    #If the muscle group is arms, need to search for BICEP and TRICEP and return before
    #the next for loop is reached. See next loop for comments
    if muscle_group == "ARMS":
        t_list_tricep = []
        t_list_bicep = []
        for index, value in enumerate(column):
            if "TRICEP" in str(value).upper():
                t_list_tricep.append(df.iloc[index,1]) 
            elif "BICEP" in str(value).upper():
                t_list_bicep.append(df.iloc[index,1])
        tricep_list = random.sample(t_list_tricep,3)
        bicep_list = random.sample(t_list_bicep, 3)
        return [item for pair in zip(tricep_list, bicep_list) for item in pair]

    #Loop through the muscle group column and store exercises (2nd column)
    #that match the muscle_group key
    for index, value in enumerate(column):
        if muscle_group in str(value).upper():
            if "STRENGTH" in str(df.iloc[index,7]).upper():
                t_list_strength.append(df.iloc[index,1])
            else:
                t_list_acc.append(df.iloc[index,1])
    str_list = random.sample(t_list_strength, 3) #Choose 3 random compound movements
    acc_list = random.sample(t_list_acc, 2) #Choose 2 random accessory movements
     
    #return the compound and accessory movements lists combined
    return str_list + acc_list
    

def generate_rep_scheme(t_list):
    #Find the number of sets assuming 2.5 minutes per set
    #number_of_sets = math.floor(time_per_workout/2.5)

    #Set the minimum or maximum number of reps given the fitness goal
    if fitness_goal == 1:    
        rep_min, rep_max = 3,5
    elif fitness_goal == 2:
        rep_min, rep_max = 8,12
    elif fitness_goal == 3:
        rep_min, rep_max = 15,20
    #Set minimum or maximum number of sets given the fitness experience
    if user_experience == 1:    
        set_min, set_max = 2,3
    elif user_experience == 2:
        set_min, set_max = 3,4
    elif user_experience == 3:
        set_min, set_max = 4,5

    #Choose how many sets for each exercise
    sets = [random.randint(set_min,set_max) for value in t_list]
    #If rep range is 8-12, prevent odd numbers
    if fitness_goal == 2:
        reps = [random.randrange(rep_min,rep_max,2) for value in t_list]
    else:
        reps = [random.randint(rep_min,rep_max) for value in t_list]
    for i in range(len(t_list)):
        suffix = f" {sets[i]}x{reps[i]}"
        t_list[i] += suffix
    return t_list

#-------------------MAIN-----------------
#legs, shoulders, back, chest, arms.
if split_selection == 1:
    split_list = ["LEGS", "SHOULDERS", "BACK", "CHEST", "ARMS"]

for value in split_list:
    daily_workout = generate_routine(value)
    daily_workout = generate_rep_scheme(daily_workout)
    print(daily_workout)
