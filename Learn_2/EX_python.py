def get_box_area(width, length, height):
    box_area = width * length * height
    return box_area

box1 = get_box_area(4, 4, 2)
box2 = get_box_area(width=1, length=1, height=1)

print(box2)