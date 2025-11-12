def compute_area_of_sphere(radius):
	pi = 3.14
	area = pi * radius * radius * 4
	return area

radius1 = 30
area1 = compute_area_of_circle(radius1)
print(f"The area of sphere with radius {radius1} is: {area1}")

radius2 = 40
area2 = compute_area_of_circle(radius2)
print(f"The area of sphere with radius {radius2} is: {area2}")
