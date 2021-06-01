class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    @staticmethod
    def is_player(player, players):
        return player in players

    @staticmethod
    def get_player(player_name, players):
        result = [player for player in players if player.name ==player_name]
        if result:
            return result[0]

    def add_player(self, player):
        if self.is_player(player, self.players):
            return f"Player {player.name} has already joined"

        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        current_player = self.get_player(player_name, self.players)
        if not current_player:
            return f"Player {player_name} not found"

        self.players.remove(current_player)
        return current_player

import unittest

from project_football_team_generator.team import Team


class Tests(unittest.TestCase):
    def test_player_init(self):
        p = Player("Pall", 3, 3, 3, 3, 3)
        self.assertEqual(p.name, "Pall")
        self.assertEqual(p.endurance, 3)
        self.assertEqual(p.sprint, 3)
        self.assertEqual(p.passing, 3)
        self.assertEqual(p.dribble, 3)
        self.assertEqual(p.shooting, 3)

    def test_player_str(self):
        p = Player("Pall", 3, 3, 3, 3, 3)
        result = str(p)
        expected = "Player: Pall\nEndurance: 3\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3\n"
        self.assertEqual(expected, result)

    def test_team_init(self):
        t = Team("Best", 10)
        self.assertEqual(t.name, "Best")
        self.assertEqual(t.rating, 10)
        self.assertEqual(len(t.players), 0)

    def test_team_add_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)

        self.assertEqual(t.add_player(p), "Player Pall joined team Best")

    def test_team_add_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)

        t.add_player(p)
        self.assertEqual(t.add_player(p), "Player Pall has already joined")

    def test_team_remove_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)
        t.add_player(p)
        exp = t.remove_player("Pall")
        self.assertEqual(exp, p)

    def test_team_remove_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)
        result = "Player Pall not found"
        exp = t.remove_player("Pall")
        self.assertEqual(exp, result)


if __name__ == "__main__":
    unittest.main()