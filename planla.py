incompleted_tasks = []
completed_tasks = []    

def addNewTask():
    task = input('Task : ')
    incompleted_tasks.append(task)
    print('Added to your list.')

def deleteTask():
    task = input('Task : ')
    incompleted_tasks.remove(task)
    completed_tasks.append(task)
    print('Deleted from your list') 


def plan():    
    print('1. Add new task\n2. Complete existing task\n3. All completed tasks\n4. All incompleted tasks')
    
    while True:
        choice = (input('Choose the action you want: '))

        if choice == '1':
            addNewTask()
            
        elif choice == '2':
            deleteTask()
                    
        elif choice == '3':
            print('All completed tasks:' )
            print(completed_tasks)   

        else:
            print('All incompleted tasks: ')
            print(incompleted_tasks)

plan()
