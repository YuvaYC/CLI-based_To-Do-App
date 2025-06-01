work = []

while True:
    info = input("What do you want to do: ")

    if info == "e":
        print("Goodbye, Have a nice day!")
        break

    elif info == "add":
        while True:
            task = input("Enter your task (or 'e' to exit): ")

            if task == "e":
                break
            else:
                work.append(task)
                for i in work:
                    print("~", i)

    elif info == "remove":
        while True:
            task = input("Enter the task index number to remove (or 'e' to exit): ")

            if task == "e":
                break
            try:
                index = int(task)
                if 0 <= index < len(work):
                    del work[index]
                    for i in work:
                        print("~", i)
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif info == "l":
        for i in work:
            print("~", i)
            
    elif info == "m":
        while True:
            task = input('Enter the task index number which you need mark done: ')
            if task == 'e':
               break
            try:
                index = int(task)
                if 0 <= index < len(work):
                    work[index] = work[index] + ' - task done!'
                    new = work[index]
                    print(new)
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
               
    else:
        print("Unknown command. Try: add, remove, l (list), or e (exit).")
