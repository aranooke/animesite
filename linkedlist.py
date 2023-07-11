

class Node:
    def __init__(self,value):
        self.v = value;
        self.next = None;

class LinkedList:
    
    def __init__(self) -> None:
        self.head,self.tail = None, None;
    
    def push(self,value):
        if self.head == None:
            self.head = Node(value);
            self.tail = self.head;
        else:
            self.tail.next = Node(value);
            self.tail= self.tail.next;

    def show_all(self):
            self.temp = self.head;
            while self.temp != None:
                print(self.temp.v);
                self.temp = self.temp.next;
    def delete(self,index):
        if index == 0:
            self.head = self.head.next;
        else:
            self.temp = self.head;
            itr = 0;
            while itr != index :
                itr+=1;
                self.temp = self.temp.next;
            self.temp.next = self.temp.next.next;
    def pop(self):
        self.temp = self.head;
        while self.temp.next.next != None:
            self.temp = self.temp.next;
        self.temp.next = None;
        self.tail = self.temp;

class DoubleNode():
    def __init__(self,value) -> None:
        self.prev = None;
        self.next = None;
        self.v = value;


class DoubleList():
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;
    
    def push(self,value):
        if self.head == None:
            self.head = DoubleNode(value);
            self.tail = self.head;
            self.p = self.head;
        else:
            self.tail.next = DoubleNode(value);
            self.tail.next.prev = self.p;
            self.tail = self.tail.next;


    def showList(self):
        if self.head == None:
            return;
        self.p = self.head;
        while self.p != None:
            print(self.p.v);
            self.p = self.p.next;
    
    def delete(self,value):
        if self.head == None:
            return;
    
def main():
    dlst = DoubleList();
    dlst.push(34);
    dlst.push(55);
    dlst.push(120);
    dlst.push(13);
    dlst.showList();
main();