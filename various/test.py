from tkinter import *

order = 1  # input('Select Hilbert curve order: ')


canvas_dimensions = 512
line_length = 40

master = Tk()
w = Canvas(master,
           width=canvas_dimensions,
           height=canvas_dimensions)
w.pack()


def getHilbert(order: int):
    return [(0, 0), (0, 1), (1, 1), (1, 0)]


def addPadding(point: tuple, padding: int = 50):
    x = padding if point[0] == 0 else point[0]*padding

    return (padding if point[0] == 0 else point[0]*padding, padding if point[1] == 0 else point[1]*padding)

for point in map(addPadding, [(0,0), (1, 1)]):
    print(point)

# w.create_line( *( point for point in map(addPadding, [(0,0), (1, 1)]) ))
# w.create_line(*(point*line_length for point in getHilbert(order)), fill="#000")

# w.create_line(0, y, canvas_width, y, fill="#000000")


mainloop()
