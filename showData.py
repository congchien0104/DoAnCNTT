from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


 
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    # Functio to insert a new node at the beginning 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
  
    # This function is in LinkedList class. Inserts a 
    # new node after the given prev_node. This method is 
    # defined inside LinkedList class shown above */
    def insertBefore(self, given_ptr, new_data): 
  
        if (self.head == given_ptr):
  
            # Create a node
            n = Node(new_data)
      
            # Point to next to current head
            n.next = self.head;
      
            # Update the head pointer
            self.head = n;
          
            # Otherwise traverse the list to
            # find previous node of given node
        else:
      
            p = None
            n = self.head;
      
            # This loop will return p with
            # previous pointer of given node
            while(n != given_ptr):
                p = n
                n = n.next
      
            # Create a node
            m = Node(new_data)
      
            # Update the m.next
            m.next = p.next;
      
            # Update previous node's next
            p.next = m;
        
    def insertAfter(self, prev_node, new_data): 
  
        # 1. check if the given prev_node exists 
        if prev_node is None: 
          print ("The given previous node must inLinkedList.")
          return
  
        #  2. create new node & 
        #      Put in the data 
        new_node = Node(new_data) 
  
        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next
  
        # 5. make next of prev_node as new_node 
        prev_node.next = new_node 
  
  
    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    # defined inside LinkedList class shown above */ 
    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node 

    def remove(self,data):
        temp = self.head  
  
      # If head node itself holds the data to be deleted  
        if (temp is not None):  
            if (temp.data == data):  
                self.head = temp.next
                temp = None
                return
      
        # Search for the data to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp.data == data:  
                break
            prev = temp  
            temp = temp.next
      
        # if key was not present in linked list  
        if(temp == None):  
            return
      
        # Unlink the node from linked list  
        prev.next = temp.next
      
        temp = None
        
  
    # Utility function to print the linked list


    # In danh sách sinh viên đầy đủ các field
    
    def printList(self):
        f = open("List_Students.txt", "w", encoding = 'utf-8')
        temp = self.head 
        while (temp):
            temp.data.show()
            f.write( temp.data.details() + '\n')
            temp = temp.next
        f.close()

    def copy(self):
      list = LinkedList()
      temp = self.head 
      while (temp): 
        list.push(temp.data.copy())
        temp = temp.next
      return list

    # DS sinh viên Kha or Gioi and ít nhất một môn 10
    def check6(self, temp):
      if((temp.data.XEPLOAI() == 'Kha') and (temp.data.DT.data.Toan == 10 or temp.data.DT.data.Van == 10 or temp.data.DT.data.Anh == 10 )):
        return 1
      elif((temp.data.XEPLOAI() == 'Gioi') and (temp.data.DT.data.Toan == 10 or temp.data.DT.data.Van == 10 or temp.data.DT.data.Anh == 10 )):
        return 2
      else: 
        return 0

    def sortNode6(self):
      temp1 = self.head
      while(temp1):
          temp2 = temp1.next
          while(temp2):
            if(self.check6(temp2) == 1 and self.check6(temp1) == 1 and temp1.data.TONGDIEM() < temp2.data.TONGDIEM()):
              temp1.data.show()
              temp2.data.show()
              tmp = temp1.data
              temp1.data = temp2.data
              temp2.data = tmp
            elif(self.check6(temp2) == 2 and self.check6(temp1) == 2 and temp1.data.TONGDIEM() < temp2.data.TONGDIEM()):
              tmp = temp1.data
              temp1.data = temp2.data
              temp2.data = tmp
            elif(self.check6(temp2) == 1 and self.check6(temp1) == 2):
              tmp = temp1.data
              temp1.data = temp2.data
              temp2.data = tmp
            temp2 = temp2.next
          temp1 = temp1.next
      
      f = open("List_Students_6.txt", "w", encoding = 'utf-8')
      t = self.head
      while(t):
        if(self.check6(t)==1 or self.check6(t)== 2):
          f.write( t.data.details() + "\n")
        t = t.next
      f.close()

    # Câu 7: DS sinh viên Trượt
    def check7(self, temp):
      if(temp.data.XEPLOAI() == 'Truot'):
        return 1
      else: 
        return 2

    def sortNode7(self):
      temp1 = self.head
      while(temp1):
          temp2 = temp1.next
          while(temp2):
            if(self.check7(temp2) == 1 and self.check7(temp1) == 1 and temp1.data.DS.data.DTDT !=  temp2.data.DS.data.DTDT):
              if(temp1.data.DS.data.DTDT >  temp2.data.DS.data.DTDT):
                tmp = temp1.data
                temp1.data = temp2.data
                temp2.data = tmp
            elif(self.check7(temp2) == 1 and self.check7(temp1) == 1 and temp1.data.DS.data.DTDT ==  temp2.data.DS.data.DTDT):
              if(temp1.data.TONGDIEM() < temp2.data.TONGDIEM()):
                tmp = temp1.data
                temp1.data = temp2.data
                temp2.data = tmp
            #temp2.data.show()
            temp2 = temp2.next
          temp1 = temp1.next

      f = open("List_Students_7.txt", "w", encoding = 'utf-8')
      t = self.head
      while(t):
        if(self.check7(t)==1 ):
          f.write( t.data.details() + "\n")
        t = t.next
      f.close()
    

    # Câu 8: DS sinh viên thủ khoa
    def List_ThuKhoa(self):
      sum = self.head.data.TONGDIEM()
      temp = self.head.next
      while(temp):
        if(sum < temp.data.TONGDIEM()):
          sum = temp.data.TONGDIEM()
        temp = temp.next

      f = open("List_Students_8.txt", "w", encoding = 'utf-8')
      t = self.head
      while(t):
        if(sum == t.data.TONGDIEM()):
          f.write( t.data.details() + "\n")
        t = t.next
      f.close()

    # Câu 9
    def List_DTDT(self, dtdt = 0):
      fail = 0
      total = 0
      f = open("List_Students_9.txt", "w", encoding = 'utf-8')
      temp = self.head
      while(temp):
        if( temp.data.DS.data.DTDT == dtdt):
            total += 1
            f.write( temp.data.details() + "\n")
            if(temp.data.XEPLOAI() == 'Truot'):
                fail += 1
        temp = temp.next
    
      if total == 0:
          f.write('DTDT is not exists!')
      else:
          passss = total - fail
          percent1 = round((passss/total)*100)
          percent2 = 100 - percent1
          f.write('Ti le hoc sinh dau va rot la: ' + str(percent1) + '% va ' + str(percent2) + '%')
      f.close()

    # Câu 10
    def List_SBD(self, id_sbd):
      f = open("List_Students_10.txt", "w", encoding = 'utf-8')
      temp = self.head
      while(temp):
        if( temp.data.DS.data.SBD == id_sbd):
            if(int(temp.data.DS.data.Phai) == 0):
                f.write( 'GIAY BAO DIEM' + '\n' +
                         'So Bao Danh: ' + str(temp.data.DS.data.SBD) + '\n' +
                         'Anh: ' + temp.data.DS.data.Ho + temp.data.DS.data.Ten + '\n' +
                         'Toan: ' + str(temp.data.DT.data.Toan) + '\n' +
                         'Van: ' + str(temp.data.DT.data.Van) + '\n' +
                         'Anh: ' + str(temp.data.DT.data.Anh) + '\n' +
                         'Tong Diem: ' + str(temp.data.TONGDIEM()) + '\n' +
                         'Xep Loai: ' + temp.data.XEPLOAI()
                         )
            else:
                f.write( 'GIAY BAO DIEM' + '\n' +
                         'So Bao Danh: ' + str(temp.data.DS.data.SBD) + '\n' +
                         'Chi: ' + temp.data.DS.data.Ho + temp.data.DS.data.Ten + '\n' +
                         'Toan: ' + str(temp.data.DT.data.Toan) + '\n' +
                         'Van: ' + str(temp.data.DT.data.Van) + '\n' +
                         'Anh: ' + str(temp.data.DT.data.Anh) + '\n' +
                         'Tong Diem: ' + str(temp.data.TONGDIEM()) + '\n' +
                         'Xep Loai: ' + temp.data.XEPLOAI()
                         )
        temp = temp.next
      f.close()

    # Câu 2
    def Remove_SBD(self, id_sbd):
        temp = self.head
        while(temp):
            if(temp.data.DS.data.SBD == id_sbd):
                print(id_sbd)
                print(type(temp.data))
                break
            temp = temp.next
      
      
      

  
  
