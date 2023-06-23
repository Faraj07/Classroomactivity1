import tkinter as tk
import requests

# Function to get a random joke from an API
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    return f"{data['setup']} {data['punchline']}"

# Create the tkinter window
window = tk.Tk()
window.title("Jokes")

# Create a label for displaying the jokes
joke_label = tk.Label(window, text="")
joke_label.pack()

# Function to update the label with a new joke
def update_joke():
    joke = get_joke()
    joke_label.configure(text=joke)
    window.after(5000, update_joke)

update_joke()

# Start the tkinter event loop
window.mainloop()
