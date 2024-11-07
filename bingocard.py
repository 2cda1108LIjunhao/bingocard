import tkinter as tk
import random

class BingoCard:
    def __init__(self):
        self.grid_size = 5
        self.bingo_card = self.generate_unique_card()
        self.selected = [[False] * self.grid_size for _ in range(self.grid_size)]
    
    def generate_unique_card(self):
        """生成唯一的宾果卡，遵循宾果数字分布规则。"""
        card = []
        columns = [
            random.sample(range(1, 16), self.grid_size),
            random.sample(range(16, 31), self.grid_size),
            random.sample(range(31, 46), self.grid_size),
            random.sample(range(46, 61), self.grid_size),
            random.sample(range(61, 76), self.grid_size),
        ]
        
        # 将列插入到行中，形成5x5的网格
        for i in range(self.grid_size):
            row = [columns[j][i] for j in range(self.grid_size)]
            card.append(row)
        
        # 将中心位置设为“免费”格子
        card[2][2] = "FREE"
        return card

    def toggle_selection(self, row, col):
        """切换选择宾果卡中的单元格。"""
        if self.bingo_card[row][col] != "FREE":
            self.selected[row][col] = not self.selected[row][col]

    def check_bingo(self):
        """检查是否有行、列或对角线完成宾果。"""
        # 检查行和列
        for i in range(self.grid_size):
            if all(self.selected[i]):  # 行
                return True
            if all(self.selected[j][i] for j in range(self.grid_size)):  # 列
                return True

        # 检查对角线
        if all(self.selected[i][i] for i in range(self.grid_size)) or all(self.selected[i][self.grid_size - 1 - i] for i in range(self.grid_size)):
            return True

        return False

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Card Generator Ver.1")
        self.card = BingoCard()
        self.buttons = [[None for _ in range(5)] for _ in range(5)]
        self.create_bingo_grid()
    
    def create_bingo_grid(self):
        """根据宾果卡创建按钮网格。"""
        for i in range(5):
            for j in range(5):
                value = self.card.bingo_card[i][j]
                button = tk.Button(self.root, text=value, width=6, height=3, command=lambda i=i, j=j: self.toggle_button(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button
    
    def toggle_button(self, row, col):
        """切换按钮外观并检查宾果。"""
        self.card.toggle_selection(row, col)
        if self.card.selected[row][col]:
            self.buttons[row][col].config(bg="lightgreen")
        else:
            self.buttons[row][col].config(bg="SystemButtonFace")
        
        # 检查是否达成宾果
        if self.card.check_bingo():
            self.show_bingo_message()

    def show_bingo_message(self):
        """显示宾果成功消息。"""
        bingo_message = tk.Label(self.root, text="Bingo!", font=("Arial", 20), fg="red")
        bingo_message.grid(row=6, columnspan=5, pady=10)

# 创建主窗口并运行Bingo GUI
root = tk.Tk()
app = BingoApp(root)
root.mainloop()
