from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import os

''' ''' ''' ''' ''' ''' ''' 함수 ''' ''' ''' ''' ''' ''' '''
#로그인 함수
def login():
    if id_ent.get() == "skku" and pw_ent.get() == "1234": #로그인 성공
        login_window.destroy()
        
        #메인메뉴 창 생성
        global main_window
        main_window = Tk()
        main_window.geometry("500x620+700+120")
        main_window.title("ㅇㅇㅌㄷ | 메인 화면")
        main_window.resizable(False,False)
        main_bg = get_list("bg",500,620)
        bg_label = Label(main_window, image=main_bg[1])

        #위젯
        btn_closet = Button(main_window, width = 30, text="옷장 열기",font=("바탕",12), 
                              fg = "deeppink", bg = "pink", command =closet_category)
        btn_do_cody = Button(main_window, width = 30,text="코디하기",font=("바탕",12),
                             fg = "deeppink", bg = "pink",command=run_cody)
        btn_my_cody = Button(main_window, width = 30,text="나만의 코디",font=("바탕",12),
                             fg = "deeppink", bg = "pink",command=show_savecody)
        #위젯 배치
        btn_closet.place(x=100, y=150)
        btn_do_cody.place(x=100, y=300)
        btn_my_cody.place(x=100, y=450)
        bg_label.place(x=0,y=0)

        main_window.mainloop()

    else: #로그인 실패
        messagebox.showinfo("로그인 실패","잘못된 정보입니다.")
        id_ent.delete(0, "end")
        pw_ent.delete(0, "end")

#리스트초기화함수: 옷  종류별로 입력받은 사이즈의 이미지로 구성된 리스트를 반환
def get_list(clothes_name,width,height):
    route =  os.path.dirname(os.path.realpath(__file__))+"\\"+clothes_name+"\\" #이미지 폴더의 경로를 route 변수에 저장

    file_list = os.listdir(route) 
    clothes_list = [x for x in file_list if(x.endswith(".PNG")
                                          or (x.endswith(".png")==True))] #route에 있는 사진 파일의 이름으로 구성된 clothes_list생성

    image_list = [] #PhotoImage 가 저장될 리스트
    i = 0
    while i < len(clothes_list):
        img_open = Image.open(route+clothes_list[i])
        resize_img = img_open.resize((width,height)) #사진 사이즈 조절
        reimg = ImageTk.PhotoImage(resize_img)
        image_list.append(reimg) #image_list에 사이즈가 조절된 이미지를 하나씩 append시킴
        i+=1
        
    return image_list #이미지 리스트 반환

''' ''' ''' ''' ''' ''' ''' 옷장 함수 ''' ''' ''' ''' ''' ''' '''
#옷장 열기 버튼 클릭 시 실행되는 함수
def closet_category():
    global dresser_toplevel
    #옷장열기 윈도우
    dresser_toplevel = Toplevel(main_window)
    dresser_toplevel.geometry("500x620+700+120")
    dresser_toplevel.resizable(False,False)
    dresser_toplevel.title("ㅇㅇㅌㄷ | 옷장 열기")
    dresser_bg = get_list("bg",500,620)
    bg_label = Label(dresser_toplevel,image=dresser_bg[2])
           
    #위젯
    btn_top = Button(dresser_toplevel, text="상의",width = 20, font=("바탕",12), fg = "lavenderblush",
                     bg = "hotpink",command = lambda: show_closet("top"))
    btn_bottom = Button(dresser_toplevel, text="하의",width = 20, font=("바탕",12), fg = "lavenderblush",
                     bg = "hotpink",command = lambda: show_closet("bottom"))
    btn_outer = Button(dresser_toplevel, text="아우터",width = 20, font=("바탕",12), fg = "lavenderblush",
                     bg = "hotpink",command = lambda: show_closet("outer"))
    btn_shoes = Button(dresser_toplevel, text="신발",width = 20, font=("바탕",12), fg = "lavenderblush",
                     bg = "hotpink",command = lambda: show_closet("shoes"))

    #위젯 배치
    btn_top.place(x=140, y=120)
    btn_bottom.place(x=140, y=240)
    btn_outer.place(x=140, y=360)
    btn_shoes.place(x=140, y=480)
    bg_label.place(x=0,y=0)

    dresser_toplevel.mainloop()

