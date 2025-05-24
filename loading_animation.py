"""
This script displays an animated loading circle using Tkinter.
The animation shows a series of dots arranged in a circle, with one dot
highlighted and the highlight rotating through the dots.
The animation can be paused and resumed by pressing the spacebar.
"""
import tkinter as tk
import math

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Loading...")

# Set the window geometry
root.geometry("200x200")

# Create a Canvas widget
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(fill="both", expand=True)

# Parameters for the loading circle
num_dots = 12  # Number of dots in the circle
circle_radius = 50  # Radius of the circle on which dots are placed
dot_radius = 5  # Radius of each individual dot
center_x = 100
center_y = 100
inactive_color = "lightgray"  # Color of the dots that are not currently active
active_color = "blue"  # Color of the currently active/highlighted dot

# List to store dot object references
dots = []

# Calculate and draw dots
# The dots are arranged in a circle. Trigonometric functions (cos and sin)
# are used to calculate the (x, y) coordinates for each dot based on its angle.
for i in range(num_dots):
    # Calculate the angle for each dot (in radians)
    angle = (2 * math.pi / num_dots) * i
    # Calculate x coordinate: center_x + radius * cos(angle)
    x = center_x + circle_radius * math.cos(angle)
    # Calculate y coordinate: center_y + radius * sin(angle)
    y = center_y + circle_radius * math.sin(angle)
    
    dot_id = canvas.create_oval(
        x - dot_radius, y - dot_radius,
        x + dot_radius, y + dot_radius,
        fill=inactive_color, outline=inactive_color
    )
    dots.append(dot_id)

# Active dot index
active_dot_index = 0

# Global variable to control animation state
is_animating = True  # True if the animation is running, False if paused

# Function to update the animation
def update_animation():
    """
    Updates the animation by changing the color of the dots.
    It highlights the current 'active' dot and sets others to 'inactive'.
    Then, it advances the active dot index and reschedules itself to run
    again after a specified delay, creating the animation loop.
    """
    global active_dot_index, is_animating
    
    if not is_animating: # If animation is paused, do nothing further in this cycle
        return
        
    # Update dot colors: active dot gets active_color, others get inactive_color
    for i, dot_id in enumerate(dots):
        if i == active_dot_index:
            canvas.itemconfig(dot_id, fill=active_color)
        else:
            canvas.itemconfig(dot_id, fill=inactive_color)
            
    # Move to the next dot for the next frame
    active_dot_index = (active_dot_index + 1) % num_dots
    
    # Schedule this function to be called again after ANIMATION_DELAY milliseconds
    # ANIMATION_DELAY is 100ms
    root.after(100, update_animation)

# Function to toggle animation
def toggle_animation(event=None):
    """
    Pauses or resumes the animation.
    It flips the 'is_animating' boolean flag. If the animation is resumed,
    it calls 'update_animation' to restart the animation sequence.
    This function can be triggered by an event (e.g., key press).
    """
    global is_animating
    is_animating = not is_animating
    if is_animating:
        # If animation was paused and is now resumed, start the update loop again
        update_animation()

# Bind spacebar press to the toggle_animation function
# This allows the user to pause/resume the animation by pressing the spacebar.
root.bind('<space>', toggle_animation)

# Start the animation initially
update_animation()

# Start the Tkinter event loop
root.mainloop()
