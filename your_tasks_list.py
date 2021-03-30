#!/usr/bin/env Python3
from os import system


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
    "Participate in a folk-dance concert on tour",
    "Get a green belt in kyokushin"
    ]

# ######################

while True:
    
    # ######## interaction ######
    
    new_task = input( " Add task: \n" )

    if( new_task == "\n" ):
        break
    
    if new_task not in tasks:
        tasks.append( new_task)
    else:
        print( "This task already exists!" )
    
    # ######## interaction ######

    
    # ## print the tasks #######
    system( "clear" )

    print( "TODO list", len( tasks ), ":-)" )
    
    for i in range( len( tasks )):
        
        print( "\t", i + 1, ">", tasks[i] )

    # ## print the tasks #######















