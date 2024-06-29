import tkinter as tk

# Constants
BOARD_ROWS = 3
BOARD_COLS = 3
cells = 70
canvas_width = cells * BOARD_COLS
canvas_height = cells * BOARD_ROWS




root = tk.Tk()
root.title("Tic Tac Toe Game")



xcolor = ""
ocolor = ""
color_selection_count = 0  
current_player = 'X'
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]



def start_game():
    global xcolor, ocolor
    for widget in root.winfo_children():
        widget.destroy()
        
    draw_board()



def set_color(color):
    global xcolor, ocolor, color_selection_count
    if color_selection_count == 0:
        xcolor = color
        color_selection_count += 1
    elif color_selection_count == 1:
        ocolor = color
        color_selection_count += 1




def draw_board():
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="ivory2")
    
    for i in range(1, BOARD_ROWS):
        canvas.create_line(0, i * cells, canvas_width, i * cells, fill="black", width=5)
    
    for j in range(1, BOARD_COLS):
        canvas.create_line(j * cells, 0, j * cells, canvas_height, fill="black", width=5)
    
    # Button click bounds to the make_move func
    canvas.bind("<Button-1>", lambda event: make_move(event, canvas))




def make_move(event, canvas):
    global current_player
    x, y = event.x, event.y
    row, col = y // cells, x // cells

    if board[row][col] == '':
        board[row][col] = current_player
        draw_mark(canvas, row, col)
        if check_winner():
            winner()
        else:
            current_player = 'O' if current_player == 'X' else 'X'




def draw_mark(canvas, row, col):
    x_center = col * cells + cells // 2
    y_center = row * cells + cells // 2
    if current_player == 'X':
        canvas.create_line(x_center - 20, y_center - 20, x_center + 20, y_center + 20, fill=xcolor, width=5)
        canvas.create_line(x_center - 20, y_center + 20, x_center + 20, y_center - 20, fill=xcolor, width=5)
    else:
        canvas.create_oval(x_center - 20, y_center - 20, x_center + 20, y_center + 20, outline=ocolor, width=5)




# check for 3 in a row
def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False



def winner():
    winner_label = tk.Label(root, text=f"Player {current_player} wins!", font=('arial', 20, 'bold'))
    winner_label.pack(pady=20)




#name_label = tk.Label(root, text="Enter your name:")
#name_entry = tk.Entry(root, textvariable=player_name)
#name_label.pack(padx=10, pady=10)
#name_entry.pack(padx=10, pady=10)

color_label = tk.Label(root, text="Choose what color you wish to play as: ")
color_label.pack(padx=10, pady=10)

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






root.configure(bg='sky blue')
root.mainloop()
