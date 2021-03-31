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
    "Become a good programmer-real haсker",
    "Participate in a folk-dance concert on tour",
    "Get a green belt in kyokushin",
    ]

# ######################

# ##### func  ##########

def view_menu(): 
 system( "clear" )
 print()
 print( "Info how to use TODO list" )
 print()
 print( "***************************************" )
 print()
 print( "Enter 1 to add a new task in TODO list" )
 print( "Enter 2 to show TODO list" )
 print( "Enter 3 to remove one task in TODO list" )
 print( "Enter 4 to clear TODO list" )
 print( "Enter 0 to EXIT" )
 print()


def view_tasks():
 system( "clear" )
 print( "Your TODO list:", len( tasks ), ":-)" )
 for i in range( len( tasks )):
  print( "\t", i + 1, ">", tasks[i] )


 ########################


view_menu()

## A LOT OF CODE ###

while True:
    
    # ######## interaction ######
    
 new_task = input( " Enter any number from the menu: \n" )

 if( new_task == "0" ):
  break 

 elif( new_task == "1" ):
  view_tasks()
  new_task = input( " Add new task: \n" )
  
  if new_task not in tasks:
   tasks.append( new_task)
   view_tasks()

  else:
    print( "This task already exists!" )
    
 elif( new_task == "2" ):
  view_tasks()

 elif( new_task == "3" ):
  
  view_tasks()

  i = int( input( " What task do you want to remove: \n" ))
  i -= 1  
  
  if( 0 <= i <= len( tasks )):
   
   print( "Are you shue you want to remove task ", i + 1, tasks[i], "?" )
   verif = input( "\nEnter Y or N\n" )
  
   if( verif == "Y" ):
    del tasks[i]
    view_tasks()

   else:
    print( "You haven't made any changes in TODO list.\n" )
    continue
  else:
   print( "Enter a number from the range: 1 to ", len(tasks))
# need to think about other solution ###

# ### -4- #### 

 elif( new_task == "4" ):
  print( "Are you shue you want to clear TODO list?" )
  verif = input( "\nEnter Y or N\n" )
  
  if( verif == "Y" ):
   tasks.clear()
   print("Your TODO list is empty.\n")
   view_tasks()
  else:
   print( "You haven't made any changes in TODO list.\n" )
   continue
    
   # ######## interaction ######

