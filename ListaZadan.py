tasks = []

def add_task():
    task = input("Podaj nazwe zadania: ")
    tasks.append(task)
    print ("Zadanie ",task,"dodane")

def show_tasks():
    if not tasks:
        print("Nie ma zadnych zadan na liscie")
    else:
        print("Lista zadan:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    show_tasks()
    try:
        task_numer = int(input("Wprowadz numer zadania do usuniecia: "))
        removed_task = tasks.pop(task_numer -1)
        print(f"Zadanie ",removed_task, "usuniete")
    except (IndexError, ValueError):
        print("Zly numer zadania")



                         
def main():
    while True:
        print("\nLista zadan:")
        print("1. Dodaj zadanie")
        print("2. Wyswietl zadania")
        print("3. Usun zadanie")
        print("4. Zakoncz program")

        choice = input("Wybierz opcje (cyfre): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Do widzenia!")
            break
        else:
            print("Zly numer. Sprobuj jeszcze raz")


if __name__ == "__main__":
    main()

            
