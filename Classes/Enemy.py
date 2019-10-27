# Класс противника
class Enemy:
    def __init__(self, player):
        self.boss = 5 if (player.stats["defiedEnemies"] % 3 == 0) else 1
        # Создаю словарь для сохранения;
        self.stats = {
            "maxHealth": (100 * player.stats["defiedEnemies"] / 5) * self.boss,
            "health": (100 * player.stats["defiedEnemies"] / 5) * self.boss,
            "money": (100 * player.stats["defiedEnemies"] / 2) * self.boss,
        }

        # Создаю указатель на объект игрока;
        self.player = player
        # Умер ли противник;
        self.dead = False
    
    # Функция нанесения урона;
    def AddDamage(self):
        # Уменьшаю кол-во здоровья;
        self.stats["health"] -= self.player.damage

        # Смотрю кол-во здоровья меньше нуля и противник не умер;
        if (self.stats["health"] <= 0 and not self.dead):
            # Добавляю деньги игроку;
            self.player.stats["money"] += self.stats["money"]
            # Убиваю противника;
            self.dead = True
            # Увеличиваю кол-во убитых противников;
            self.player.stats["defiedEnemies"] += 1
        print(self.stats["health"], self.player.stats["defiedEnemies"], self.boss)
    
    # Получаю проценты здоровья
    def GetDamageForUI(self):
        # Сколько здоровья в одном проценте
        maxHealth = self.stats["maxHealth"] / 100
        # Сколько процентов осталось
        health = self.stats["health"] / maxHealth
        return health

