#!/usr/bin/env Python3



# ########### DATA #########

tasks = [
    "To raise a child who are genuinely nice human",
    "Keep a family strong and friendly",
    "Learn Python",
    "Learn English",
    "Learn C",
    "Learn computer architecture",
    "Learn Assembler",
    "Become a good programmer-real haсker"
    "Learn folk-dance",
    "Learn kyokushin"
    ]

# ######################

while True:
    
    # ######## interaction ######
    
    new_task = input( " Add task: " )
    
    if new_task not in tasks:
        tasks.append( new_task)
    else:
        print( "This task already exists!" )
    
    # ######## interaction ######

    # ## print the tasks #######

    print
