# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:30:57 2025

@author: Utilizador
"""

import datetime

# Importação das classes
from classes.Book import Book
from classes.Member import Member
from classes.Publisher import Publisher
from classes.Requisition import Requisition

# Dicionário de classes disponíveis
classes_disponiveis = {
    "1": ("Book", Book),
    "2": ("Member", Member),
    "3": ("Publisher", Publisher),
    "4": ("Requisition", Requisition)
}

test_class = None
db = 'library.db'

def gerar_exemplo_ob(cls):
    """Gera um exemplo 'ob' com valores padrão para a classe selecionada."""
    if cls is None:
        return ""

    atributos = list(cls.__init__.__code__.co_varnames[1:cls.__init__.__code__.co_argcount])  # Pega os atributos da __init__
    valores_exemplo = []

    for atributo in atributos:
        if "date" in atributo.lower():
            valores_exemplo.append("2000-01-01")  # Exemplo de data
        elif "id" in atributo.lower() or atributo == "id":
            valores_exemplo.append("100")  # Exemplo de ID
        elif "price" in atributo.lower() or "salary" in atributo.lower():
            valores_exemplo.append("1000.0")  # Exemplo de valor monetário
        elif "age" in atributo.lower():
            valores_exemplo.append("30")  # Exemplo de idade
        else:
            valores_exemplo.append(f"Exemplo_{atributo}")  # Exemplo de string

    return ";".join(valores_exemplo)

# Função para escolher a classe
def escolher_classe():
    global test_class, ob  # Para modificar as variáveis globais
    print("\nEscolha a classe que deseja testar:")
    for key, (name, _) in classes_disponiveis.items():
        print(f"{key} - {name}")
    
    escolha = input("Digite o número da classe: ")

    if escolha in classes_disponiveis:
        nome, test_class = classes_disponiveis[escolha]
        ob = gerar_exemplo_ob(test_class)  # Gera um exemplo válido para a classe escolhida
        print(f"\nClasse selecionada: {nome}")
        print(f"Exemplo de entrada gerado: {ob}")
    else:
        print("\nOpção inválida. Mantendo a classe anterior.")

# Começa pedindo para escolher uma classe
escolher_classe()

# Lê o ficheiro CSV correspondente à classe escolhida
test_class.read('data/' + db)

op = ''
while op != 'q':
    print('\nEscolha uma opção:')
    print('---------------')
    print('c - escolher outra classe')
    print('l - listar')
    print('b - início')
    print('n - próximo')
    print('p - anterior')
    print('e - fim')
    print('---------------')
    print('i - inserir')
    print('m - modificar')
    print('r - remover')
    print('---------------')
    print('s - ordenar por atributo')
    print('f - procurar por atributo')
    print('---------------')
    print('q - sair')
    print('---------------')

    p = test_class.current()
    print(f'\n{p}')
    op = input('?')

    if op == 'c':
        escolher_classe()
        test_class.read('data/' + db)  # Recarrega os dados da nova classe

    elif op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        p1 = None
        if len(test_class.lst) == 0:
            p = eval('test_class.from_string("' + ob + '")')
            p1 = p
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        print('Deixe em branco para auto-incremento')
        id = input(f'{attrib[1:]} = ')
        if id == "":
            id = 0
        else:
            id = int(id)
        strarg = f'test_class({id}'
        for i in range(1, len(str_list)):
            attrib = str_list[i]
            atype = type(getattr(p, attrib))
            if atype == datetime.date or atype == str:
                value = input(f'{attrib[1:]} = ')
                strarg += f',"{value}"'
            else:
                value = atype(input(f'{attrib[1:]} = '))
                strarg += f',{value}'
        strarg += ')'
        if p1 is not None:
            test_class.remove(getattr(p, str_list[0]))
        print(strarg)
        pobj = eval(strarg)
        attrib = str_list[0]
        code = getattr(pobj, attrib)
        obj = test_class.current(code)
        test_class.insert(code)

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Registo {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj = test_class.current(id)
            print('Deixe em branco ou insira um novo valor para modificar')
            for attrib in str_list[1:]:
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.date.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        test_class.update(id)

    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirmar remoção (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)

    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])

    elif op == 's':
        attrib = input('Ordenar por atributo: ')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverso (False):'):
                reverse = True
            codep = p.id
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)

    elif op == 'f':
        attrib = input('Nome do atributo: ')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            value = atype(input('Valor: '))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)
