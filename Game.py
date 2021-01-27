import tkinter as tk
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk, ImageSequence


count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player_turn=20
def main_menu():
    global count
    global number
    root = tk.Tk()
    root.geometry('500x500')
    root.minsize(500, 500)
    root.maxsize(500, 500)
    root.iconbitmap('logo.ico')
    root.title('Tic_Tac_Toe')
    root.config(bg='#000000')

    img2 = Image.open("2.jpg")
    img2 = img2.resize([330, 330])
    pic2 = ImageTk.PhotoImage(img2)
    img_blank = Image.open(r"3.jpg")
    img_blank = img_blank.resize([100, 100])
    pic_blank = ImageTk.PhotoImage(img_blank)
    img_cross = Image.open(r"4.jpg")
    img_cross = img_cross.resize([100, 100])
    pic_cross = ImageTk.PhotoImage(img_cross)
    img_circle = Image.open(r"5.jpg")
    img_circle = img_circle.resize([100, 100])
    pic_circle = ImageTk.PhotoImage(img_circle)
    img_newcross = Image.open(r"6.png")
    img_newcross = img_newcross.resize([100, 100])
    pic_newcross = ImageTk.PhotoImage(img_newcross)
    img_newcircle = Image.open(r"7.png")
    img_newcircle = img_newcircle.resize([100, 100])
    pic_newcircle = ImageTk.PhotoImage(img_newcircle)
    img_xwin = Image.open(r"8.jpg")
    img_xwin = img_xwin.resize([350, 350])
    pic_xwin = ImageTk.PhotoImage(img_xwin)
    img_owin = Image.open(r"9.jpg")
    img_owin = img_owin.resize([350, 350])
    pic_owin = ImageTk.PhotoImage(img_owin)
    img_quit = Image.open(r"10.jpg")
    img_quit = img_quit.resize([58, 58])
    pic_quit = ImageTk.PhotoImage(img_quit)
    img_replay = Image.open(r"11.jpg")
    img_replay = img_replay.resize([60, 60])
    pic_replay = ImageTk.PhotoImage(img_replay)
    img_draw = Image.open(r"12.jpg")
    img_draw = img_draw.resize([500, 500])
    pic_draw = ImageTk.PhotoImage(img_draw)
    img_homebutton=Image.open(r"home.jpg")
    img_homebutton = img_homebutton.resize([50, 50])
    pic_homebutton=ImageTk.PhotoImage(img_homebutton)
    img_newhomebutton = Image.open(r"newhome.jpg")
    img_newhomebutton = img_newhomebutton.resize([50, 50])
    pic_newhomebutton = ImageTk.PhotoImage(img_newhomebutton)

    def info(event):
        tmsg.showinfo('Team-Takedown', 'Aryan Solanki\t         E20CSE157\nYash Sharma\t         '
                                       'E20CSE158\nAryaman Nagdev\t         E20CSE178\nShubhankar Samadar     E20CSE161')


    def player_vs_player_gui(event):
        a.pack_forget()
        def animate_title(counter):
            title_canvas.itemconfig(image, image=title_sequence[counter])
            root.after(20, lambda: animate_title((counter + 1) % len(title_sequence)))

        title_canvas = tk.Canvas(root, width=300, height=130, bg='black',borderwidth=0,highlightthickness=0)
        title_canvas.place(x=100,y=0)
        title_sequence = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open(
                    r'titlegif.gif'))]
        image = title_canvas.create_image(150, 70, image=title_sequence[0])
        animate_title(1)

        def gui_reset():
            global count
            global number
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            number = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            root.destroy()
            main_menu()

        def home_button_hover(event):
            home_button.config(image=pic_newhomebutton)
            home_button.image = pic_newhomebutton

        def home_button_hoverback(event):
            home_button.config(image=pic_homebutton)
            home_button.image = pic_homebutton
        home_button=tk.Button(image=pic_homebutton, borderwidth=0, highlightthickness=0, command=gui_reset)
        home_button.place(x=0, y=0)
        home_button.bind('<Enter>',home_button_hover)
        home_button.bind('<Leave>',home_button_hoverback)

        def reset():
            quit = tk.Button(image=pic_quit, borderwidth=0, highlightthickness=0, command=root.destroy)
            quit.place(x=264, y=220)
            reset_button = tk.Button(image=pic_replay, borderwidth=0, highlightthickness=0, command=gui_reset)
            reset_button.place(x=185, y=220)

        def check_win():
            if (count[0] == count[1] == count[2] == 10) or (count[0] == count[1] == count[2] == 20):
                return True
            elif (count[3] == count[4] == count[5] == 10) or (count[3] == count[4] == count[5] == 20):
                return True
            elif (count[6] == count[7] == count[8] == 10) or (count[6] == count[7] == count[8] == 20):
                return True
            elif (count[0] == count[3] == count[6] == 10) or (count[0] == count[3] == count[6] == 20):
                return True
            elif (count[1] == count[4] == count[7] == 10) or (count[1] == count[4] == count[7] == 20):
                return True
            elif (count[2] == count[5] == count[8] == 10) or (count[2] == count[5] == count[8] == 20):
                return True
            elif (count[0] == count[4] == count[8] == 10) or (count[0] == count[4] == count[8] == 20):
                return True
            elif (count[6] == count[4] == count[2] == 10) or (count[6] == count[4] == count[2] == 20):
                return True
        def chance_general(eff=None,count_number=50,button_name=tk.Button):
            global count
            global number
            if count[count_number] == 0:
                button_name.config(image=pic_newcircle)
                button_name.image = pic_newcircle
                count[count_number] = 10
                for _ in range(0, 9):
                    if count[_] != 10 and count[_] != 20:
                        count[_] = 1
                    if count[_] != 1 and count[_] != 0:
                        number[count_number] += 1
                if number[count_number] >= 3:
                    if check_win() == True:
                        tk.Label(image=pic_owin, borderwidth=0, highlightthickness=0).place(x=73, y=150)
                        reset()
                    else:
                        if number[count_number] == 9:
                            tk.Label(image=pic_draw, borderwidth=0, highlightthickness=0).place(x=-5, y=150)
                            reset()

            elif count[count_number] == 1:
                button_name.config(image=pic_newcross)
                button_name.image = pic_newcross
                count[count_number] = 20
                for _ in range(0, 9):
                    if count[_] != 10 and count[_] !=20:
                        count[_] = 0
                    if count[_] != 1 and count[_] != 0:
                        number[count_number] += 1
                if number[count_number] >= 3:
                    if check_win() == True:
                        tk.Label(image=pic_xwin, borderwidth=0, highlightthickness=0).place(x=73, y=150)
                        reset()
                    else:
                        if number[count_number] == 9:
                            tk.Label(image=pic_draw, borderwidth=0, highlightthickness=0).place(x=-5, y=150)
                            reset()
        def hover_change(count_number,button_name):
            if count[count_number] == 0:
                button_name.config(image=pic_circle)
                button_name.image = pic_circle
            elif count[count_number] == 1:
                button_name.config(image=pic_cross)
                button_name.image = pic_cross
        def hover_change_back(count_number,button_name):
            if count[count_number] == 0:
                button_name.config(image=pic_blank)
                button_name.image = pic_blank
            elif count[count_number] == 1:
                button_name.config(image=pic_blank)
                button_name.image = pic_blank

        tk.Label(image=pic2, borderwidth=0).place(x=85,y=150)

        button1 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,0,button1))
        button1.place(x=85, y=150)
        button1.bind('<Enter>', lambda event,count_number=0,button_name=button1:hover_change(count_number,button_name))
        button1.bind('<Leave>', lambda event,count_number=0,button_name=button1:hover_change_back(count_number,button_name))

        button2 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,1,button2))
        button2.place(x=200, y=150)
        button2.bind('<Enter>', lambda event,count_number=1,button_name=button2:hover_change(count_number,button_name))
        button2.bind('<Leave>', lambda event,count_number=1,button_name=button2:hover_change_back(count_number,button_name))

        button3 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,2,button3))
        button3.place(x=315, y=150)
        button3.bind('<Enter>', lambda event,count_number=2,button_name=button3:hover_change(count_number,button_name))
        button3.bind('<Leave>', lambda event,count_number=2,button_name=button3:hover_change_back(count_number,button_name))

        button4 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,3,button4))
        button4.place(x=85, y=265)
        button4.bind('<Enter>', lambda event,count_number=3,button_name=button4:hover_change(count_number,button_name))
        button4.bind('<Leave>', lambda event,count_number=3,button_name=button4:hover_change_back(count_number,button_name))

        button5 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,4,button5))
        button5.place(x=200, y=265)
        button5.bind('<Enter>', lambda event,count_number=4,button_name=button5:hover_change(count_number,button_name))
        button5.bind('<Leave>', lambda event,count_number=4,button_name=button5:hover_change_back(count_number,button_name))

        button6 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,5,button6))
        button6.place(x=315, y=265)
        button6.bind('<Enter>', lambda event,count_number=5,button_name=button6:hover_change(count_number,button_name))
        button6.bind('<Leave>', lambda event,count_number=5,button_name=button6:hover_change_back(count_number,button_name))

        button7 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,6,button7))
        button7.place(x=85, y=375)
        button7.bind('<Enter>', lambda event,count_number=6,button_name=button7:hover_change(count_number,button_name))
        button7.bind('<Leave>', lambda event,count_number=6,button_name=button7:hover_change_back(count_number,button_name))

        button8 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,7,button8))
        button8.place(x=200, y=375)
        button8.bind('<Enter>', lambda event,count_number=7,button_name=button8:hover_change(count_number,button_name))
        button8.bind('<Leave>', lambda event,count_number=7,button_name=button8:hover_change_back(count_number,button_name))

        button9 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,8,button9))
        button9.place(x=315, y=375)
        button9.bind('<Enter>', lambda event,count_number=8,button_name=button9:hover_change(count_number,button_name))
        button9.bind('<Leave>', lambda event,count_number=8,button_name=button9:hover_change_back(count_number,button_name))
        root.mainloop()
    def player_vs_comp(event):
        global count
        a.pack_forget()
        def animate_title(counter):
            title_canvas.itemconfig(image, image=title_sequence[counter])
            root.after(20, lambda: animate_title((counter + 1) % len(title_sequence)))

        title_canvas = tk.Canvas(root, width=300, height=130, bg='black',borderwidth=0,highlightthickness=0)
        title_canvas.place(x=100,y=0)
        title_sequence = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open(
                    r'titlegif.gif'))]
        image = title_canvas.create_image(150, 70, image=title_sequence[0])
        animate_title(1)


        def is_end():

            for i in range(0, 3):
                if count[i] != 0 and count[i] != 1 and (
                        count[i] == count[i + 3] == count[i + 6]):
                    return count[i]

            for i in range(0, 7, 3):
                if (count[i] == count[i + 1] == count[i + 2] == 20):
                    return 20
                elif (count[i] == count[i + 1] == count[i + 2] == 10):
                    return 10

            if (count[0] != 0 and count[0] != 1 and (
                    count[0] == count[4] == count[8])):
                return count[0]

            if (count[2] != 0 and count[2] != 1 and (
                    count[2] == count[4] == count[6])):
                return count[2]

            for i in range(0, 9):
                if (count[i] == 0) or (count[i] == 1):
                    return None
            return '.'

        def max():
            global mini
            maxv = -2

            pindex = None

            result = is_end()

            if result == 20:
                return (-1, 0)

            elif result == 10:
                return (1, 0)

            elif result == '.':
                return (0, 0)

            for i in range(0, 9):
                if count[i] == 0:
                    count[i] = 10
                    (m, mini) = min()

                    if m > maxv:
                        maxv = m
                        pindex = i
                    count[i] = 0
                elif count[i] == 1:
                    count[i] = 10
                    (m, mini) = min()

                    if m > maxv:
                        maxv = m
                        pindex = i
                    count[i] = 1
            return (maxv, pindex)

        def min():
            global maxi
            minv = 2

            qindex = None
            result = is_end()

            if result == 20:
                return (-1, 0)

            elif result == 10:
                return (1, 0)

            elif result == '.':
                return (0, 0)

            for i in range(0, 9):
                if count[i] == 0:
                    count[i] = 20
                    (m, maxi) = max()
                    if m < minv:
                        minv = m
                        qindex = i
                    count[i] = 0
                elif count[i] == 1:
                    count[i] = 20
                    (m, maxi) = max()
                    if m < minv:
                        minv = m
                        qindex = i
                    count[i] = 1
            return (minv, qindex)

        def play(input_index):
            global player_turn
            while True:
                result = is_end()

                if result != None:
                    return
                if player_turn == 20:

                    while True:
                        (m, qindex) = min()

                        count[input_index] = 20
                        player_turn = 10
                        break

                else:
                    (m, pindex) = max()
                    count[pindex] = 10
                    player_turn = 20
                    return (pindex)

        def check_result():
            while True:
                result = is_end()
                if result != None:
                    if result == 20:
                        tk.Label(image=pic_owin, borderwidth=0, highlightthickness=0).place(x=73, y=150)
                        reset()
                    elif result == 10:
                        tk.Label(image=pic_xwin, borderwidth=0, highlightthickness=0).place(x=73, y=150)
                        reset()
                    elif result == '.':
                        tk.Label(image=pic_draw, borderwidth=0, highlightthickness=0).place(x=-5, y=150)
                        reset()

                    return
                break



        def gui_reset():
            global count
            global number
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            number = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            root.destroy()
            main_menu()

        def home_button_hover(event):
            home_button.config(image=pic_newhomebutton)
            home_button.image = pic_newhomebutton

        def home_button_hoverback(event):
            home_button.config(image=pic_homebutton)
            home_button.image = pic_homebutton

        home_button = tk.Button(image=pic_homebutton, borderwidth=0, highlightthickness=0, command=gui_reset)
        home_button.place(x=0, y=0)
        home_button.bind('<Enter>', home_button_hover)
        home_button.bind('<Leave>', home_button_hoverback)

        def reset():
            quit = tk.Button(image=pic_quit, borderwidth=0, highlightthickness=0, command=root.destroy)
            quit.place(x=264, y=220)
            reset_button = tk.Button(image=pic_replay, borderwidth=0, highlightthickness=0, command=gui_reset)
            reset_button.place(x=185, y=220)


        def chance_general(eff=None,count_number=50,button_name=tk.Button):
            global ai
            global count
            global number
            if count[count_number] == 0:
                button_name.config(image=pic_newcircle)
                button_name.image = pic_newcircle
                count[count_number] = 20
                play(count_number)
                check_result()
            if count[0] == 10:
                button1.config(image=pic_newcross)
                button1.image = pic_newcross
            if count[1] == 10:
                button2.config(image=pic_newcross)
                button2.image = pic_newcross
            if count[2] == 10:
                button3.config(image=pic_newcross)
                button3.image = pic_newcross
            if count[3] == 10:
                button4.config(image=pic_newcross)
                button4.image = pic_newcross
            if count[4] == 10:
                button5.config(image=pic_newcross)
                button5.image = pic_newcross
            if count[5] == 10:
                button6.config(image=pic_newcross)
                button6.image = pic_newcross
            if count[6] == 10:
                button7.config(image=pic_newcross)
                button7.image = pic_newcross
            if count[7] == 10:
                button8.config(image=pic_newcross)
                button8.image = pic_newcross
            if count[8] == 10:
                button9.config(image=pic_newcross)
                button9.image = pic_newcross

        def hover_change(count_number,button_name):
            if count[count_number] == 0:
                button_name.config(image=pic_circle)
                button_name.image = pic_circle

        def hover_change_back(count_number,button_name):
            if count[count_number] == 0:
                button_name.config(image=pic_blank)
                button_name.image = pic_blank

        tk.Label(image=pic2, borderwidth=0).place(x=85, y=150)

        button1 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,0,button1))
        button1.place(x=85, y=150)
        button1.bind('<Enter>', lambda event,count_number=0,button_name=button1:hover_change(count_number,button_name))
        button1.bind('<Leave>', lambda event,count_number=0,button_name=button1:hover_change_back(count_number,button_name))

        button2 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,1,button2))
        button2.place(x=200, y=150)
        button2.bind('<Enter>', lambda event,count_number=1,button_name=button2:hover_change(count_number,button_name))
        button2.bind('<Leave>', lambda event,count_number=1,button_name=button2:hover_change_back(count_number,button_name))

        button3 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,2,button3))
        button3.place(x=315, y=150)
        button3.bind('<Enter>', lambda event,count_number=2,button_name=button3:hover_change(count_number,button_name))
        button3.bind('<Leave>', lambda event,count_number=2,button_name=button3:hover_change_back(count_number,button_name))

        button4 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,3,button4))
        button4.place(x=85, y=265)
        button4.bind('<Enter>', lambda event,count_number=3,button_name=button4:hover_change(count_number,button_name))
        button4.bind('<Leave>', lambda event,count_number=3,button_name=button4:hover_change_back(count_number,button_name))

        button5 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0, command=lambda: chance_general(None,4,button5))
        button5.place(x=200, y=265)
        button5.bind('<Enter>', lambda event,count_number=4,button_name=button5:hover_change(count_number,button_name))
        button5.bind('<Leave>', lambda event,count_number=4,button_name=button5:hover_change_back(count_number,button_name))

        button6 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,5,button6))
        button6.place(x=315, y=265)
        button6.bind('<Enter>', lambda event,count_number=5,button_name=button6:hover_change(count_number,button_name))
        button6.bind('<Leave>', lambda event,count_number=5,button_name=button6:hover_change_back(count_number,button_name))

        button7 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,6,button7))
        button7.place(x=85, y=375)
        button7.bind('<Enter>', lambda event,count_number=6,button_name=button7:hover_change(count_number,button_name))
        button7.bind('<Leave>', lambda event,count_number=6,button_name=button7:hover_change_back(count_number,button_name))

        button8 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,7,button8))
        button8.place(x=200, y=375)
        button8.bind('<Enter>', lambda event,count_number=7,button_name=button8:hover_change(count_number,button_name))
        button8.bind('<Leave>', lambda event,count_number=7,button_name=button8:hover_change_back(count_number,button_name))

        button9 = tk.Button(image=pic_blank, borderwidth=0, highlightthickness=0,command=lambda: chance_general(None,8,button9))
        button9.place(x=315, y=375)
        button9.bind('<Enter>', lambda event,count_number=8,button_name=button9:hover_change(count_number,button_name))
        button9.bind('<Leave>', lambda event,count_number=8,button_name=button9:hover_change_back(count_number,button_name))


    def animate(counter):
        a.config(image=sequence[counter])
        a.image = sequence[counter]
        root.after(75, lambda: animate((counter + 1) % len(sequence)))

    a = tk.Button(root, width=500, height=500, command=player_vs_player_gui,borderwidth=0, highlightthickness=0)
    a.pack()
    a.bind('<Button 1>',player_vs_player_gui)
    a.bind('<Button 2>',info)
    root.bind('i',info)

    a.bind('<Button 3>',player_vs_comp)
    sequence = [ImageTk.PhotoImage(img)
                for img in ImageSequence.Iterator(
            Image.open(
                r'main_screen.gif'))]
    animate(1)


    root.mainloop()
main_menu()
