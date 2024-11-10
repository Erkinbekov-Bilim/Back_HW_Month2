from Geeks_M2.homework_two.hero import Hero, hero_action


class Archer(Hero):
    def __init__(self, name, health, arrows = 10):
        super().__init__(name, health)
        self.arrows = arrows

    def shoot_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} использует лук! Количество стрел: {self.arrows}"
        else:
            return f"У {self.name} закончились стрелы"

    def action(self):
        base_action = super().action()
        spell_result = self.shoot_arrow()
        return f"{base_action}{spell_result}"


archer = Archer("Robin", 80, 2)
hero_action(archer)