class DiemThi:
  def __init__(self, SBD,Toan,Van,Anh):
    self.SBD =SBD
    self.Toan = Toan
    self.Van = Van
    self.Anh = Anh
  def details(self):
    return str(self.Toan) + "|" +str(self.Van) + "|" + str(self.Anh) + "|"
  def show(self):
    print(self.details())

  def copy(self):
     return DiemThi(self.SBD, self.Toan, self.Van, self.Anh)
  

class DanhSach:
  def __init__(self, SBD, Ho, Ten, Phai, NgaySinh, DTDT):
    self.SBD = SBD
    self.Ho = Ho
    self.Ten = Ten
    self.Phai = Phai
    self.NgaySinh = NgaySinh
    self.DTDT = DTDT
  def details(self):
    return self.Ho +" " +self.Ten+"|"+ self.Phai +"|"+self.NgaySinh +"|"

  def show(self):
    print(self.details())
  def copy(self):
    return DanhSach(self.SBD, self.Ho, self.Ten, self.Phai, self.NgaySinh, self.DTDT)

# Code execution starts here 
class Data():
  def __init__(self, DS,DT):
    self.DS = DS
    self.DT = DT
  def details(self):
    return str(self.DS.data.SBD) +"|" + self.DS.data.details() + self.DT.data.details() + str(self.DTN()) +"|" + str(self.TONGDIEM()) + "|"+self.XEPLOAI() + "|" + str(self.DS.data.DTDT) +"|"
  def show(self):
    print(self.details())

  # DTN
  def DTN(self):
    dtn = self.DT.data.Toan
    if(self.DT.data.Toan > self.DT.data.Van):
      dtn = self.DT.data.Van
      if(self.DT.data.Van > self.DT.data.Anh):
        dtn = self.DT.data.Anh
    else:
      if(self.DT.data.Toan > self.DT.data.Anh):
        dtn = self.DT.data.Anh
    return dtn
  # TongDiem
  def TONGDIEM(self):
    sum = 0
    if(self.DS.data.DTDT == 1):
      sum += self.DT.data.Toan + self.DT.data.Van + self.DT.data.Anh + 2
    elif(self.DS.data.DTDT == 2):
      sum += self.DT.data.Toan + self.DT.data.Van + self.DT.data.Anh + 1
    else:
      sum += self.DT.data.Toan + self.DT.data.Van + self.DT.data.Anh
    return sum
  # XepLoai
  def XEPLOAI(self):
    strr = ''
    if(self.TONGDIEM() >= 24 and self.DTN() >= 7):
      strr = "Gioi"
    elif(self.TONGDIEM() >= 21 and self.DTN() >= 6):
      strr = "Kha"
    elif(self.TONGDIEM() >= 15 and self.DTN() >=4):
      strr = "Trung Binh"
    else:
      strr = "Truot"
    return strr

