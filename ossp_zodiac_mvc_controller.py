from ossp_zodiac_mvc_model import ZodiacModel

class ZodiacController:
    def __init__(self, model: ZodiacModel, view):
        self.model=model
        self.view=view
        self.view.set_on_calculate(self.on_click)

    def on_click(self):
        day=self.view.get_day()
        month=self.view.get_month()
        zodiac=self.model.zodiac_for(day,month)
        self.view.show_zodiac(zodiac)