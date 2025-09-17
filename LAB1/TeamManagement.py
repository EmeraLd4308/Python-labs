teams = []

def create_team(name, results, country, league, wins, coach):
    return {
        "name": name,
        "results": results,
        "info": (country, league),
        "wins": wins,
        "coach": coach
    }

def input_team_data(existing_name=None):
    name = existing_name if existing_name else input("Введіть назву команди: ")
    results = list(map(int, input("Введіть результати матчів (забиті голи) через пробіл: ").split()))
    country = input("Введіть країну: ")
    league = input("Введіть лігу: ")
    wins = int(input("Введіть кількість перемог: "))
    coach = input("Введіть головного тренера: ")
    return name, results, country, league, wins, coach

def print_team(tid, team):
    print(f"ID: {tid}")
    print(f"Назва команди: {team['name']}")
    print(f"Результати матчів: {team['results']}")
    print(f"Країна/Ліга: {team['info']}")
    print(f"Кількість перемог: {team['wins']}")
    print(f"Головний тренер: {team['coach']}")
    print("-" * 40)

def add_team():
    name, results, country, league, wins, coach = input_team_data()
    team = create_team(name, results, country, league, wins, coach)
    teams.append(team)
    print(f"Команду {name} додано з ID: {len(teams)-1}\n")

def get_team(tid):
    if 0 <= tid < len(teams):
        return teams[tid]
    return None

def find_team(name_query):
    name_query = name_query.lower()
    results = [(i, t) for i, t in enumerate(teams) if name_query in t['name'].lower()]
    return results

def show_teams():
    if not teams:
        print("Список команд порожній.\n")
        return
    for i, team in enumerate(teams):
        print_team(i, team)
    print()

def edit_team():
    try:
        tid = int(input("Введіть ID команди для редагування: "))
    except ValueError:
        print("ID має бути числом.\n")
        return

    team = get_team(tid)
    if team:
        print(f"Редагуємо команду {team['name']}")
        name, results, country, league, wins, coach = input_team_data(existing_name=team['name'])
        teams[tid] = create_team(name, results, country, league, wins, coach)
        print("Дані команди оновлено!\n")
    else:
        print("Команду з таким ID не знайдено.\n")

def delete_team():
    try:
        tid = int(input("Введіть ID команди для видалення: "))
    except ValueError:
        print("ID має бути числом.\n")
        return

    if 0 <= tid < len(teams):
        deleted = teams.pop(tid)
        print(f"Команду {deleted['name']} видалено.\n")
    else:
        print("Команду з таким ID не знайдено.\n")

def search_by_id():
    try:
        tid = int(input("Введіть ID команди: "))
    except ValueError:
        print("ID має бути числом.\n")
        return

    team = get_team(tid)
    if team:
        print_team(tid, team)
    else:
        print("Команду з таким ID не знайдено.\n")

def search_by_name():
    name_query = input("Введіть назву команди для пошуку: ")
    results = find_team(name_query)
    if results:
        for tid, team in results:
            print_team(tid, team)
    else:
        print("Команду з такою назвою не знайдено.\n")

def statistics():
    if not teams:
        print("Список команд порожній.\n")
        return
    all_goals = [g for t in teams for g in t['results']]
    if all_goals:
        avg = sum(all_goals) / len(all_goals)
        print(f"Середня кількість забитих м’ячів: {avg:.2f}")
        print(f"Максимальна кількість м’ячів у матчі: {max(all_goals)}")
        print(f"Мінімальна кількість м’ячів у матчі: {min(all_goals)}")
        over3 = [g for g in all_goals if g >= 3]
        print(f"Кількість матчів з 3+ голами: {len(over3)}\n")
    else:
        print("Результатів матчів ще немає.\n")

def menu():
    while True:
        print("Меню")
        print("1. Додати команду")
        print("2. Показати всі команди")
        print("3. Пошук команди за ID")
        print("4. Пошук команди за назвою")
        print("5. Редагувати команду")
        print("6. Видалити команду")
        print("7. Статистика")
        print("8. Вихід")
        choice = input("Ваш вибір: ")

        options = {
            "1": add_team,
            "2": show_teams,
            "3": search_by_id,
            "4": search_by_name,
            "5": edit_team,
            "6": delete_team,
            "7": statistics
        }

        if choice in options:
            options[choice]()
        elif choice == "8":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")

menu()