# def readFile(LinkedList &llist):

def xemDanhSachTXT():    
    newWin = Toplevel()
    newWin.title("Danh sách")

    my_text = Text(newWin)
    my_text.pack()   

    def save_file():
        text_file = open("C:/Users/User/Documents/DoAnCNTT/DanhSach.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("C:/Users/User/Documents/DoAnCNTT/DanhSach.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    
def xemChiTietTXT():
    newWin = Toplevel()
    newWin.title("Chi tiết đối tượng")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("C:/Users/User/Documents/DoAnCNTT/ChiTietDT.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()
    
    text_file = open("C:/Users/User/Documents/DoAnCNTT/ChiTietDT.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def xemDiemThiTXT():
    newWin = Toplevel()
    newWin.title("Danh sách điểm thi")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("C:/Users/User/Documents/DoAnCNTT/DiemThi.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("C:/Users/User/Documents/DoAnCNTT/DiemThi.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

 # Câu 5
def openListStudents():
    llistData.printList()
    newWin = Toplevel()
    newWin.title("Danh sách sinh viên ")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("List_Students.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("List_Students.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

 # Câu 6
def openListStudents_6():
    llistData.sortNode6()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên Khá or Giỏi and Có ít nhất một môn 10 ")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("List_Students_6.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("List_Students_6.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

  # Câu 7
def openListStudents_7():
    llistData.sortNode7()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên Trượt ")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("List_Students_7.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("List_Students_7.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

   # Câu 8
def openListStudents_8():
    llistData.List_ThuKhoa()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên Thủ Khoa ")

    my_text = Text(newWin)
    my_text.pack()

    def save_file():
        text_file = open("List_Students_8.txt", 'w')
        text_file.write(my_text.get(1.0, END))
    save_button = Button(newWin, text = "Lưu file", command=save_file)
    save_button.pack()

    text_file = open("List_Students_8.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

    # Câu 9

def openListStudents_9():
    if(DTDT_field.get() == ""):
        messagebox.showerror("Input Error", "Enter Your DTDT, Please!")
    else:
        dt = DTDT_field.get()
        if dt.strip():
            dtdt = int(dt)
        llistData.List_DTDT(dtdt)
        newWin = Toplevel()
        newWin.title("Danh Sách Sinh Viên ĐoiTuongDT " + DTDT_field.get())

        my_text = Text(newWin)
        my_text.pack()

        def save_file():
            text_file = open("List_Students_9.txt", 'w')
            text_file.write(my_text.get(1.0, END))
        save_button = Button(newWin, text = "Lưu file", command=save_file)
        save_button.pack()

        text_file = open("List_Students_9.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
        clearAll(9)
        
    

    # Câu 10
def clearAll(i):
    if( i == 2):
        SBD_delete_field.delete(0, END)
    elif( i == 3):
        sobaodanh_field.delete(0, END) 
        lastName_field.delete(0, END) 
        firstName_field.delete(0, END) 
        gender_field.delete(0, END) 
        birthday_field.delete(0, END) 
        doituongDT_field.delete(0, END) 
        math_field.delete(0, END)
        van_field.delete(0, END)
        english_field.delete(0, END)
        model_field.delete(0, END)
    elif( i == 5):
        sobaodanh_field.delete(0, END)
    elif(i == 9):
        DTDT_field.delete(0, END)
    else:
        SBD_field.delete(0, END)
        
def openListStudents_10():
    if(SBD_field.get() == ""):
        messagebox.showerror("Input Error", "Enter Your SBD, Please!")
        
    else:
        sbd = SBD_field.get()
        if sbd.strip():
            id_sbd = int(sbd)
        llistData.List_SBD(id_sbd)
        newWin = Toplevel()
        newWin.title("Chi Tiết Sinh Viên SBD: " + SBD_field.get())

        my_text = Text(newWin)
        my_text.pack()

        def save_file():
            text_file = open("List_Students_10.txt", 'w')
            text_file.write(my_text.get(1.0, END))
        save_button = Button(newWin, text = "Lưu file", command=save_file)
        save_button.pack()

        text_file = open("List_Students_10.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
        clearAll(10)

    # Câu 2: Xóa một mẫu tin
def deleteStudent_2():
    if(SBD_delete_field.get() == ""):
        messagebox.showerror("Input Error", "Enter Your SBD, Please!")
    else:
        sbd = SBD_delete_field.get()
        if sbd.strip():
            id_sbd = int(sbd)
        temp = llistData.head
        while(temp):
            if(temp.data.DS.data.SBD == id_sbd):
                llistData.remove(temp.data)
                messagebox.showinfo("Success", "Đã Xóa Mẫu Tin: " + str(id_sbd)) 
                break
            temp = temp.next
        llistData.printList()
        clearAll(2)

    # Câu 3: insertBefore
def checkError():
    if( sobaodanh_field.get() == '' or
    lastName_field.get() == '' or
    firstName_field.get() == '' or
    gender_field.get() == '' or
    birthday_field.get() == '' or
    doituongDT_field.get() == '' or 
    math_field.get() == '' or
    van_field.get() == '' or
    english_field.get() == '' or
    model_field.get() == ''):
        messagebox.showerror("Input Error")
        clearAll(3)
        return -1
    else:
        temp = llistData.head
        while(temp):
            if(temp.data.DS.data.SBD == int(sobaodanh_field.get())):
                messagebox.showerror("Input Error", "SBD tồn tại rồi, Vui lòng nhập SBD khác !!")
                clearAll(5)
                return -1
            temp = temp.next
            
    
def insertBefore_3():
    value = checkError()
    if (value == -1):
        return
    else:
        SBD = int(sobaodanh_field.get())
        Ho = lastName_field.get()
        Ten = firstName_field.get()
        Phai = gender_field.get()
        NgaySinh = birthday_field.get()
        DTDT = int(doituongDT_field.get())
        Toan = float(math_field.get())
        Van = float(van_field.get())
        Anh = float(english_field.get())
        a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, DTDT)
        llist.push(a)
        b = DiemThi(SBD, Toan, Van, Anh)
        llist2.push(b)

        #temp = llistData.head

        ds = llist.head 
        while (ds): 
            dt = llist2.head
            while (dt): 
              if(ds.data.SBD == SBD and dt.data.SBD == SBD):
                #llistData.insertBefore(temp.next,Data(ds,dt))
                c = Data(ds, dt)
                tmp = 1
                break
              dt = dt.next
            if(tmp == 1):
                break
            ds = ds.next

        temp = llistData.head
        while(temp):
            if(1 == int(model_field.get())):
                llistData.push(c)
                break
            elif(temp.data.DS.data.SBD == int(model_field.get())):
                llistData.insertBefore(x.next,c)
                break
            x = temp
            temp = temp.next

    # Câu 4: insertAfter
def insertAfter_4():
    value = checkError()
    if (value == -1):
        return
    else:
        SBD = int(sobaodanh_field.get())
        Ho = lastName_field.get()
        Ten = firstName_field.get()
        Phai = gender_field.get()
        NgaySinh = birthday_field.get()
        DTDT = int(doituongDT_field.get())
        Toan = float(math_field.get())
        Van = float(van_field.get())
        Anh = float(english_field.get())
        a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, DTDT)
        llist.push(a)
        b = DiemThi(SBD, Toan, Van, Anh)
        llist2.push(b)

        #temp = llistData.head

        ds = llist.head 
        while (ds): 
            dt = llist2.head
            while (dt): 
              if(ds.data.SBD == SBD and dt.data.SBD == SBD):
                #llistData.insertAfter(temp.next,Data(ds,dt))
                c = Data(ds, dt)
                tmp = 1
                break
              dt = dt.next
            if(tmp == 1):
                break
            ds = ds.next

        temp = llistData.head
        while(temp):
            if( 1 == int(model_field.get())):
                llistData.insertBefore(temp.next, c)
                break
            elif(temp.data.DS.data.SBD == int(model_field.get())):
                llistData.insertAfter(x.next,c)
                break
            x = temp
            temp = temp.next

        

            
        llistData.printList()


        

            
    
        
    



    

#main
if __name__ == "__main__":



    llist = LinkedList()
    llist2 = LinkedList() 
    llistData = LinkedList() 


    f = open("C:/Users/User/Documents/DoAnCNTT/DanhSach.txt", "r")
    for x in f:
      sbd = x[0:11]
      if sbd.strip():
          SBD = int(sbd)
      Ho = str(x[11:26])
      Ten = str(x[26:33])
      Phai = str(x[33:35])
      NgaySinh = str(x[35:46])
      dtdt = x[46:49]
      if dtdt.strip():
          DTDT = int(dtdt)
      a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, DTDT)
      llist.append(a)

    f = open("C:/Users/User/Documents/DoAnCNTT/DiemThi.txt", "r");
    for x in f:
      a = DiemThi(int(x[0:11]),float(x[11:24]),float(x[24:37]),float(x[37:49]))
      llist2.append(a)

    ds = llist.head 
    while (ds): 
        dt = llist2.head
        while (dt): 
          if(ds.data.SBD == dt.data.SBD):
            llistData.append(Data(ds,dt))
          dt = dt.next
        ds = ds.next

    
        







  
    # Insert 6.  So linked list becomes 6->None 
    #llist.append(a) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    #llist.push(b); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    #llist.push(c); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    #llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    #llist.insertAfter(llist.head.next, 8) 
  
    print ('Created linked list is:')
    #llist.printList() 
    print ('Created linked list is:')
    #llist2.printList() 

    print ('\n\nmerge: ')
    #llistData.printList()
    #llistData.sortNode6()
    #llistData.sortNode7()
    #llistData.List_ThuKhoa()
    #llistData.List_DTDT()
    
    
    root = Tk()
    root.title("Quản lý điểm thi")
    root.configure(background = "light green")
    root.geometry("500x500")
    heading = Label(root, text="Helo World!", bg="light green")

    open_button1 = Button(root, text="Xem File Danh Sách", fg="Black", 
                            bg="Orange", command=xemDanhSachTXT)
    open_button2 = Button(root, text="Xem File Chi Tiết", fg="Black", 
                            bg="White", command=xemChiTietTXT)
    open_button3 = Button(root, text="Xem File Điểm Thi", fg="Black", 
                            bg="Orange", command=xemDiemThiTXT)

    
    open_button5 = Button(root, text="Danh Sách Sinh Viên", fg="Black", 
                            bg="White", command=openListStudents)
    open_button6 = Button(root, text="DS Sinh Viên Khá, Giỏi", fg="Black", 
                            bg="Orange", command=openListStudents_6)
    open_button7 = Button(root, text="DS Sinh Viên Trượt", fg="Black", 
                            bg="White", command=openListStudents_7)
    open_button8 = Button(root, text="DS Sinh Viên Thủ Khoa", fg="Black", 
                            bg="Orange", command=openListStudents_8)

    DTDT = Label(root, text="DoiTuongDT", bg="light green")
    DTDT_field = Entry(root)
    submit = Button(root, text="Search", fg="Black", 
                            bg="Orange", command=openListStudents_9)

    SBD = Label(root, text="Số Báo Danh", bg="light green")
    SBD_field = Entry(root)
    submit_SBD = Button(root, text="Search_SBD", fg="Black", 
                            bg="White", command=openListStudents_10)

    # xóa một mẫu tin
    SBD_delete = Label(root, text="Xóa Một Mẫu Tin", bg="light green")
    SBD_delete_field = Entry(root)
    submit_SBD_delete = Button(root, text="Xóa", fg="Black", 
                            bg="Orange", command=deleteStudent_2)




    # Chèn trước và sau
    # create a Name label
    insertNode = Label(root, text="Mục Chèn Node", bg="light green")
    sobaodanh = Label(root, text="SBD", bg="light green") 
    lastName = Label(root, text="Họ", bg="light green")
    firstName = Label(root, text="Tên", bg="light green")
    gender = Label(root, text="Phái", bg="light green")
    birthday = Label(root, text="Ngày Sinh", bg="light green") 
    doituongDT = Label(root, text="DoiTuongDT", bg="light green")
    math = Label(root, text="Toán", bg="light green")
    van = Label(root, text="Văn", bg="light green")
    english = Label(root, text="Anh", bg="light green")
    
    model = Label(root, text="Mẫu chọn để chèn", bg="light green")


    sobaodanh_field = Entry(root) 
    lastName_field = Entry(root) 
    firstName_field = Entry(root) 
    gender_field = Entry(root) 
    birthday_field = Entry(root) 
    doituongDT_field = Entry(root) 
    math_field = Entry(root)
    van_field = Entry(root)
    english_field = Entry(root)

    model_field = Entry(root)

    

    submit_insertBefore = Button(root, text="insertBefore", fg="Black", 
                            bg="White", command=insertBefore_3)
    submit_insertAfter = Button(root, text="insertAfter", fg="Black", 
                            bg="Orange", command=insertAfter_4)
    


    heading.grid(row=0, column=1)

    open_button1.grid(row=1, column=0)
    open_button2.grid(row=1, column=1)
    open_button3.grid(row=1, column=2)

    
    open_button5.grid(row=2, column=0)
    open_button6.grid(row=3, column=0)
    open_button7.grid(row=4, column=0)
    open_button8.grid(row=5, column=0)
    
    DTDT.grid(row=6, column=0)
    DTDT_field.grid(row=6, column=1)
    submit.grid(row=6, column=2)

    SBD.grid(row=7, column=0)
    SBD_field.grid(row=7, column=1)
    submit_SBD.grid(row=7, column=2)

    SBD_delete.grid(row=8, column=0)
    SBD_delete_field.grid(row=8, column=1)
    submit_SBD_delete.grid(row=8, column=2)


    insertNode.grid(row=9, column=1)


    sobaodanh.grid(row=10, column=0)
    lastName.grid(row=11, column=0)
    firstName.grid(row=12, column=0)
    gender.grid(row=13, column=0)
    birthday.grid(row=14, column=0)
    doituongDT.grid(row=15, column=0)
    math.grid(row=16, column=0)
    van.grid(row=17, column=0)
    english.grid(row=18, column=0)

    sobaodanh_field.grid(row=10, column=1)
    lastName_field.grid(row=11, column=1)
    firstName_field.grid(row=12, column=1)
    gender_field.grid(row=13, column=1)
    birthday_field.grid(row=14, column=1)
    doituongDT_field.grid(row=15, column=1)
    math_field.grid(row=16, column=1)
    van_field.grid(row=17, column=1)
    english_field.grid(row=18, column=1)

    model.grid(row=16, column=2)
    model_field.grid(row=17, column=2)
    submit_insertBefore.grid(row=19, column=2)
    submit_insertAfter.grid(row=20, column=2)


    


    
                  
      

   
    
    

    root.mainloop()
