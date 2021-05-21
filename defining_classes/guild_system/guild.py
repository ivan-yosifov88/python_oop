from guild_system.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: Player):
        current_player = [p for p in self.players if p.name == player_name]
        if not current_player:
            return f"Player {player_name} is not in the guild."
        self.players.remove(current_player[0])
        current_player[0].guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players = '\n'.join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n{players}"

