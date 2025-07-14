# tool_quanlydanhsachcongviec.py
tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def main():
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
    
