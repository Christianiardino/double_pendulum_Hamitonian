from tkinter import messagebox
from double_pendulum import *
import time

class GUI_generator:
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title("Pendulo duplo")

        self.time_step = 0.01
        self.n_pend = 1
        self.start_simulation = False
        self.total_time = 30
        self.gravity = 9.81
        self.paused = False
        self.caos_bool = False
        self.barra = True
        self.bola = True
        self.tracer = True
        self.bola2 = True

        self.frame = Frame(self.window)
        self.frame.pack(anchor=NW, side=LEFT)

        # Canvas, width, height, t_one, t_two, len_one, len_two, mass_one, mass_two, gravity, vel_one, vel_two
        self.start_condition = []
        self.pendulum = []
        self.y = []

        self.width = width
        self.height = height

        label_num_pend = Label(self.frame, text="Numero de pendulos:")
        label_num_pend.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        self.entry_num_pend = Entry(self.frame)
        self.entry_num_pend.grid(row=0, column=1, padx=10, pady=10)

        label_ang1_pend = Label(self.frame, text="Angulo 1 dos pendulos:")
        label_ang1_pend.grid(row=1, column=0, padx=10, pady=10)
        self.entry_ang1_pend = Entry(self.frame)
        self.entry_ang1_pend.grid(row=1, column=1, padx=10, pady=10)

        label_ang2_pend = Label(self.frame, text="Angulo 2 dos pendulos:")
        label_ang2_pend.grid(row=2, column=0, padx=10, pady=10)
        self.entry_ang2_pend = Entry(self.frame)
        self.entry_ang2_pend.grid(row=2, column=1, padx=10, pady=10)

        label_len1_pend = Label(self.frame, text="Comprimento 1 dos pendulos:")
        label_len1_pend.grid(row=3, column=0, padx=10, pady=10)
        self.entry_len1_pend = Entry(self.frame)
        self.entry_len1_pend.grid(row=3, column=1, padx=10, pady=10)

        label_len2_pend = Label(self.frame, text="Comprimento 2 dos pendulos:")
        label_len2_pend.grid(row=4, column=0, padx=10, pady=10)
        self.entry_len2_pend = Entry(self.frame)
        self.entry_len2_pend.grid(row=4, column=1, padx=10, pady=10)

        label_mass1_pend = Label(self.frame, text="Massa 1 dos pendulos:")
        label_mass1_pend.grid(row=5, column=0, padx=10, pady=10)
        self.entry_mass1_pend = Entry(self.frame)
        self.entry_mass1_pend.grid(row=5, column=1, padx=10, pady=10)

        label_mass2_pend = Label(self.frame, text="Massa 2 dos pendulos:")
        label_mass2_pend.grid(row=6, column=0, padx=10, pady=10)
        self.entry_mass2_pend = Entry(self.frame)
        self.entry_mass2_pend.grid(row=6, column=1, padx=10, pady=10)

        label_time = Label(self.frame, text="Tempo de simulação:")
        label_time.grid(row=7, column=0, padx=10, pady=10)
        self.entry_time = Entry(self.frame)
        self.entry_time.grid(row=7, column=1, padx=10, pady=10)

        label_step = Label(self.frame, text="Step de tempo:")
        label_step.grid(row=8, column=0, padx=10, pady=10)
        self.entry_step = Entry(self.frame)
        self.entry_step.grid(row=8, column=1, padx=10, pady=10)

        label_gravity = Label(self.frame, text="Valor da gravidade:")
        label_gravity.grid(row=9, column=0, padx=10, pady=10)
        self.entry_gravity = Entry(self.frame)
        self.entry_gravity.grid(row=9, column=1, padx=10, pady=10)

        self.button_barra = Button(self.frame, text="Barra", command=lambda: self.barra_pressed())
        self.button_barra.grid(row=10, column=0, padx=10, pady=10)
        self.button_barra.config(bg="green")

        self.button_caos = Button(self.frame, text="Caos", command=lambda: self.caos_pressed())
        self.button_caos.grid(row=10, column=1, padx=10, pady=10)
        self.button_caos.config(bg="red")

        self.button_bola = Button(self.frame, text="Bola 1", command=lambda: self.bola_pressed())
        self.button_bola.grid(row=11, column=0, padx=10, pady=10)
        self.button_bola.config(bg="green")

        self.button_pause = Button(self.frame, text="pausar", command=lambda: self.button_pausar_pressed())
        self.button_pause.grid(row=11, column=1, padx=10, pady=10)

        self.button_bola2 = Button(self.frame, text="Bola 2", command=lambda: self.bola2_pressed())
        self.button_bola2.grid(row=12, column=0, padx=10, pady=10)
        self.button_bola2.config(bg="green")

        self.button_resume = Button(self.frame, text="resumir", command=lambda: self.button_resumir_pressed())
        self.button_resume.grid(row=12, column=1, padx=10, pady=10)

        self.button_tracer = Button(self.frame, text="Tracer", command=lambda: self.tracer_pressed())
        self.button_tracer.grid(row=13, column=0, padx=10, pady=10)
        self.button_tracer.config(bg="green")

        label_ang_dif = Label(self.frame, text="Diferença no angulo:")
        label_ang_dif.grid(row=14, column=0, padx=10, pady=10)
        self.entry_ang_dif = Entry(self.frame)
        self.entry_ang_dif.grid(row=14, column=1, padx=10, pady=10)

        self.canvas = Canvas(self.window, width=width, height=height, bg="#ffffff", bd=2, relief=GROOVE,
                             background="#000000")
        self.canvas.pack(pady=10, padx=0)

    def barra_pressed(self):
        if not self.barra:
            self.barra = True
            self.button_barra.config(bg="green")
        else:
            self.barra = False
            self.button_barra.config(bg="red")

    def bola_pressed(self):
        if not self.bola:
            self.bola = True
            self.button_bola.config(bg="green")
        else:
            self.bola = False
            self.button_bola.config(bg="red")

    def bola2_pressed(self):
        if not self.bola2:
            self.bola2 = True
            self.button_bola2.config(bg="green")
        else:
            self.bola2 = False
            self.button_bola2.config(bg="red")

    def tracer_pressed(self):
        if not self.tracer:
            self.tracer = True
            self.button_tracer.config(bg="green")
        else:
            self.tracer = False
            self.button_tracer.config(bg="red")

    def caos_pressed(self):
        if not self.caos_bool:
            self.caos_bool = True
            self.button_caos.config(bg="green")
        else:
            self.caos_bool = False
            self.button_caos.config(bg="red")

    def button_resumir_pressed(self):
        self.paused = False

    def button_pausar_pressed(self):
        self.paused = True

    def button_start_pressed(self):
        if self.entry_num_pend.get().isdigit():
            self.n_pend = int(self.entry_num_pend.get())
        else:
            messagebox.showinfo('Erro', "Erro em numero de pendulos!")
            return

        # Pass values from entry ang1
        ang_one_pend = [float(random.randrange(0, 600)/100) for i in range(self.n_pend)]
        temp_ang_one_pend = self.entry_ang1_pend.get().split(",")
        for i in range(len(temp_ang_one_pend)):
            try:
                ang_one_pend[i] = float(temp_ang_one_pend[i])
            except:
                ang_one_pend[i] = ang_one_pend[i]

        ang_one_pend[0] = float(random.randrange(200, 400)/100)

        # Pass values from entry ang2
        ang_two_pend = [float(random.randrange(0, 600)/100) for i in range(self.n_pend)]
        temp_ang_two_pend = self.entry_ang2_pend.get().split(",")
        for i in range(len(temp_ang_two_pend)):
            try:
                ang_two_pend[i] = float(temp_ang_two_pend[i])
            except:
                temp_ang_two_pend[i] = 1
                ang_two_pend[i] = ang_two_pend[i]

        # Pass values from entry len1
        len_one_pend = [float(random.randrange(50, 200)/100) for i in range(self.n_pend)]
        temp_len_one_pend = self.entry_len1_pend.get().split(",")
        for i in range(len(temp_len_one_pend)):
            try:
                len_one_pend[i] = float(temp_len_one_pend[i])
            except:
                len_one_pend[i] = len_one_pend[i]

        # Pass values from entry len2
        len_two_pend = [float(random.randrange(50, 200)/100) for i in range(self.n_pend)]
        temp_len_two_pend = self.entry_len2_pend.get().split(",")
        for i in range(len(temp_len_two_pend)):
            try:
                len_two_pend[i] = float(temp_len_two_pend[i])
            except:
                len_two_pend[i] = len_two_pend[i]

        # Pass values from entry mass1
        mass_one_pend = [float(random.randrange(50, 400)/100) for i in range(self.n_pend)]
        temp_mass_one_pend = self.entry_mass1_pend.get().split(",")
        for i in range(len(temp_mass_one_pend)):
            try:
                mass_one_pend[i] = float(temp_mass_one_pend[i])
            except:
                mass_one_pend[i] = mass_one_pend[i]

        # Pass values from entry mass2
        mass_two_pend = [float(random.randrange(50, 400)/100) for i in range(self.n_pend)]
        temp_mass_two_pend = self.entry_mass2_pend.get().split(",")
        for i in range(len(temp_mass_two_pend)):
            try:
                mass_two_pend[i] = float(temp_mass_two_pend[i])
            except:
                mass_two_pend[i] = mass_two_pend[i]

        # Pass values from entry total time
        try:
            self.total_time = float(self.entry_time.get())
        except:
            self.total_time = 30

            # Pass values from entry time step
        try:
            self.time_step = float(self.entry_step.get())
        except:
            self.time_step = 0.01

        # Pass values from entry time gravity
        try:
            self.gravity = float(self.entry_gravity.get())
        except:
            self.gravity = random.randrange(50, 300)/10

        if self.caos_bool:
            ang_dif = float(self.entry_ang_dif.get())
            ang_one_pend = [float(ang_one_pend[0]) + i * ang_dif for i in range(len(ang_one_pend))]
            ang_two_pend = [float(ang_two_pend[0]) + i * ang_dif for i in range(len(ang_two_pend))]
            len_one_pend = [float(len_one_pend[0]) for i in range(len(len_one_pend))]
            len_two_pend = [float(len_two_pend[0]) for i in range(len(len_two_pend))]
            mass_one_pend = [float(mass_one_pend[0]) for i in range(len(mass_one_pend))]
            mass_two_pend = [float(mass_two_pend[0]) for i in range(len(mass_two_pend))]


        # Canvas, width, height, t_one, t_two, len_one, len_two, mass_one, mass_two, gravity, vel_one, vel_two
        for i in range(self.n_pend):
            self.start_condition.append([self.canvas, self.width, self.height, ang_one_pend[i], ang_two_pend[i],
                                         len_one_pend[i], len_two_pend[i], mass_one_pend[i], mass_two_pend[i],
                                         self.gravity, 0, 0, self.total_time, self.time_step,
                                         self.barra, self.bola, self.bola2, self.tracer])

        self.calc_pend()
        self.update_position()

    def ret_varaibles(self):
        return self.window

    def calc_pend(self):
        # Wait buttons star be pressed, while calculate the values
        for i in range(self.n_pend):
            self.start_condition.append(self.start_condition)
            self.pendulum.append(double_pendulum(*self.start_condition[i]))
            self.y.append(self.pendulum[i].calc_position())

    def update_position(self):
        i = 0
        while i < len(self.y[0]):
            if self.paused:
                time.sleep(0.01)
            else:
                for k in range(self.n_pend):
                    self.pendulum[k].calculate_new_position(self.y[k][:, 0][i], self.y[k][:, 2][i])
                time.sleep(0.01)
                i += 1
            self.window.update()
