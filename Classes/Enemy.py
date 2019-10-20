# Класс противника
class Enemy:
    def __init__(self, health, player, money, stage):
        # Создаю словарь для сохранения;
        self.stats = {
            "health": 100 * stage // 20,
            "money": money,
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

