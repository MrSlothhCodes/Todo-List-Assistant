import pandas as pd
from datetime import date as dt

print("To Do List")

a = True
today =  dt.today()
fd = dt.strftime(today,'%d-%m-%Y')

while a == True:
    #variables
    data = pd.read_csv('GFG.csv')
    tasks = data['Tasks'].tolist()
    complete = data['Completed'].tolist()
    dat = data['Date'].tolist()
    lenT = len(tasks)
    lenC = len(complete)
    
    #null container remover
    for k in range(-lenC,0):
        if complete[k] == ".":
            complete.pop(k)

    for j in range(-lenT,0):
        if tasks[j] == ".":
            tasks.pop(k)

    #print list
    for n in range(len(tasks)):
        if dat[n]==fd :
            print(n+1,tasks[n])
        else:
            print(n+1,tasks[n],"Due Date :",dat[n])  
    print("\n1. Add Task")
    print("2. Mark as Complete")
    print("3. Exit")
    sel = int(input("\nSelect : "))

    #entry
    if (sel == 1):
        task = input("Enter The  Task : ")
        tasks.append(task)
        dat.append(today)
        print(task, "added")
        #equilizer
        for i in range(len(tasks)):
            if len(complete) > len(tasks):
                tasks.append(".")
            elif len(complete) < len(tasks):
                complete.append(".")
            elif len(dat) < len(tasks):
                dat.append(".")    
        
        tdict = {'Tasks': tasks, 'Completed': complete , 'Date':dat}
        df = pd.DataFrame(tdict)
        df.to_csv('GFG.csv')

    #task Complted 
    if (sel == 2):
        b = True
        dtask = int(input("\n Enter Task Number[To Mark as Complete] \n press [0] For Completed Tasks List :"))
        if(dtask==0):
            print("\n Completed Tasks")
            for j in range(len(complete)):
                print(j+1, complete[j])
                
        else:
            comtask = tasks.pop(dtask-1)
            dat.pop(dtask-1)
            print(comtask, "Completed")
            print(tasks, ": Are/is Remaining Task")
            complete.append(comtask)
            #equilizer
            for i in range(len(complete)):
                if len(complete) > len(tasks):
                    tasks.append(".")
                elif len(complete) < len(tasks):
                    complete.append(".")
                elif len(dat) < len(tasks):
                    dat.append(".")    
                
            tdict = {'Tasks': tasks, "Completed": complete ,"Date":dat}
            df = pd.DataFrame(tdict)
            df.to_csv('GFG.csv')
    
    #exit
    if sel == 3:
        a=False