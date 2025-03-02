from answer.src.tasker import Task_Manager,Task
from answer.src.database import init_db, save_db, load_db

tm = Task_Manager
manager = Task_Manager()  

def main_menu():
    init_db()  
    load_db(manager)  

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Изменить статус задачи")
        print("4. Удалить задачу")
        print("5. Найти задачи по ключевому слову")
        print("6. Отфильтровать задачи по статусу")
        print("7. Сохранить и выйти")

        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите число от 1 до 7.")
            continue

        if choice == 1:
            add_task(manager)
        elif choice == 2:
            show_tasks(manager)
        elif choice == 3:
            update_task_status(manager)
        elif choice == 4:
            delete_task(manager)
        elif choice == 5:
            find_tasks(manager)
        elif choice == 6:
            filter_tasks(manager)
        elif choice == 7:
            save_and_exit(manager)
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def add_task(manager):
    title = input("Введите название задачи: ").strip()
    description = input("Введите описание задачи: ").strip()
    if title and description:
        manager.create(Task(title, description))
        print("Задача успешно добавлена!")
    else:
        print("Название и описание задачи не могут быть пустыми.")

def show_tasks(manager):
    tasks = manager.read()
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i+1}. Название: {task.title}, Описание: {task.description}, Статус: {task.status}")
    else:
        print("У вас пока нет задач.")

def update_task_status(manager):
    task_id = input("Введите ID задачи: ").strip()
    new_status = input("Введите новый статус ('Не выполнено', 'В процессе', 'Выполнено'): ").strip()
    if manager.update(int(task_id), new_status):
        print("Статус задачи успешно обновлён!")
    else:
        print("Задача с указанным ID не найдена.")

def delete_task(manager):
    task_id = input("Введите ID задачи: ").strip()
    if manager.delete(int(task_id)):
        print("Задача успешно удалена!")
    else:
        print("Задача с указанным ID не найдена.")

def find_tasks(manager):
    keyword = input("Введите ключевое слово для поиска: ").strip().lower()
    tasks = manager.search(keyword)
    if tasks:
        for task in tasks:
            print(f"Название: {task.title}, Описание: {task.description}, Статус: {task.status}")
    else:
        print("По вашему запросу ничего не найдено.")

def filter_tasks(manager):
    status = input("Введите статус для фильтрации ('Не выполнено', 'В процессе', 'Выполнено'): ").strip()
    tasks = manager.filter(status)
    if tasks:
        for task in tasks:
            print(f"Название: {task.title}, Описание: {task.description}, Статус: {task.status}")
    else:
        print("Задач с указанным статусом не найдено.")

def save_and_exit(manager):
    save_db(manager)
    print("Все задачи были сохранены. Программа завершила работу.")
    exit(0)

if __name__ == "__main__":
    main_menu()