#카테고리 선택 하면 옷장을 보여주는 함수
def show_closet(clothes_name):
    image_list = get_list(clothes_name, 150, 150) #리스트 초기화 함수로 옷 리스트 생성
    row = 0 #사진 배치 관련 변수
    column = 0 #사진 배치 관련 변수
    
    if len(image_list) == 0: #옷 폴더에 사진이 없으면
        messagebox.showinfo("알림","옷장에 옷이 없습니다.")

    else: #옷 폴더에 사진이 있으면
        #옷장 윈도우
        closet_toplevel = Toplevel(dresser_toplevel)
        closet_toplevel.resizable(False,False)
        closet_toplevel.title("ㅇㅇㅌㄷ | 옷장 열기")
        closet_toplevel.geometry("500x620+700+120")
        closet_toplevel.config(bg='lavenderblush')
        
        for i in range(len(image_list)): #옷 리스트의 길이만큼
            #옷 배치: column이 3이 되면 다음 row로 넘어가게 함
            if column != 3:
                lab_image = Label(closet_toplevel, image=image_list[i])
                lab_image.grid(row=row, column=column)
                column += 1
            else:
                row+=1
                column = 0
                lab_image = Label(closet_toplevel, image=image_list[i])
                lab_image.grid(row=row, column=column)
                column+=1

        closet_toplevel.mainloop()

''' ''' ''' ''' ''' ''' ''' 코디하기 함수 ''' ''' ''' ''' ''' ''' '''
#코디하기 화면 설정 함수
def run_cody():
    global cody_win
    global outer_label, top_label, bottom_label, shoes_label
    global top_list, bottom_list, outer_list, shoes_list
    
    #이미지 리스트 생성 
    top_list = get_list("top", 200, 200)
    bottom_list = get_list("bottom", 200, 200)
    outer_list = get_list("outer", 200, 200)
    shoes_list = get_list("shoes", 200, 200)

    if len(top_list)==0 or len(bottom_list)==0 or len(outer_list)==0 or len(shoes_list)==0: #옷 폴더 중 비어있는 폴더가 있으면
        messagebox.showinfo("알림","옷장 속 모든 카테고리에 옷이 있는지 확인해주세요.")

    else:#모든 옷 폴더에 사진이 있으면
        #코디하기 윈도우
        cody_win = Toplevel(main_window)
        cody_win.title("ㅇㅇㅌㄷ | 코디하기")
        cody_win.geometry("500x620+700+120")
        cody_win.resizable(False,False)
        cody_bg = get_list("bg",500,620)
        bg_label = Label(cody_win,image=cody_bg[3])
        
        #위젯
        outer_label = Label(cody_win, image=outer_list[0])
        top_label = Label(cody_win, image=top_list[0])
        bottom_label = Label(cody_win, image=bottom_list[0])
        shoes_label = Label(cody_win, image=shoes_list[0])

        random_btn = Button(cody_win,text='랜덤 코디',width=15,font = ("바탕",12), bg="deeppink"
                            ,fg = "lavenderblush", command=random_cody)
        save_btn = Button(cody_win,text='저장하기',width=15,font=("바탕",12), bg="orchid", fg = "lavenderblush"
                            ,command=save_cody)
        
        outer_next_btn = Button(cody_win, text="▶",font=11, bg="thistle", fg = "mediumorchid"
                                ,command=lambda:next_image(outer_label,outer_list,"outer"), relief="groove")
        outer_previous_btn = Button(cody_win, text="◀",font=11, bg="thistle", fg = "mediumorchid"
                                   ,command=lambda:previous_image(outer_label,outer_list,"outer"),relief="groove")

        top_next_btn = Button(cody_win, text="▶",font=11, bg="thistle", fg = "mediumorchid"
                              ,command=lambda:next_image(top_label,top_list,"top"),relief="groove")
        top_previous_btn = Button(cody_win, text="◀",font=11, bg="thistle", fg = "mediumorchid"
                                 ,command=lambda:previous_image(top_label,top_list,"top"),relief="groove")

        bottom_next_btn = Button(cody_win, text="▶",font=11, bg="thistle", fg = "mediumorchid"
                                 ,command=lambda:next_image(bottom_label,bottom_list,"bottom"),relief="groove")
        bottom_previous_btn = Button(cody_win, text="◀",font=11, bg="thistle", fg = "mediumorchid"
                                    ,command=lambda:previous_image(bottom_label,bottom_list,"bottom"),relief="groove")

        shoes_next_btn = Button(cody_win, text="▶",font=11, bg="thistle", fg = "mediumorchid"
                                ,command=lambda:next_image(shoes_label,shoes_list,"shoes"),relief="groove")
        shoes_previous_btn = Button(cody_win, text="◀",font=11,bg="thistle", fg = "mediumorchid"
                                   ,command=lambda:previous_image(shoes_label,shoes_list,"shoes"),relief="groove")

        #위젯 배치
        bg_label.place(x=0,y=0)
        top_label.grid(row=0, column=0, columnspan=2,
                       padx=(40,10), pady=(20,0))
        bottom_label.grid(row=2, column=0, columnspan=2,
                          padx=(40,10), pady=(15,0))
        outer_label.grid(row=0,column=2, columnspan=2,
                         padx=(10,30), pady=(20,0))
        shoes_label.grid(row=2,column=2, columnspan=2,
                          padx=(10,30), pady=(15,0))

        top_next_btn.grid(row=1, column=1, sticky="ne",
                          padx=10)
        top_previous_btn.grid(row=1, column=0, sticky="nw",
                             padx=40)

        bottom_next_btn.grid(row=3, column=1, sticky="ne",
                             padx=10)
        bottom_previous_btn.grid(row=3, column=0, sticky="nw",
                                padx=40)

        outer_next_btn.grid(row=1, column=3, sticky="ne",
                            padx=30)
        outer_previous_btn.grid(row=1, column=2, sticky="nw",
                               padx=10)

        shoes_next_btn.grid(row=3, column=3, sticky="ne",
                            padx=30)
        shoes_previous_btn.grid(row=3, column=2, sticky="nw",
                               padx=10)

        random_btn.grid(row=4, columnspan=4, pady=15)
        save_btn.grid(row=5, columnspan=4, pady =(0,5))

        cody_win.mainloop()

