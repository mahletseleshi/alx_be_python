task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", task, "is a high priority task that requires immediate attention today!")
        else:
            print("Reminder:", task, "is a high priority task.")
    
    case "medium":
        if time_bound == "yes":
            print("Reminder:", task, "is a medium priority task that needs to be done soon.")
        else:
            print("Reminder:", task, "is a medium priority task.")
    
    case "low":
        if time_bound == "yes":
            print("Reminder:", task, "is a low priority task. Consider completing it when you have free time.")
        else:
            print("Reminder:", task, "is a low priority task.")
    
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
