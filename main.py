import turtle
import pandas

# setting up screen
screen = turtle.Screen()
screen.title("African States Game")
image = "img/africa-map.gif"
screen.addshape(image)
screen.setup(487, 479)
turtle.shape(image)

data = pandas.read_csv("final-africa-list.csv")
all_countries = data.Country.to_list()

guessed_countries = []

while len(guessed_countries) < 55:
    answer_country = screen.textinput(
        title=f"{len(guessed_countries)}/55 Countries Correct",
        prompt="What's another country's name?").title()

    if answer_country == "Exit":
        break

    if answer_country in all_countries and answer_country not in guessed_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.Country == answer_country]
        t.goto(int(country_data.Xcoor), int(country_data.Ycoor))
        t.write(country_data.Country.item())

screen.exitonclick()
