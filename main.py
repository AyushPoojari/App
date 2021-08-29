from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window


class HomeScreen(Screen):
    pass

class DataStructureWindow(Screen):
    pass

class AlgorithmWindow(Screen):
    pass

class StackWindow(Screen):
    pass

class QueueWindow(Screen):
    pass

class StackVisualizer(Screen):
    global stack,top
    top = -1
    stack = []

    def push(self):
        global  data
        data = self.ids.text_input.text
        print(data)
        global  top
        if (top < 9):
            top = int(top) + 1
            print(top)
            stack.append(data)
            self.ids[f'{top}'].background_color = (1,0,0,1)
            self.ids[f'{top}'].text = data
            self.ids.l1.text = f'Pushed {data}'
            print(stack)
        else:
            self.ids.l1.text = 'Stack is Full'
            print('Stack is Full')

    def pop(self):
        global top
        if (top == -1):
            self.ids.l1.text = 'Stack is Empty'
            print('Underflow')
        else:
            temp =stack.pop()
            self.ids.l1.text = f'Popped {temp}'
            self.ids[f'{top}'].background_color = (0,0,0,0)
            top = int(top) - 1
            print(stack)
    pass


class QueueVisualizer(Screen):
    global rear,head,size,queue
    queue = []
    head = -1
    rear = -1
    size = 10

    def enqueue(self):
        global data
        data = self.ids.text_input.text
        global  rear,size,head
        if (rear == size - 1):
            print("\nQueue is Full!!")
        else:
            if (head == -1):
                head = 0
            rear = int(rear) + 1
            queue.insert(rear,data)
            self.ids[f'{rear}'].background_color = 1,0,1,1
            self.ids[f'{rear}'].text = f'{data}'
            print(queue)


    def dequeue(self):
        global rear, size, head
        if(head == -1):
            print("\nQueue is Empty!!")
        else:
            print(head)
            queue.pop(0)
            print(queue)
            self.ids[f'{head}'].background_color = 0,0,0,0
            head = int(head) + 1
            print(head)
            if (head > rear):
                head = rear = -1
    pass



class LinearSearch(Screen):
    global t,k,array,x,f
    k = 0
    array =[]
    x = 1
    f = 0
    def create_array(self):
        global k
        if (k < 6):
            enter_data = self.ids.lstext_input.text
            array.append(enter_data)
            self.ids[f'a{k}'].background_color = 1,0,0,1
            self.ids[f'a{k}'].text = str(enter_data)
            k = int(k) + 1
            print(array)
        else:
            print("Array is Full")

    def ls(self):
        global array,x,f,k

        print(f'New {array}')
        for i in range(len(array)):
            k = i
            self.ids[f't{k}'].background_color = 1,1,1,1
            self.ids[f't{k}'].text = 'X'
            if array[i] == str(x):
                self.ids[f'a{k}'].background_color = 0,1,0,1
                self.ids[f't{k}'].text = '^'
                print("Found")
                f = 1
        if (f == 0):
            print('Not Found')

    pass


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    global width,height
    Window_size = Window.size
    width = Window_size[0]
    height = Window_size[1]
    def build(self):
        return Builder.load_file('main.kv')

MyApp().run()
