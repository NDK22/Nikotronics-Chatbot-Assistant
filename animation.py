

# Python code to create the GIF animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Text to reveal
text = "Welcome to Nikotronics' Customer Service Chatbox"
font_properties = {"family": "serif", "weight": "bold", "size": 24}

# Initialize the text
txt = ax.text(0.5, 0.5, "", ha="center", va="center", fontdict=font_properties)

# Animation function
def animate(frame):
    txt.set_text(text[:frame + 5])
    return txt,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(text), interval=1, blit=True)

# Save the animation as a GIF
ani.save("nikotronics_animation.gif", writer="imagemagick", fps=7)

print("Classy GIF animation created! Check out 'nikotronics_animation.gif'.")