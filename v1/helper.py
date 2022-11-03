import pandas
import turtle

x_coor = {}
y_coor = {}
counter = 0


def get_coor(x, y):
    global counter
    global x_coor
    global y_coor
    print(x, y)
    x_coor[counter] = str(x)
    y_coor[counter] = str(y)
    counter += 1


data = pandas.read_csv("list-african-countries.csv")
data_dict = data.to_dict()

data_dict["Xcoor"] = x_coor
data_dict["Ycoor"] = y_coor

myDataFrame = pandas.DataFrame(data_dict)

print(myDataFrame)

myDataFrame.to_csv("final-africa-list.csv")

turtle.onscreenclick(get_coor)
turtle.mainloop()
