# ***
# ***
# ***
def draw_rectangle(width, height,shape):
    for j in range(height):
        for i in range(width):
            print("*", end=shape)
        print()

draw_rectangle(5, 10, "🌻")
draw_rectangle(5, 10, "❤️")
