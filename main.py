import tkinter as tk
import tkinter.font as tkFont

ans = ""
sub_win = None
result_label = None

def start_game():
    global sub_win
    global questions
    sub_win = tk.Toplevel()
    sub_win.geometry("400x300")
    sub_label = tk.Label(sub_win, text="下記に単語を記入してください \n 回答が分かったら「答える」のボタンを押してください。")
    sub_label.pack()
    global ans
    ans = tk.Entry(sub_win)
    ans.pack()
    level=level_var.get() 
    button = tk.Button(sub_win, text="答える", command=get_info)
    button.pack()

    if level=="easy":
        questions={
            "エネルギー": "energy",
            "条件、コンディション": "condition",
            "階段": "stairs",
            "インフルエンザ":"flu",
            "祝う":"celebrate",
            "残る":"remain",
            "デザインする":"design",
            "準備する":"prepare",
            "達成、功績":"achieve",
            "関係":"relationship",
            "資源":"resource",
        }

    elif level == "medium":
        questions = {
            "核の、原子力の": "nuclear",
            "柔軟な": "flexible	",
            "国内の、家庭の":"domestic",
            "不審な":"suspicious",
            "態度":"attitude",
            "意気消沈した":"depressed",
            "明らかな":"obvious",
            "能力がある":"capable",
            "有能な、効率のよい":"efficient",
            "応用、申し込み":"application",
        }
    else:
        questions = {
            "青年期": "adolescence",
            "回避": "evasion",
            "誠実さ":"sincerity",
            "再開する":"resume",  
            "提携させる":"affiliate",
            "閉じ込める":"confine",
            "不十分な":"insufficient",
            "抑えがたい、抵抗できない":"irresistible"
        }
    display_question()

def display_question():
    global sub_win
    global word
    global question_index
    global questions

    question = list(questions.items())[question_index]  # 現在の問題を取得する
    if question_index == 0:
        word = tk.Label(sub_win, text=question[0])
        word.pack()
    else:
        word.config(text=question[0])  # 問題を更新する


def get_info():
    global ans
    global sub_win
    global result_label
    global question_index
    global questions

    if result_label:
        result_label.destroy()

    output = ans.get()
    question = list(questions.items())[question_index]
    if output == question[1]:
        result_label = tk.Label(sub_win, text="正解",fg="green")
        question_index += 1  # 次の問題に進む
        ans.delete(0, 'end')
        if question_index < len(questions):  # 問題が残っている場合は、問題を更新する
            display_question()
        else:
            end_call=tk.Label(sub_win,text="終了！お疲れ様でした。")
            end_call.pack()
            word.pack_forget()
            result_label.pack_forget()

    else:
        result_label = tk.Label(sub_win, text="不正解",fg="red")
    result_label.pack(padx=5,pady=10)




question_index = 0  # 最初の問題から始める

root = tk.Tk()
root.title("")
root.geometry("400x300")
font_style = tkFont.Font(size=20, weight="bold")
title_label = tk.Label(root, text="単語学習アプリ",font=font_style)
title_label.pack()
level_var = tk.StringVar()
level_var.set("easy")
easy_btn = tk.Radiobutton(root, text="Easy", variable=level_var, value="easy")
medium_btn = tk.Radiobutton(root, text="Medium", variable=level_var, value="medium")
hard_btn = tk.Radiobutton(root, text="Hard", variable=level_var, value="hard")
easy_btn.pack()
medium_btn.pack()
hard_btn.pack()
start_btn = tk.Button(root, text="Start", command=start_game)
start_btn.pack()

root.mainloop()
