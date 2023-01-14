class Spaceship:

    def __init__(self, canvas, x, y, photo, x_velocity, y_velocity, anchor):
        self.canvas = canvas
        self.image = canvas.create_image(x, y, image=photo, anchor=anchor)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[0] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.x_velocity = -self.x_velocity

        if coordinates[1] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.y_velocity = -self.y_velocity

        self.canvas.move(self.image, self.x_velocity, self.y_velocity)