#다음 버튼이 눌렸을 때  사진 바꾸는 함수
def next_image(label_img,pick_img,index): #사진을 보여줄 라벨, 이미지 리스트, 어떤 버튼이 클릭됐는지 알려줄 인덱스를 매개변수로 받음
    global top_index, bottom_index, outer_index, shoes_index, save_index

    if index != "save": #코디하기 화면에서 버튼클릭할 경우
        if index == "top": #아래 4개의 조건문에서 해당하는 인덱스를 변경해줌
            top_index += 1
            index = top_index
            if ( index >= len(pick_img) ) :
                index = top_index = 0   
        elif index == "bottom":
            bottom_index += 1
            index = bottom_index
            if ( index >= len(pick_img) ) :
                index = bottom_index = 0            
        elif index == "outer":
            outer_index += 1
            index = outer_index
            if ( index >= len(pick_img) ) :
                index = outer_index = 0           
        elif index == "shoes":
            shoes_index += 1
            index = shoes_index
            if ( index >= len(pick_img) ) :
                index = shoes_index = 0
        label_img.config(image=pick_img[index]) #변경한 인덱스로 라벨에 이미지띄움

    elif index == "save": #나만의 코디 화면에서 버튼 클릭할 경우
        save_index += 1 #인덱스 변경
        index = save_index
        if(index >= len(pick_img)):
            index = save_index = 0
        for i in range(4): #4개의 라벨에 이미지 띄우기
            label_img[i].config(image=pick_img[save_index][i])

#이전 버튼이 눌렸을 때  사진 바꾸는 함수
def previous_image(label_img,pick_img,index): #사진을 보여줄 라벨, 이미지 리스트, 어떤 버튼이 클릭됐는지 알려줄 인덱스를 매개변수로 받음
    global top_index, bottom_index, outer_index, shoes_index, save_index

    if index != "save": #코디하기 화면에서 버튼클릭할 경우
        if index == "top": #아래 4개의 조건문에서 해당하는 인덱스를 변경해줌
            top_index -= 1
            index = top_index
            if ( index < 0 ) :
                index = top_index = len(pick_img)-1        
        elif index == "bottom":
            bottom_index -= 1
            index = bottom_index
            if ( index < 0 ) :
                index = bottom_index = len(pick_img)-1            
        elif index == "outer":
            outer_index -= 1
            index = outer_index
            if ( index < 0 ) :
                index = outer_index = len(pick_img)-1            
        elif index == "shoes":
            shoes_index -= 1
            index = shoes_index
            if ( index < 0 ) :
                index = shoes_index = len(pick_img)-1
        label_img.config(image=pick_img[index]) #변경한 인덱스로 라벨에 이미지띄움

    elif index == "save": #나만의 코디 화면에서 버튼 클릭할 경우
        save_index -= 1 #인덱스 변경
        index = save_index
        if(index < 0):
            index = save_index = len(pick_img)-1
        for i in range(4): #4개의 라벨에 이미지 띄우기
            label_img[i].config(image=pick_img[save_index][i])
        
