work = []

while True:
	info = input("What do you want to do: ")
	
	if info == "e":
		print("Goodbye, Have a nice day!")
		break
	elif info == "add":
		while True:
			task = input("Enter your task: ")
			
			if task == "e":
				break
			else:
				added  = work.append(task)
				for i in work: print("~", i)
	elif info == "remove":
		while True:
			task = input("Enter the task index number: ")
			
			try:
				if task == "e":
					break
				else:
					work.remove(task)
					for i in work: print("~", i)
			except ValueError:
				print("Inavlid number or the task is already removed.")
	elif info == "l":
		for i in work: print("~", i)



#Interface: eth0, Type: ethernet, Module: r8169, Device Description: pci: Realtek semiconductor RT811181688411 PCI Express Gigabit Ethernet Controller


