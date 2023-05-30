import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


my_list = LinkedList()

username = input("กรุณากรอกชื่อผู้ใช้: ") #string
password = input("กรุณากรอกรหัสผ่าน: ") #string

if username == "admin" and password == "password":
    print("เข้าสู่ระบบสำเร็จ")
    df = pd.read_excel("data.xlsx")
    for row in df.iterrows():
        index, data = row
        my_list.insert(data.tolist())
    my_list.display()
else:
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
