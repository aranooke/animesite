import linkedlist as ls;


class Node:
    def __init__(self) -> None:
        self.keys = [];
        self.value = [];

class HashTable:
    def __init__(self,size = 10) -> None:
        self.size = 10;
        self.table = [None] * self.size;
    def _hash(self,key):
        return hash(key) % self.size;

    def push(self,key,value):
        index = self._hash(key);
        print(index);
        if self.table[index] == None:
            self.table[index] = Node();
        
        node = self.table[index];
        node.keys.append(key);
        node.value.append(value);


    def delete(self,key):
        if self.table[0] == None:
            return;
        index = self._hash(key);
        node = self.table[index];
        if node == None:
            return;
        for i in range(len(node.keys)):
            if node.keys[i] == key:
                node.keys.pop(i);
                node.value.pop(i);
                return;
    def show_all(self):
        for i in range(self.size):
            if self.table[i] != None:
                print(self.table[i].keys);
                print(self.table[i].value);

    def search_key(self,key):
        index = self._hash(key);
        node = self.table[index];

        if node is not None:
            for i,val in enumerate(node.keys):
                if val == key:
                     print("find ");
                     return node.value[i];
        return None

class NodeTree():
    def __init__(self,v) -> None:
        self.v = v;

class Tree():
    def __init__(self) -> None:
        self.root = None;
        self.children = [];
    def push(self,v):
        if self.root == None:
            self.root = NodeTree(v);
        else:
            self.children.append(NodeTree(v));
    def show_all(self):
        if self.root == None:
            return;
        else:
            print(self.root.v);
            for i in self.children:
                print(i.v);
    
    def delete(self,value):
        if self.root is None:
            return;
        if not self.children:
            self.root = None;
        if value == self.root.v:
            self.root = self.children[-1];
            self.children.pop();
        else:
            for i in self.children:
                if i.v == value:
                    self.children.remove(i);
                    return;


    def delete_tree(self):
        self.root = None;
        self.children = [];
    def search_value(self,value):
        if self.root.v == value:
            return self.root;
        else:
            for i in self.children:
                if i.v == value:
                    return i.v;
        print("not found");
        return None;


class GraphNode():
    def __init__(self) -> None:
        self.value = None;

class Graph():
    def __init__(self) -> None:
        self.vertix = [];
        self.edges = [];
    def add_vertix(self,value):
        self.vertix.append(value);
    def add_edge(self,vertix1,vertix2):
        self.edges.append([vertix1,vertix2]);

    def search(self,value):
        for i in self.vertix:
            if i == value:
                print(i);
                return i;
        return None;

class NodeMark():
    def __init__(self) -> None:
        self.value = None;
        
class ChainMark():
    def __init__(self) -> None:
        pass;




# graph = Graph();

# graph.add_vertix("London");
# graph.add_vertix("Paris");
# graph.add_vertix("New York");
# graph.search("London");
# graph.add_edge("London","Paris");

# tree= Tree();
# main_branch = tree;
# main_branch.push("main");
# main_branch.push("main2");
# tree.push(main_branch);
# tree.push("sec");
# tree.push("men");
# tree.show_all();
# hf = HashTable();
# hf.push("bro",23);
# hf.push("wt",143);
# hf.show_all();
# hf.search_key("wt");
# ls.main();