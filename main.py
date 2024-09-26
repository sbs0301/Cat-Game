import tkinter 
import random

index = 0
timer = 0
score = 0
hisc = 0
difficulty = 0 #난이도를 관리해주는 변수
next = 0

mouse_x = 0
mouse_y = 0
mouse_c = 0 #클릭 여부
cursor_x = 0
cursor_y = 0

neko = [] #칸을 관리해주는
check = [] #판정용
for i in range(10):
  neko.append([0,0,0,0,0,0,0,0])
  check.append([0,0,0,0,0,0,0,0])


# check = neko

def check_neko():
  for y in range(10):
    for x in range(8):
      check[y][x] = neko[y][x]
  for y in range(1, 9):
    for x in range(8):
      if check[y][x] > 0:
        if check[y-1][x] == check[y][x] == check[y+1][x]:
          neko[y-1][x], neko[y][x], neko[y+1][x] = 7, 7, 7
  for y in range(10):
    for x in range(1, 7):
      if check[y][x] > 0:
        if check[y][x-1] == check[y][x] == check[y][x+1]:
          neko[y][x-1], neko[y][x], neko[y][x+1] = 7, 7, 7
  for y in range(1, 9):
    for x in range(1, 7):
      if check[y][x] > 0:
        if check[y-1][x-1] == check[y][x] == check[y+1][x+1]:
          neko[y-1][x-1], neko[y][x], neko[y+1][x+1] = 7, 7, 7
  for y in range(1, 9):
    for x in range(1, 7):
      if check[y][x] > 0:
        if check[y+1][x-1] == check[y][x] == check[y-1][x+1]:
          neko[y+1][x-1], neko[y][x], neko[y-1][x+1] = 7, 7, 7





def draw_neko():
  cvs.delete("img_cat")
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(24+36+x*72, 24+36+y*72, image = img_neko[neko[y][x]], tag="img_cat")
  #neko리스트를 반복문을 통해서 하나씩확인
  #0보다 큰 값이 들어있다면 해당 위치에 고양이를 그려준

def drop_neko():
  flg = False #낙하를 했는지 안했는지 여부를 알려주는 변수
  for y in range(8, -1, -1): # 8부터 0까지 1씩 감소 아래에서 위로
    for x in range(0, 8, 1) : # 0부터 7까지 1씩 증가 왼쪽에서 오른쪽으
      if neko[y][x] > 0 and neko[y+1][x] == 0:
        neko[y+1][x] = neko[y][x]
        neko[y][x] = 0
        flg = True
  return flg
      # 고양이가 있고, 아래칸이 비었다면
        # 아래 빈칸에 고양이를 넣어주기
        # 원래 고양이가 있던 칸을 비움

# def yoko_neko():
#   for y in range(10):
#     for x in range(1, 7): # 0,8이 아닌 이유?
#       if neko[y][x] > 0:
#         if neko[y][x] == neko[y][x-1] == neko[y][x+1]:
#           neko[y][x], neko[y][x-1], neko[y][x+1] = 7, 7, 7

#   for y in range(1, 9):
#     for x in range(8):
#       if neko[y][x] > 0:
#         if neko[y+1][x] == neko[y][x] == neko[y-1][x]:
#           neko[y+1][x], neko[y][x], neko[y-1][x] = 7, 7, 7
          
      # 가운데를 기준으로 좌우에 같은 고양이가 놓여있다면
          #해당 위치에 고양이 대신 발자국 값을 넣어주기
  

def set_neko():
  # 네코 리스트의 맨 위쪽에 고양이를 랜덤으로 만들어주는 것 (0~6까지)
  # 만들고 setneko와 드로우 함수를 실행했을때 파이썬에 고양이가 만들어져있는지 확인
  for x in range(8):
    num = random.randint(0, difficulty)
    neko[0][x] = num

def mouse_move(e):
  global mouse_x, mouse_y
  mouse_x = e.x
  mouse_y = e.y

def mouse_press(e):
  global mouse_c
  mouse_c = 1
  
def mouse_release(e):
  global mouse_c
  mouse_c = 0

def draw_text(txt, x, y, siz, col, tg):
  fnt = ("Times New Roman", siz, "bold")
  cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
  cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def sweep_neko():
  count = 0
  for y in range(10):
    for x in range(8):
      if neko[y][x] == 7:
        count += 1
        neko[y][x] = 0
  return count

def over_neko():
  isTop = False
  for x in range(8):
    if neko[0][x] > 0:
      isTop = True
  return isTop


