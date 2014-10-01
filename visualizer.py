from Tkinter import *

def read_line(line):
    #Parses records.txt
    #Format of records.txt is:
    #week:winner/loser,winner/loser,winner/loser,winner/loser
    [week,split_line] = line.split(":")
    matchups = split_line.split(",")
    print "Week " + week
    for matchup in matchups:
        [winner, loser] = matchup.split("/")
        if "\n" in loser:
            loser = loser[0:len(loser)-1]
        print winner + " beat " + loser
        draw_win_line(winner, loser, week)

def draw_win_line(winner, loser, week):
    #Draws a color-coded line connecting each matchup
    [winner_x, winner_y] = owner_dic[winner]
    [loser_x, loser_y] = owner_dic[loser]
    
    octagon_size = 400
    x_offset = 50
    y_offset = 50

    #Scale points up to the size of the window, and center it
    winner_x = winner_x*octagon_size + x_offset
    winner_y = winner_y*octagon_size + y_offset
    loser_x = loser_x*octagon_size + x_offset
    loser_y = loser_y*octagon_size + y_offset

    midpoint_x = (winner_x + loser_x) / 2
    midpoint_y = (winner_y + loser_y) / 2
    
    win.create_line(winner_x, winner_y,midpoint_x, midpoint_y, fill = "green", width = 5)
    win.create_line(midpoint_x, midpoint_y, loser_x, loser_y, fill = "red", width = 5)

def add_label(owner):
    [owner_x, owner_y] = owner_dic[owner]
    widget = Label(win, text = owner)

    if owner_x == 0:
        win.create_window(50, 400*owner_y+50, window=widget)
    if owner_y == 0:
        win.create_window(400*owner_x+50, 50, window=widget)
    if owner_x == 1:
        win.create_window(450, 400*owner_y+50, window=widget)
    if owner_y == 1:
        win.create_window(400*owner_x+50, 450, window=widget)
        
def main():
    master = Tk()
    global win
    win = Canvas(master, width = 500, height = 500)
    win.pack()
    records_file = open('records.txt', 'r')

    for line in records_file:   
        read_line(line)

    for owner in owner_dic:
        add_label(owner)

    records_file.close()

    mainloop()

global owner_dic
owner_dic = {"Robert":[0,.25], "Troy":[0,.75], "Chris":[.25,0], "Dale":[.75,0],\
              "Dejan":[1,.25], "Jordan":[1,.75], "Rick":[.25,1], "Ram":[.75,1]}

main()
