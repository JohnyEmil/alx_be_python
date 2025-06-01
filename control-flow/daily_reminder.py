# Get task input from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Plan to complete it soon.")
            
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Schedule it this week.")
            
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task for today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")