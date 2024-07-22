def task():
    tasks=[] #empty list
    print("----Welcome to Binod Todo task management----")
    total_task=int(input("Enter how many task that you want to add Mr.Binod: ")) #for 5 times
    for i in range(1,total_task+1): #5+1
         task_name=input(f"Enter the task {i}:")
         tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
         operation=int(input("Enter\n1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT/STOP/"))
         if operation==1:
              add=input("Enter task you want to add:")
              tasks.append(add)
              print(f"Task {add} has been successfully added...")
         elif operation==2:
              updated_value=input("Enter the task name that you want to update:")
              if updated_value in tasks:
                   updated=input("Enter tne new update task:")
                   ind=tasks.index(updated_value) #2
                   tasks[ind]=updated
                   print(f"updated task {updated}")
         elif operation==3:
              delete_value=input("which task you want to delete:")
              if delete_value in tasks:
                   ind=tasks.index(delete_value)
                   del tasks[ind]
                   print(f"Task {delete_value} has been deleted")
         elif operation==4:
              print(f"Total tasks={tasks}")
         elif operation==5:
              print("Closing the program...")
              break
         else:
              ("invalid input task...")
task()
              
              

         
         
