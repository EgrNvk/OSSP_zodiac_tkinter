from ossp_zodiac_mvc_model import ZodiacModel
from ossp_zodiac_mvc_view import ZodiacView
from ossp_zodiac_mvc_controller import ZodiacController

def main():
    model = ZodiacModel()
    view = ZodiacView()
    ZodiacController(model, view)
    view.mainloop()

if __name__ == "__main__":
    main()