#랜덤 함수
def random_cody():
    global top_index, bottom_index, outer_index, shoes_index
    #사진 인덱스를 랜덤으로 설정
    outer_index = random.randint(0, len(outer_list)-1)
    top_index = random.randint(0, len(top_list)-1)
    bottom_index = random.randint(0, len(bottom_list)-1)
    shoes_index =  random.randint(0, len(shoes_list)-1)

    #랜덤하게 설정한 사진 보여주기
    outer_label.configure(image=outer_list[outer_index])
    top_label.configure(image=top_list[top_index])
    bottom_label.configure(image=bottom_list[bottom_index])
    shoes_label.configure(image=shoes_list[shoes_index])

''' ''' ''' ''' ''' ''' ''' 저장 기능''' ''' ''' ''' ''' ''' '''
#저장하기 버튼 눌렀을 때 실행되는 함수
def save_cody():
    #현재 코디하기 화면에 보여지는 사진으로 리스트 생성
    showing_cody = [top_list[top_index], bottom_list[bottom_index],
                      outer_list[outer_index], shoes_list[shoes_index]]
    
    if showing_cody in save_list: #이미 저장된 코디를 다시 저장하려 한다면
        messagebox.showinfo("알림","이미 저장된 코디입니다.")#이미 저장됐다는 알림 출력
    else: #새로운 코디라면
        save_list.append(showing_cody) #save_list에 저장

#나만의 코디 버튼을 눌렀을 때
def show_savecody():
    if len(save_list) == 0: #저장된 코디가 없을 경우 메시지 출력
        messagebox.showinfo("알림","아직 저장된 코디가 없습니다.")
    else:
        #나만의 코디 윈도우
        savecody_win = Toplevel(main_window)
        savecody_win.title("ㅇㅇㅌㄷ | 나만의 코디")
        savecody_win.geometry("550x620+700+120")
        savecody_win.resizable(False,False)
        save_bg = get_list("bg",550,620)
        bg_label = Label(savecody_win,image=save_bg[3])
                
        #위젯
        save_top_label = Label(savecody_win, image = save_list[0][0])
        save_bottom_label = Label(savecody_win, image = save_list[0][1])
        save_outer_label = Label(savecody_win, image = save_list[0][2])
        save_shoes_label = Label(savecody_win, image = save_list[0][3])
        save_label_list = [save_top_label,save_bottom_label,save_outer_label,save_shoes_label]
        
        save_next_btn = Button(savecody_win, width = 15, font=12, text="▷", bg="orchid", fg = "lavenderblush"
                               ,command=lambda:next_image(save_label_list,save_list,"save"),relief="groove")
        save_previous_btn = Button(savecody_win, width = 15,font=12, text="◁", bg="orchid", fg = "lavenderblush"
                                   ,command = lambda:previous_image(save_label_list,save_list,"save"),relief="groove")
        
        #위젯 배치
        bg_label.place(x=0,y=0)

        save_top_label.grid(row=0, column=0, padx=(35,10), pady=(40,0))
        save_bottom_label.grid(row=1, column=0, padx=(35,10), pady=(15,0))
        save_outer_label.grid(row=0,column=1, padx=(10,35), pady=(40,0))
        save_shoes_label.grid(row=1,column=1, padx=(10,35), pady=(15,0))

        save_previous_btn.grid(row=2, column=0, padx=35, pady = 30)
        save_next_btn.grid(row=2, column=1, padx=35, pady=30)
        
        savecody_win.mainloop()
        
''' ''' ''' ''' ''' ''' ''' 변수 ''' ''' ''' ''' ''' ''' '''
top_index=bottom_index=outer_index=shoes_index = save_index = 0
save_list = []

''' ''' ''' ''' ''' 메인 코드''' ''' ''' ''' ''' ''' ''' 
#로그인 윈도우
login_window = Tk()
bg_list = get_list("bg",500,620)
login_window.geometry("500x620+700+120")
login_window.title("ㅇㅇㅌㄷ | 로그인")
login_window.resizable(False,False)

#위젯
bg_label = Label(login_window, image=bg_list[0])
id_lab = Label(login_window, width = 7, text="ID", font=("courier",12), bg="hotpink", fg="lavenderblush")
pw_lab = Label(login_window, width = 7,text="PW", font = ('courier',12), bg="hotpink", fg="lavenderblush")
id_ent = Entry(login_window, width = 20,font = ("courier",12), fg = "deeppink")
pw_ent = Entry(login_window, width = 20,font = ("courier",12), fg = "deeppink")
pw_ent.config(show="*")
login_btn = Button(login_window, width = 28, text="로그인", font=("바탕",12), command=login, bg="lavenderblush", fg="deeppink")

#위젯 배치
bg_label.place(x=0, y=0)
id_lab.place(x=111, y=513)
pw_lab.place(x=111, y=538)
id_ent.place(x=191, y=513)
pw_ent.place(x=191, y=538)
login_btn.place(x=109, y=570)

login_window.mainloop()
