# -*- coding:utf-8 -*-

class Pilha:
    def __init__(self) -> None:
        self.pilha = [] #Lista do python

    def is_empty(self):
        return true if len(self.__pilha)==0 else false 

    def push(self):
        self.__pilha.append(valor)

    def pop(self):
        if self.is_empty()
            raise Exception("Sorry, pilha vazia!!!")
        else:
            valor = self.__pilha.pop()
            return valor

    def peek(self):
        if self.is_empty()
            raise Exception("Sorry, pilha vazia!!!")
        else:
            valor = self.__pilha[-1]
            return valor

    def list_items(self):
        if self.is_empty()
            raise Exception("Sorry, pilha vazia!!!")
        else:
            print("Relação de itens na pilha:\n")
            for item in self.__pilha:
                print(item)

    def get_size(self):
        return len(self.__pilha)
