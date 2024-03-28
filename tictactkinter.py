#tictactkinter
import random
import tkinter as tk

#variables
moves = 0
players = ['X', 'O']
postype = {'Edge':[1, 3, 5, 7], 'Corner':[0, 2, 6, 8], 'Center':[4]}
player = 'X'
wincon = [[0, 1, 2], [0, 3, 6], [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5]]
wind ={0: [[0, 1, 2], [0, 3, 6], [0, 4, 8]], 1: [[0, 1, 2], [1, 4, 7]],
       2: [[0, 1, 2], [2, 5, 8],[2, 4, 6]], 3: [[0, 3, 6], [3, 4, 5]],
       6: [[0, 3, 6], [6, 7, 8], [2, 4, 6]], 7: [[6, 7, 8], [1, 4, 7]],
       8: [[6, 7, 8], [2, 5, 8], [0, 4, 8]], 5: [[2, 5, 8], [3, 4, 5]],
       4: [[0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5]]}
games = []
comp = players[(players.index(player)+1)%2]
        
def opengamewindow(gametype):
    global player, board, moves, players, postype, wind, games, comp

    def dest():
        global games
        for window in games:
            games.remove(window)
            window.destroy()       
        
    def move(b, l):
        global player, moves, game, comp
        blist = [b0, b1, b2, b3, b4, b5, b6, b7, b8]
        pos = blist.index(b)
        if b['text'] == ' ':
            b.config(text=player) 
            if gametype == 'MULTIPLAYER':
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

            moves += 1
            if moves == 9:
                gameover(pos)
                return None

            if gametype == 'MULTIPLAYER':
                l.config(text=player+' TO PLAY')
             
            if gametype == 'SINGLEPLAYER':
                if gameover(blist.index(b)):
                    return None
                board = []
                for b in blist:
                    board.append(b['text'])
                cmove = computer(pos)
                blist[cmove]['text'] = comp
                gameover(cmove)
                moves += 1
                if moves == 9:
                    gameover(pos)
                    return None
                
    def gameover(index):
        global wind, game, players, moves
        blist = [b0, b1, b2, b3, b4, b5, b6, b7, b8]
        if moves <= 9:
            checklist = wind[index]
            for vector in checklist:
                if blist[vector[0]]['text'] == blist[vector[1]]['text'] and blist[vector[1]]['text'] == blist[vector[2]]['text']:
                    root.deiconify()
                    if gametype == 'MULTIPLAYER':
                        wplayer = players[(players.index(player)+1)%2]
                    else:
                        wplayer = blist[vector[0]]['text']
                    l0.config(text=wplayer+' WINS')
                    for b in blist:
                        b['state'] = tk.DISABLED
                    return True
                        
        if moves == 9 and 'WINS' not in l0['text']:
            root.deiconify()
            l0.config(text='TIE')
            for b in blist:
                b['state'] = tk.DISABLED
            return True

    def computer(pos):
        global postype, player, index, moves, wincon, comp, game
        board, blist = [], [b0, b1, b2, b3, b4, b5, b6, b7, b8]
        for b in blist:
            board.append(b['text'])
            
        if moves == 1 and pos != 4:
            cmove = 4
            
        elif moves == 1 and pos == 4:
            cmove = random.choice(postype['Corner'])
                    
        else:
            win = []
            los = []
            for vector in wincon:
                vechar = []
                for position in vector:
                    vechar.append(board[position])
                    
                if vechar.count(comp) == 2 and vechar.count(' ') == 1:
                    win.append(vector[vechar.index(' ')])
                if vechar.count(player) == 2 and vechar.count(' ') == 1:
                    los.append(vector[vechar.index(' ')])
                    
            if len(win) != 0:
                cmove = random.choice(win)
            elif len(los) != 0:
                cmove = random.choice(los)
                
            elif moves == 3:
                a = True
                for i in postype['Edge']:
                    if board[i] != ' ':
                        False
                if a:
                    cmove = random.choice(postype['Edge'])   
            else:
                pm = []
                for i in range(len(board)):
                    if board[i] == ' ':
                        pm.append(i)
                cmove = random.choice(pm)
                
            
                
        return cmove
             
    root.withdraw()
    moves = 0
    game = tk.Toplevel(root)
    game.title(gametype)
    game.geometry('210x219')
    dest()
    games.append(game)
            
    b0 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b0,l0), gameover(0)], height=2, width=5)
    b1 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b1,l0), gameover(1)], height=2, width=5)
    b2 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b2,l0), gameover(2)], height=2, width=5)
    b3 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b3,l0), gameover(3)], height=2, width=5)
    b4 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b4,l0), gameover(4)], height=2, width=5)
    b5 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b5,l0), gameover(5)], height=2, width=5)
    b6 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b6,l0), gameover(6)], height=2, width=5)
    b7 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b7,l0), gameover(7)], height=2, width=5)
    b8 = tk.Button(game, text=' ', bg='black', fg='white', font='agencyfb 15 bold', command=lambda:[move(b8,l0), gameover(8)], height=2, width=5)    
    
    b0.grid(row=1, column=0)
    b1.grid(row=1, column=1)
    b2.grid(row=1, column=2)
    b3.grid(row=2, column=0)
    b4.grid(row=2, column=1)
    b5.grid(row=2, column=2)
    b6.grid(row=3, column=0)
    b7.grid(row=3, column=1)
    b8.grid(row=3, column=2)

    if gametype == 'SINGLEPLAYER':
        start = 0#random.randint(0, 1)
        if start == 0:
            player = 'X'
            comp = players[(players.index(player)+1)%2]
        else:
            player = 'O'
            comp = players[(players.index(player)+1)%2]
            b4['text'] = comp
            moves += 1
            
    l0 = tk.Label(game, text=player+' TO PLAY')
    l0.grid(row=0, column=0)
    
#root
root = tk.Tk()
root.title('TIC TAC TOE')
root.geometry('242x132')

gamemode = tk.Label(root, text='GAMEMODE', font='agencyfb 30 bold', fg='White', bg='grey30')
single = tk.Button(root, text='SINGLE PLAYER', font='agencyfb 15', bg='black', fg='FloralWhite', command=lambda:opengamewindow('SINGLEPLAYER'))
multi = tk.Button(root, text='MULTIPLAYER', font='agencyfb 15', bg='black', fg='FloralWhite', command=lambda:opengamewindow('MULTIPLAYER'))


gamemode.grid(sticky='EW')
single.grid(row=1, sticky='EW')
multi.grid(row=2, sticky='EW')

#calling mainloop
root.mainloop()



