# Класс противника
class Enemy:
    def __init__(self, player):
        # Создаю словарь для сохранения;
        self.stats = {
            "maxHealth": 100 * player.stats["defiedEnemies"] / 5,
            "health": 100 * player.stats["defiedEnemies"] / 5,
            "money": 100 * player.stats["defiedEnemies"] / 2,
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
        print(self.stats["health"])
    
    # Получаю проценты здоровья
    def GetDamageForUI(self):
        # Сколько здоровья в одном проценте
        maxHealth = self.stats["maxHealth"] / 100
        # Сколько процентов осталось
        health = self.stats["health"] / maxHealth
        return health

