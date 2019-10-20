from Classes.Player import Player
from Classes.Enemy import Enemy

player = Player()
enemy = Enemy(100, player, 10000, 1)

player.Save()

print(f"Damage: {player.damage}; Money: {player.stats['money']}; Enemy health: {enemy.stats['health']}")

enemy.AddDamage()
player.BuyNewNotebook()
player.BuyNewNotebook()
player.BuyNewNotebook()

print(f"Damage: {player.damage}; Money: {player.stats['money']}; Enemy health: {enemy.stats['health']}")

enemy.AddDamage()

print(f"Damage: {player.damage}; Money: {player.stats['money']}; Enemy health: {enemy.stats['health']}")

enemy.AddDamage()

print(f"Damage: {player.damage}; Money: {player.stats['money']}; Enemy health: {enemy.stats['health']}")

player.Load()

print(f"Damage: {player.damage}; Money: {player.stats['money']}; Enemy health: {enemy.stats['health']}")

# "HZ_c-I"

