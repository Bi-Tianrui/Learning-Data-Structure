import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import ctypes

# 适配高分屏
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class DSGrandLab:
    def __init__(self, root):
        self.root = root
        self.root.title("栈与队列算法实验室 - 同济教材第3章专版")
        self.root.geometry("1300x900")
        self.root.configure(bg="#1e1e1e")

        self.is_animating = False
        
        # 教学选项卡
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.setup_sqstack_tab()    # 3.1.1 顺序栈
        self.setup_linkstack_tab()  # 3.1.2 链栈
        self.setup_circular_tab()   # 3.3.3 循环队列
        self.setup_app_tab()        # 3.2 栈的应用: 数制转换

    # ------------------ 工具函数 ------------------
    def create_view(self, parent):
        canvas = tk.Canvas(parent, bg="white", height=400, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        lower_frame = tk.Frame(parent, bg="#2d2d2d", height=250)
        lower_frame.pack(fill=tk.X, padx=10, pady=(0,10))
        
        code_txt = tk.Text(lower_frame, width=70, height=12, bg="#1e1e1e", fg="#d4d4d4", 
                          font=("Consolas", 12), padx=15, pady=15, borderwidth=0)
        code_txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        info_txt = tk.Text(lower_frame, width=40, height=12, bg="#252526", fg="#cccccc", 
                          font=("微软雅黑", 10), padx=15, pady=15, wrap=tk.WORD, borderwidth=0)
        info_txt.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        return canvas, code_txt, info_txt

    def step_msg(self, code_ctrl, info_ctrl, codes, line, msg, delay=0.8):
        code_ctrl.delete(1.0, tk.END)
        info_ctrl.delete(1.0, tk.END)
        for i, c in enumerate(codes):
            tag = "hi" if i == line else "no"
            code_ctrl.insert(tk.END, c + "\n", tag)
        code_ctrl.tag_config("hi", background="#3e3e42", foreground="#dcdcaa")
        info_ctrl.insert(tk.END, f"【执行逻辑】\n{msg}")
        self.root.update()
        if delay > 0: time.sleep(delay)

    # ================== 3.1.1 顺序栈 (SqStack) ==================
    def setup_sqstack_tab(self):
        tab = tk.Frame(self.notebook, bg="#2d2d2d")
        self.notebook.add(tab, text=" 3.1 顺序栈 ")
        
        ctrl = tk.Frame(tab, bg="#333", pady=10)
        ctrl.pack(fill=tk.X)
        self.sqs_val = tk.Entry(ctrl, width=5); self.sqs_val.pack(side=tk.LEFT, padx=10); self.sqs_val.insert(0, "A")
        tk.Button(ctrl, text="Push (入栈)", command=self.sqs_push).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="Pop (出栈)", command=self.sqs_pop).pack(side=tk.LEFT, padx=5)

        self.sqs_data = []
        self.sqs_max = 8
        self.sqs_can, self.sqs_code, self.sqs_info = self.create_view(tab)
        self.draw_sqs()

    def draw_sqs(self, hi_line=-1):
        self.sqs_can.delete("all")
        bx, by, w, h = 550, 350, 120, 40
        # 绘制容器
        self.sqs_can.create_line(bx, by-320, bx, by, width=3)
        self.sqs_can.create_line(bx+w, by-320, bx+w, by, width=3)
        self.sqs_can.create_line(bx, by, bx+w, by, width=3)
        
        # 绘制栈底 base
        self.sqs_can.create_text(bx-40, by, text="base", fill="blue", font=("Consolas", 10, "bold"))
        
        # 绘制数据
        for i, val in enumerate(self.sqs_data):
            color = "#e3f2fd" if i != hi_line else "#ffeb3b"
            self.sqs_can.create_rectangle(bx+2, by-i*h-2, bx+w-2, by-(i+1)*h+2, fill=color, outline="#1976d2")
            self.sqs_can.create_text(bx+w/2, by-i*h-h/2, text=str(val), font=("Arial", 12, "bold"))

        # 绘制 top 指针 (PPT 第 7 页: 指向栈顶元素的下一个位置)
        top_idx = len(self.sqs_data)
        self.sqs_can.create_line(bx+w+50, by-top_idx*h-h/2, bx+w+5, by-top_idx*h-h/2, arrow=tk.LAST, fill="red", width=2)
        self.sqs_can.create_text(bx+w+70, by-top_idx*h-h/2, text="top", fill="red", font=("Consolas", 12, "bold"))

    def sqs_push(self):
        codes = ["Status Push(SqStack &S, SElemType e) {", "  if (S.top - S.base >= S.stacksize) return ERROR;", "  *S.top++ = e;", "  return OK; }"]
        if len(self.sqs_data) >= self.sqs_max:
            self.step_msg(self.sqs_code, self.sqs_info, codes, 1, "检测到栈满（上溢 Overflow）！无法继续入栈。")
            return
        val = self.sqs_val.get()
        self.step_msg(self.sqs_code, self.sqs_info, codes, 2, f"执行 *S.top = {val}; S.top++;\n数据存入当前 top 指向位置，指针上移。")
        self.sqs_data.append(val)
        self.draw_sqs(len(self.sqs_data)-1)

    def sqs_pop(self):
        codes = ["Status Pop(SqStack &S, SElemType &e) {", "  if (S.top == S.base) return ERROR;", "  e = *--S.top;", "  return OK; }"]
        if not self.sqs_data:
            self.step_msg(self.sqs_code, self.sqs_info, codes, 1, "检测到栈空（下溢 Underflow）！")
            return
        self.step_msg(self.sqs_code, self.sqs_info, codes, 2, "执行 S.top--; e = *S.top;\ntop 指针先下移，然后取出数据。")
        self.draw_sqs(len(self.sqs_data)-1)
        time.sleep(0.5)
        self.sqs_data.pop()
        self.draw_sqs()

    # ================== 3.3.3 循环队列 (SqQueue) ==================
    def setup_circular_tab(self):
        tab = tk.Frame(self.notebook, bg="#2d2d2d")
        self.notebook.add(tab, text=" 3.3 循环队列 ")
        
        ctrl = tk.Frame(tab, bg="#333", pady=10)
        ctrl.pack(fill=tk.X)
        self.q_val = tk.Entry(ctrl, width=5); self.q_val.pack(side=tk.LEFT, padx=10); self.q_val.insert(0, "10")
        tk.Button(ctrl, text="EnQueue (入队)", command=self.q_en).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="DeQueue (出队)", command=self.q_de).pack(side=tk.LEFT, padx=5)

        self.q_max = 6 # 实际存储 5 个，浪费 1 个空间 (PPT 61页)
        self.q_data = [None] * self.q_max
        self.front = 0
        self.rear = 0
        self.q_can, self.q_code, self.q_info = self.create_view(tab)
        self.draw_q()

    def draw_q(self):
        self.q_can.delete("all")
        cx, cy, r = 500, 200, 120
        # 绘制圆形阵列
        for i in range(self.q_max):
            import math
            angle = i * (360 / self.q_max) - 90
            rad = math.radians(angle)
            x, y = cx + r * math.cos(rad), cy + r * math.sin(rad)
            
            fill = "#e8f5e9"
            if i == self.front: fill = "#bbdefb" # front 蓝色
            if i == self.rear: fill = "#ffcdd2"  # rear 红色
            if i == self.front and i == self.rear: fill = "#e1bee7" # 重合
            
            self.q_can.create_oval(x-35, y-35, x+35, y+35, fill=fill, width=2)
            val = self.q_data[i]
            if val is not None:
                self.q_can.create_text(x, y, text=str(val), font=("Arial", 14, "bold"))
            self.q_can.create_text(x, y+45, text=f"[{i}]", fill="gray")
            
            # 绘制指针文字
            if i == self.front: self.q_can.create_text(x, y-55, text="front", fill="blue", font=("Arial", 10, "bold"))
            if i == self.rear: self.q_can.create_text(x, y-70, text="rear", fill="red", font=("Arial", 10, "bold"))

        self.q_can.create_text(cx, cy, text=f"Length: {(self.rear-self.front+self.q_max)%self.q_max}", font=("Consolas", 12))

    def q_en(self):
        codes = ["Status EnQueue(SqQueue &Q, QElemType e) {", "  if ((Q.rear+1) % MAXSIZE == Q.front) return ERROR;", "  Q.base[Q.rear] = e;", "  Q.rear = (Q.rear + 1) % MAXSIZE;", "  return OK; }"]
        if (self.rear + 1) % self.q_max == self.front:
            self.step_msg(self.q_code, self.q_info, codes, 1, "队列满！(rear+1)%MAX == front。\n注意：循环队列通常浪费一个空间以区分空/满。")
            return
        val = self.q_val.get()
        self.q_data[self.rear] = val
        self.step_msg(self.q_code, self.q_info, codes, 2, f"数据 {val} 存入 rear 指向的槽位 [{self.rear}]。")
        self.draw_q()
        time.sleep(0.6)
        self.rear = (self.rear + 1) % self.q_max
        self.step_msg(self.q_code, self.q_info, codes, 3, "rear 指针模运算后移：rear = (rear + 1) % MAXSIZE")
        self.draw_q()

    def q_de(self):
        codes = ["Status DeQueue(SqQueue &Q, QElemType &e) {", "  if (Q.front == Q.rear) return ERROR;", "  e = Q.base[Q.front];", "  Q.front = (Q.front + 1) % MAXSIZE;", "  return OK; }"]
        if self.front == self.rear:
            self.step_msg(self.q_code, self.q_info, codes, 1, "队列空！front == rear。")
            return
        val = self.q_data[self.front]
        self.q_data[self.front] = None
        self.step_msg(self.q_code, self.q_info, codes, 2, f"取出 front 指向的数据 {val}。")
        self.draw_q()
        time.sleep(0.6)
        self.front = (self.front + 1) % self.q_max
        self.step_msg(self.q_code, self.q_info, codes, 3, "front 指针模运算后移：front = (front + 1) % MAXSIZE")
        self.draw_q()

    # ================== 3.2 栈的应用: 数制转换 ==================
    def setup_app_tab(self):
        tab = tk.Frame(self.notebook, bg="#2d2d2d")
        self.notebook.add(tab, text=" 3.2 应用: 数制转换 ")
        
        ctrl = tk.Frame(tab, bg="#333", pady=10)
        ctrl.pack(fill=tk.X)
        tk.Label(ctrl, text="十进制 N:", bg="#333", fg="white").pack(side=tk.LEFT, padx=10)
        self.n_val = tk.Entry(ctrl, width=8); self.n_val.pack(side=tk.LEFT); self.n_val.insert(0, "13")
        tk.Button(ctrl, text="开始转换 (Binary)", command=self.ani_conversion).pack(side=tk.LEFT, padx=20)

        self.app_can, self.app_code, self.app_info = self.create_view(tab)
        self.app_stack = []

    def draw_app(self, result=""):
        self.app_can.delete("all")
        bx, by, w, h = 300, 350, 80, 30
        # 绘制栈
        self.app_can.create_rectangle(bx, by-250, bx+w, by, width=2)
        self.app_can.create_text(bx+w/2, by+20, text="Stack S")
        for i, v in enumerate(self.app_stack):
            self.app_can.create_rectangle(bx+2, by-i*h-2, bx+w-2, by-(i+1)*h+2, fill="#fff9c4")
            self.app_can.create_text(bx+w/2, by-i*h-h/2, text=str(v))
        
        # 结果显示
        self.app_can.create_text(600, 200, text=f"Binary Result: {result}", font=("Consolas", 24, "bold"), fill="green")

    def ani_conversion(self):
        codes = ["while (N) {", "  Push(S, N % 2);", "  N = N / 2; }", "while (!EmptyStack(S)) {", "  Pop(S, e); print(e); }"]
        try:
            n = int(self.n_val.get())
            self.app_stack = []
            temp_n = n
            # 第一阶段：入栈
            while temp_n > 0:
                rem = temp_n % 2
                self.step_msg(self.app_code, self.app_info, codes, 1, f"计算 {temp_n} % 2 = {rem}，余数入栈。")
                self.app_stack.append(rem)
                self.draw_app()
                temp_n //= 2
                self.step_msg(self.app_code, self.app_info, codes, 2, f"更新 N = {temp_n}。")
                time.sleep(0.8)
            
            # 第二阶段：出栈
            res_str = ""
            while self.app_stack:
                e = self.app_stack.pop()
                res_str += str(e)
                self.step_msg(self.app_code, self.app_info, codes, 4, f"出栈取值：{e}。栈顶元素先弹出，它是高位。")
                self.draw_app(res_str)
                time.sleep(0.8)
        except: pass

    # ================== 3.1.2 链栈 (LinkStack) ==================
    def setup_linkstack_tab(self):
        tab = tk.Frame(self.notebook, bg="#2d2d2d")
        self.notebook.add(tab, text=" 3.1.2 链栈 ")
        ctrl = tk.Frame(tab, bg="#333", pady=10)
        ctrl.pack(fill=tk.X)
        self.ls_val = tk.Entry(ctrl, width=5); self.ls_val.pack(side=tk.LEFT, padx=10); self.ls_val.insert(0, "X")
        tk.Button(ctrl, text="Push (入栈)", command=self.ls_push).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="Pop (出栈)", command=self.ls_pop).pack(side=tk.LEFT, padx=5)
        self.ls_can, self.ls_code, self.ls_info = self.create_view(tab)
        self.ls_data = [] # 模拟不带头结点的链表
        self.draw_ls()

    def draw_ls(self):
        self.ls_can.delete("all")
        x, y, w, h, gap = 150, 200, 80, 45, 50
        # 栈顶指针 top
        self.ls_can.create_text(x-70, y+h/2, text="top", fill="red", font=("Arial", 12, "bold"))
        if not self.ls_data:
            self.ls_can.create_line(x-40, y+h/2, x, y+h/2, arrow=tk.LAST, fill="red")
            self.ls_can.create_text(x+20, y+h/2, text="NULL", fill="red")
        else:
            self.ls_can.create_line(x-40, y+h/2, x, y+h/2, arrow=tk.LAST, fill="red")
            for i, val in enumerate(self.ls_data):
                curr_x = x + i * (w + gap)
                self.ls_can.create_rectangle(curr_x, y, curr_x+w, y+h, fill="#fff9c4", width=2)
                self.ls_can.create_text(curr_x+w/2, y+h/2, text=str(val))
                if i < len(self.ls_data)-1:
                    self.ls_can.create_line(curr_x+w, y+h/2, curr_x+w+gap, y+h/2, arrow=tk.LAST)
                else:
                    self.ls_can.create_text(curr_x+w+30, y+h/2, text="^", font=("Arial", 16))

    def ls_push(self):
        codes = ["p = new SNode; p->data = e;", "p->next = s; // 连向旧栈顶", "s = p;      // 指针移动到新节点"]
        val = self.ls_val.get()
        self.step_msg(self.ls_code, self.ls_info, codes, 1, f"创建新节点 {val}，让其 next 指向当前的 top 节点。")
        self.ls_data.insert(0, val)
        self.draw_ls()
        self.step_msg(self.ls_code, self.ls_info, codes, 2, "更新 top 指针，使其指向新的表头。")

    def ls_pop(self):
        codes = ["if (!s) return ERROR;", "e = s->data; p = s;", "s = s->next; free(p);"]
        if not self.ls_data: return
        self.step_msg(self.ls_code, self.ls_info, codes, 2, f"准备弹出栈顶 {self.ls_data[0]}。")
        time.sleep(0.6)
        self.ls_data.pop(0)
        self.draw_ls()
        self.step_msg(self.ls_code, self.ls_info, codes, 2, "top 指针移向下一个节点，原栈顶空间释放。")

if __name__ == "__main__":
    root = tk.Tk()
    app = DSGrandLab(root)
    root.mainloop()