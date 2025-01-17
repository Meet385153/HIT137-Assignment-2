import turtle

# Function to draw a tree recursively
def draw_tree(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    if branch_length < 5:  # When the branch length is too short, stop the recursion
        return
    
    # Set the branch color: Long branches are brown, short ones are green
        t.pensize(depth * 2)
    if depth <= 2:
        t.color("green")  # Leaves
    else:
        t.color("brown")  # Branches

    
    # Draw the current branch
    t.forward(branch_length)
    
    # Draw the left branches
    t.left(angle_left)
    draw_tree(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    
    # Backtrack and draw the right branches
    t.right(angle_left + angle_right)  # Turn to the right branches
    draw_tree(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    
    # Backtrack to the parent branch
    t.left(angle_right)
    t.backward(branch_length)

# Main function to setup turtle  and ask user for input
def main():
    # Create turtle screen and turtle object
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Set up the screen background
    screen.bgcolor("white")

    # Ask the user for input
    try:
        angle_left = float(input("Enter the left branch angle (in degrees): "))
        angle_right = float(input("Enter the right branch angle (in degrees): "))
        branch_length = float(input("Enter the starting branch length (in pixels): "))
        depth = int(input("Enter the recursion depth (only positive natural number): "))
        reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))
    except ValueError:
        print("Invalid input! Please enter valid numerical values.")
        return
    
    # Basic input validation
    if not (0 < reduction_factor < 1):
        print("The reduction factor should be a number between 0 and 1.")
        return
    if depth <= 0:
        print("Recursion depth should be a positive integer.")
        return
    if branch_length <= 0:
        print("Starting branch length should be a positive number.")
        return

    # Setup turtle
    t.left(90)  # Start with the turtle pointing upwards
    t.speed(0)  # Fastest drawing speed
    t.pensize(2)  # Set pen size for better visibility
    
    # Start drawing the tree
    draw_tree(t, branch_length, angle_left, angle_right, depth, reduction_factor)
    
    # Hide the turtle after drawing
    t.hideturtle()
    
    # Finish drawing
    screen.mainloop()

# Run the program
if __name__ == "__main__":
  main()
