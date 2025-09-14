import os
import json

class Team:
    def __init__(self, name, results, country, league, wins, coach):
        self.name = name
        self.results = results
        self.country = country
        self.league = league
        self.wins = wins
        self.coach = coach

    def __str__(self):
        return f"Команда: {self.name} ({self.country}, {self.league}), тренер: {self.coach}, перемог: {self.wins}"

    def get_role_info(self):
        return f"Забиті м’ячі у матчах: {self.results}"

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "results": self.results,
            "country": self.country,
            "league": self.league,
            "wins": self.wins,
            "coach": self.coach
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["results"],
            data["country"],
            data["league"],
            data["wins"],
            data["coach"]
        )

class FootballTeam(Team):
    def get_role_info(self):
        return f"Футбольна команда з {self.country}, тренер: {self.coach}"

class BasketballTeam(Team):
    def get_role_info(self):
        return f"Баскетбольна команда {self.name}, ліга: {self.league}"

class Database:
    def __init__(self, filename="teams.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, filename)
        self.teams = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.teams], f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.teams = []
                for t in data:
                    if t["type"] == "FootballTeam":
                        self.teams.append(FootballTeam.from_dict(t))
                    elif t["type"] == "BasketballTeam":
                        self.teams.append(BasketballTeam.from_dict(t))
                    else:
                        self.teams.append(Team.from_dict(t))
        except FileNotFoundError:
            self.teams = []

    def show_all(self):
        if not self.teams:
            print("Список команд порожній.")
            return
        for team in self.teams:
            print(team)
            print("\t", team.get_role_info())


db = Database()

t1 = FootballTeam("Динамо Київ", [2, 1, 3, 0], "Україна", "УПЛ", 15, "Шовковський Олександр")
t2 = BasketballTeam("Лейкерс", [102, 98, 110], "США", "NBA", 25, "Дарвін Хем")
t3 = Team("Барселона", [3, 4, 2, 1], "Іспанія", "Ла Ліга", 20, "Хансі Флік")
t4 = Team("Ліверпуль", [2, 4, 3, 1], "Англія", "АПЛ", 17, "Арне Слот")

db.add_team(t1)
db.add_team(t2)
db.add_team(t3)
db.add_team(t4)

db.save_to_file()

db2 = Database()
db2.load_from_file()

db2.show_all()
