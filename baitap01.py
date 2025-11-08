from guizero import App, Box, PushButton, Text 
app = App(title="Trụ Đèn Giao Thông Tự Động", width=250, height=500, layout="auto")
text=Text(app, text="Trụ Đèn Giao Thông\n", font="Helvetica",size=17)
box = Box(app, layout="grid", width=120, height=360, align="top")
DARKcl = "dark gray"
TEXTcl = "black"
REDcl = "red"
YELLOWcl = "yellow"
GREENcl = "green"
TRANSITIONS = {"red": {"next": "yellow", "duration": 10, "color": REDcl},"yellow": {"next": "green", "duration": 3, "color": YELLOWcl},"green": {"next": "red", "duration": 10, "color": GREENcl},}
current_state = "red" 
countdown = TRANSITIONS[current_state]["duration"] 
red_light = PushButton(box, grid=[0, 0], text="", width=10, height=5, enabled=False ) # enabled=False Nghĩa là nút đó bị vô hiệu hóa
yellow_light = PushButton(box, grid=[0, 1], text="", width=10, height=5, enabled=False) 
green_light = PushButton(box, grid=[0, 2], text="", width=10, height=5, enabled=False) 
lights = {"red": red_light,"yellow": yellow_light,"green": green_light}
countdown_display = Text(app, text=f"Chuyển sau: {countdown} s", size=16, color=TEXTcl, font="Helvetica")
def update_lights_gui():
    red_light.bg = DARKcl
    yellow_light.bg = DARKcl
    green_light.bg = DARKcl
    if current_state in lights:
        lights[current_state].bg = TRANSITIONS[current_state]["color"]
def change_light():
    global current_state, countdown
    next_state_info = TRANSITIONS.get(current_state)
    if next_state_info:
        current_state = next_state_info["next"]
        countdown = TRANSITIONS[current_state]["duration"]
    update_lights_gui()
def countdown_timer():
    global countdown
    if countdown <= 0:
        change_light()
    countdown_display.value = f"Chuyển sau: {countdown} s"
    countdown -= 1
    app.after(1000, countdown_timer)
update_lights_gui() 
countdown_timer() 
app.display()