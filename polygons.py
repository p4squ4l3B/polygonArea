# polygons.py

# Allows the user to click on a number of points to define a polygon.
# The total area is then calculated.
# The polygon should be drawn in a clockwise manner.

from graphics import *

WIN_WIDTH = 900
WIN_HEIGHT = 600

# Uses a well known algorithm to calculate the area.
def calculateArea(vertices, numVertices):
    area = 0
    j = numVertices - 1

    for i in range(numVertices):
        area = area + (vertices[j].getX() + vertices[i].getX()) * (vertices[j].getY() - vertices[i].getY())
        j = i

    return int(abs(area / 2))

def main():
    # Create window object
    win = GraphWin("Polygons", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("white")

    # Running keeps track of the whole program, while done tracks only the drawing-calculation loop.
    done = False
    running = True

    # Creates rectangle object for "done" button
    doneButtonWidth = 80
    doneButtonHeight = 30
    doneButtonX = (WIN_WIDTH / 2) - (doneButtonWidth / 2)
    doneButtonY = WIN_HEIGHT - 10
    doneButton = Rectangle(Point(doneButtonX, doneButtonY), Point(doneButtonX + doneButtonWidth, doneButtonY - doneButtonHeight))
    doneButton.setFill("white")
    doneButton.draw(win)

    # Creates text object for "done" button
    doneButtonText = Text(Point(WIN_WIDTH / 2, doneButtonY - (doneButtonHeight / 2)), "Done")
    doneButtonText.draw(win)

    # Declare the polygonVertices list and numVertices variable
    polygonVertices = []
    numVertices = 0
    lines = []
    numLines = 0

    # Define and draw instructions message
    message = Text(Point(WIN_WIDTH / 2, 15), "Click on the screen to define vertices and press done to close polygon.")
    message.draw(win)

    # Main program loop
    while (running):
        # Loop running before clicking "done button"
        while (not done):
            currentPoint = win.getMouse()

            # Check if "done" button has been clicked
            if currentPoint.getX() > doneButtonX and currentPoint.getX() < (doneButtonX + doneButtonWidth):
                if currentPoint.getY() > (doneButtonY - doneButtonHeight) and currentPoint.getY() < doneButtonY:
                    # Draw polygon and break out of drawing loop is enough vertices were provided
                    if numVertices >= 3:
                        numLines += 1
                        lines.append(Line(polygonVertices[0], polygonVertices[numVertices - 1]))
                        lines[numLines - 1].draw(win)

                        pol = Polygon(polygonVertices)
                        pol.setFill("red")
                        pol.draw(win)

                        polygonArea = calculateArea(polygonVertices, len(polygonVertices))
                        message.undraw()
                        message = Text(Point(WIN_WIDTH / 2, 15), "The area is: " + str(polygonArea) + ".")
                        message.draw(win)

                        done = True
                        break
                    # Display message is not enough vertices were provided and continue to next iteration
                    else:
                        message.undraw()
                        message = Text(Point(WIN_WIDTH / 2, 15), "A polygon is made from at least tree points.")
                        message.draw(win)
                        continue

            # If a point on the screen was clicked, draw a point on it
            if not done:
                polygonVertices.append(currentPoint)
                numVertices += 1
                currentPoint.draw(win)

                # If you have more than 2 points, join the current and the previous in a line
                if numVertices >= 2:
                    numLines += 1
                    lines.append(Line(polygonVertices[numVertices - 2], polygonVertices[numVertices - 1]))
                    lines[numLines - 1].draw(win)

        # Changes the "done" button for an "again" button to draw a new polygon
        doneButtonText.undraw()
        doneButtonText = Text(Point(WIN_WIDTH / 2, doneButtonY - (doneButtonHeight / 2)), "Again")
        doneButtonText.draw(win)

        # Check if "done"/"again" button was pressed
        currentPoint = win.getMouse()
        if currentPoint.getX() > doneButtonX and currentPoint.getX() < (doneButtonX + doneButtonWidth):
            if currentPoint.getY() > (doneButtonY - doneButtonHeight) and currentPoint.getY() < doneButtonY:
                done = False

                # Go back to instructions message
                message.undraw()
                message = Text(Point(WIN_WIDTH / 2, 15), "Click on the screen to define vertices and press done to close polygon.")
                message.draw(win)

                # Go back to "done" button
                doneButtonText.undraw()
                doneButtonText = Text(Point(WIN_WIDTH / 2, doneButtonY - (doneButtonHeight / 2)), "Done")
                doneButtonText.draw(win)

                # Undraw polygon and empty the vertices list
                pol.undraw()

                for point in polygonVertices:
                    point.undraw()

                for line in lines:
                    line.undraw()

                lines = []
                numLines = 0
                polygonVertices = []
                numVertices = 0
main()
