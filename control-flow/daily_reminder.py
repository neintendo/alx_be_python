#!/usr/bin/python3

"""
Daily Reminder: a script that asks the user for a single task, its priority level, and if it is time-sensitive.
                The program will then provide a customized reminder for that task, demonstrating control flow
                and loops without relying on data structures to store multiple tasks.
"""

description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
priority_check = False

match priority:
    case "high":
        priority_check = True
    case "medium":
        priority_check = True
    case "low":
        priority_check = True
    case _:
        print("ERROR: priority should be high/medium/low")
        quit()
        
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    print("Reminder: '{0}' is a {1} priority task that requires immediate attention today!".format(description, priority))
    quit()
elif time_bound == "no":
    print("Note: '{0}' is a {1} priority task. Consider completing it when you have free time.".format(description, priority))
    quit()
else:
    print("ERROR: enter yes or no")
    quit()
