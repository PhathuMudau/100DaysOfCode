import turtle
import pandas as pd


screen = turtle.Screen()
screen.setup(width=800, height=700)
screen.title("African Countries Game")
image = "africa-blank-colorful.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("african_countries.csv")

total = len(data.country)

country_list = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < len(data.country):

    answer_country = screen.textinput(title=f"{len(guessed_countries)}/{total} Countries Correct",
                                      prompt="Guess a country? Type 'Exit' when finished.")

    if answer_country == "Exit":
        missing_countries = [country for country in country_list if country not in guessed_countries]
        new_data = pd.DataFrame(missing_countries)
        new_data.to_csv("Countries_to_Learn.csv")
        break

    if answer_country is None:
        pass
    elif answer_country.title() in country_list:
        answer = answer_country.title()
        if answer_country not in guessed_countries:
            guessed_countries.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        country_data = data[data.country == answer]
        t.goto(int(country_data.x.iloc[0]), int(country_data.y.iloc[0]))
        t.write(answer)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
