import tkinter as tk
from tkinter import ttk

BOARD_ROWS = 3
BOARD_COLS = 3
cells = 100
canvas_width = cells * BOARD_COLS
canvas_height = cells * BOARD_ROWS

root = tk.Tk()
root.title("Tic Tac Toe Game")



# Display name later
player_name = tk.StringVar()
selected_color = ""





def start_game():
    global selected_color
    for widget in root.winfo_children():
        widget.destroy()
        
    # Initialize game board with selected color
    draw_board(selected_color)




def set_color(color):
    # Set background color based on user's choise
    global selected_color
    selected_color = color




name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root, textvariable=player_name)
name_label.pack(padx=10, pady=10)
name_entry.pack(padx=10, pady=10)


lavender_button = tk.Button(root, font=('arial', 15, 'bold'), text="Lavender", bg="black", fg="purple", command=lambda: set_color("plum1"))
lavender_button.pack(padx=5, pady=5)

blue_button = tk.Button(root, font=('arial', 15, 'bold'), text="Blue", bg="black", fg="blue", command=lambda: set_color("turquoise"))
blue_button.pack(padx=5, pady=5)

pink_button = tk.Button(root, font=('arial', 15, 'bold'), text="Pink", bg="black", fg="red", command=lambda: set_color("pink"))
pink_button.pack(padx=5, pady=5)

white_button = tk.Button(root, font=('arial', 15, 'bold'), text="White", bg="black", fg="black", command=lambda: set_color("white"))
white_button.pack(padx=5, pady=5)

start_button = tk.Button(root, font=('arial', 15, 'bold'), text="Start Game", bg="black", fg="green", command=start_game)
start_button.pack(padx=10, pady=10)




# Draw the board with the selected color
def draw_board(color):
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill=color)
    
    # Draw Tic Tac Toe grid lines
    for i in range(1, BOARD_ROWS):
        canvas.create_line(0, i * cells, canvas_width, i * cells, fill="black", width=5)
    
    for j in range(1, BOARD_COLS):
        canvas.create_line(j * cells, 0, j * cells, canvas_height, fill="black", width=5)







root.configure(bg='sky blue')
root.mainloop()
