from datetime import datetime
import pickle

DATA_FILE = "tasks.dat"

def load_tasks():
    try:
        with open(DATA_FILE, "rb") as f:
            tasks = pickle.load(f)
    except (FileNotFoundError, pickle.UnpicklingError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(tasks, f)

tasks = load_tasks()

def add_task():
    task = input("Введите завершенное дело: ")
    tasks.append((task, datetime.now()))
    print("Дело добавлено.")
    save_tasks(tasks)

def view_tasks(start_date=None, end_date=None):
    if start_date is None and end_date is None:
        print("Все завершенные дела:")
        for task, date in tasks:
            print(f"{date.date()} - {task}")
    else:
        print(f"Завершенные дела с {start_date.date()} по {end_date.date()}:")
        for task, date in tasks:
            if start_date <= date <= end_date:
                print(f"{date.date()} - {task}")
        if not any(start_date <= date <= end_date for _, date in tasks):
            print("За указанный период дел не найдено.")

while True:
    action = input("Выберите действие (1 - добавить дело, 2 - просмотреть дела, 3 - выйти): ")
    if action == "1":
        add_task()
    elif action == "2":
        view_option = input("Выберите опцию (1 - все дела, 2 - за период): ")
        if view_option == "1":
            view_tasks()
        elif view_option == "2":
            start_date = datetime.fromisoformat(input("Введите начальную дату в формате ГГГГ-ММ-ДД: "))
            end_date = datetime.fromisoformat(input("Введите конечную дату в формате ГГГГ-ММ-ДД: "))
            view_tasks(start_date, end_date)
        else:
            print("Неверный ввод.")
    elif action == "3":
        break
    else:
        print("Неверный ввод.")