def game_main():
  global mouse_x, mouse_y, cursor_x, cursor_y, mouse_c
  global index, timer, score, next, hisc, difficulty

  if index == 0:
    draw_text("야옹야옹", 312, 240, 100, "violet", "TITLE")
    # draw_text("Click To Start !", 312, 500, 50, "orange", "TITLE")
    cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
    draw_text("Easy", 312, 420, 40, "white", "TITLE")
    cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
    draw_text("Normal", 312, 564, 40, "white", "TITLE")
    cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
    draw_text("Hard", 312, 708, 40, "white", "TITLE")
    index = 1
    mouse_c = 0

  elif index == 1:
    difficulty = 0
    if mouse_c == 1:
      if 168 < mouse_x < 456 and 384 < mouse_y < 456:
        difficulty = 4
      elif 168 < mouse_x < 456 and 528 < mouse_y < 600:
        difficulty = 5
      elif 168 < mouse_x < 456 and 672 < mouse_y < 744:
        difficulty = 6
    
    if difficulty > 0 :
      for y in range(10):
        for x in range(8):
          neko[y][x] = 0
      mouse_c, score, next, cursor_x, cursor_y = 0, 0, 0, 0, 0
      set_neko()
      draw_neko()
      cvs.delete("TITLE")
      index = 2

  elif index == 2: #낙하
    if drop_neko() == False:
      index = 3
    draw_neko()

  elif index == 3: #나란히 놓여져 있는가
    check_neko()
    draw_neko()
    index = 4

  elif index == 4: #나란히 놓여져 있는 발자국들을 삭제해준다
    sc = sweep_neko()
    score += sc * difficulty * 2
    if score > hisc:
      hisc = score
    if sc > 0:
      index = 2    
    else:
      if over_neko() == False:
        next = random.randint(1, difficulty)
        index = 5
      else:
        index = 6
        timer = 0
    draw_neko()

  elif index == 5: #마우스 입력 대기 상태
    if 24 <= mouse_x < 24 + 72 * 8 and 24 <= mouse_y < 24 + 72 * 10:
      cursor_x = (mouse_x-24)//72
      cursor_y = (mouse_y-24)//72

      if mouse_c == 1:
        mouse_c = 0
        set_neko()
        neko[cursor_y][cursor_x] = next
        next = 0
        index = 2
    # print(cursor_x, cursor_y)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
  elif index == 6: # 게임 오버
    timer = timer + 1
    if timer == 1:
      draw_text("GAME_OVER", 312, 348, 60, "red", "OVER")
    elif timer == 50:
      cvs.delete("OVER")
      index = 0
  cvs.delete("INFO")
  draw_text("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
  draw_text("HISC" + str(hisc), 450, 60, 32, "yellow", "INFO")

  if next > 0:
    cvs.create_image(752, 128, image=img_neko[next], tag="next")

  # mouse_x와 y의 변수의 값이 게임 판에 있다면
  # 커서 x와 커서 y의 값을 변경해준다
  # mouse의 위치가 사각형 범위 안에 있고 클릭을 헀다면 yoko_neko함수 실행시키기
  # if (mouse_x >= 660 and mouse_x <= 840) and (mouse_y >= 100 and mouse_y <= 160) and mouse_c == 1:
  #   check_neko()

  
  # if (mouse_x <= 24 + 72*8 and mouse_x >= 24) and (mouse_y >=0 and mouse_y <= 24 + 72*10):
  #   cursor_x = (mouse_x - 24) // 72
  #   cursor_y = (mouse_y - 24) // 72
  #   # 만약에 클릭을 했다면
  #   # 커서 위치에 고양이 하나를 무작위로 배치
  # ran = random.randrange(1,7)
  # if mouse_c == 1:
  #   # cvs.create_image(24+36+cursor_x*72, 24+36+cursor_y*72, image=img_neko[ran], tag="nekko")
  #   neko[cursor_y][cursor_x] = ran
    
  # cvs.delete("cursor")
  # cvs.create_image(24+36+cursor_x*72, 24+36+cursor_y*72, image=cursor, tag="cursor")

  # drop_neko() # neko 리스트의 값을 변경해줌
  # cvs.delete("img_cat") # 기존 그려진 고양이를 지워줌
  # draw_neko() # 변경된 neko리스트대로 다시 그려줌
  


  
  # fnt = ("Times New Roman", 30) #font
  # txt = f"mouse({mouse_x}, {mouse_y})" #text
  # cvs.delete("word")
  # cvs.create_text(456, 380, text=txt, font=fnt, tag="word")
  root.after(100, game_main)  





root = tkinter.Tk() 
root.title("Mouse Input")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
cvs = tkinter.Canvas(root, width= 912, height = 768)
cvs.pack()
bg = tkinter.PhotoImage(file="neko_bg.png") #배경 이미지 로밍
cursor = tkinter.PhotoImage(file="neko_cursor.png")

img_neko = [
  None, 
  tkinter.PhotoImage(file="neko1.png"),
  tkinter.PhotoImage(file="neko2.png"),
  tkinter.PhotoImage(file="neko3.png"),
  tkinter.PhotoImage(file="neko4.png"),
  tkinter.PhotoImage(file="neko5.png"),
  tkinter.PhotoImage(file="neko6.png"),
  tkinter.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
# cvs.create_rectangle(660, 100, 840, 160, fill="white")
# cvs.create_text(750, 130, text="test", fill="red",font=("Times New Roman", 30))

game_main()

root.mainloop()

# import copy
# a = [1, 2, 3]
# b = copy.deepcopy(a)
# b = a #reference 같이 공유해준다 한쪽을 바꿔도 동시에 바뀐다
# print(b)
# b[0] = 10
# print(b)
# print(a)