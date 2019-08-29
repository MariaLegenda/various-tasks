
# Закодируйте любую строку по алгоритму Хаффмана.

import heapq  
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])): 
    def walk(self, code, acc):  
        self.left.walk(code, acc + "0")  
        self.right.walk(code, acc + "1")  

class Leaf(namedtuple("Leaf", ["char"])): 
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"

def huffman_encode(s):  
    h = []  # очередь

    for ch, freq in Counter(s).items(): 
        h.append((freq, len(h), Leaf(ch)))  # частотой символа, счетчик и символ

    heapq.heapify(h)  # очередь с приоритетами
    count = len(h) # инициализируем значение счетчика длиной очереди

    while len(h) > 1:  
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна сумме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) # добавим новый внутренний узел с потомками left и right
        count += 1  
   
    code = {}  
    
    if h:  
        [(_freq, _count, root)] = h  # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        root.walk(code, "")  # обойдем дерево от корня и заполним словарь для получения кодирования Хаффмана
    return code  


s = input('Введите строку для кодирования: ')  
code = huffman_encode(s)  
encoded = "".join(code[ch] for ch in s)  
    
# for ch in sorted(code): 
#     print("{}: {}".format(ch, code[ch]))  
print(encoded)  

