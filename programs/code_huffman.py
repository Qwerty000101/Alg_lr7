#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from heapq import heappush, heappop


def add_tree(f):
    heap = []
    used = set() 

    for i in f:
        heappush(heap, (f[i], i))

    while len(heap) > 1:
        f_first, i = heappop(heap)
        f_second, j = heappop(heap)
        fs = f_first + f_second
        ord_val = ord('a')
        fl = str(fs)

        while fl in used:  
            letter = chr(ord_val)  
            fl = str(fs) + " " + letter
            ord_val += 1  

        used.add(fl) 
        f[fl] = {f"{x}": f[x] for x in [i, j]}
        del f[i], f[j]
        heappush(heap, (fs, fl))

    return f


def add_dict(tree, codes, p=''):
    for i, (node, child) in enumerate(tree.items()):
        if isinstance(child, int):
            codes[node] = p[1:] + str(abs(i-1))
        else:
            add_dict(child, codes, p + str(abs(i-1)))

    return codes


def code(sentence, dictionary):
    replaced_s = ''

    for char in sentence:
        if char in dictionary:
            replaced_s += dictionary[char]
        else:
            replaced_s += char

    return replaced_s


def decode(encoded_text, tree):
    decoded_text = ''
    key = list(tree.keys())[0]
    temp = tree[key]

    for bit in encoded_text:
        for i, (node, child) in enumerate(temp.items()):
            if str(i) != bit:
                if isinstance(child, int):
                    decoded_text += node
                    temp = tree[key]
                    break

                temp = child
                break

    return decoded_text


def count_chars(s):
    chars = {}

    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


if __name__ == "__main__":
    text = input("Введите текст: \n")
    
    chars = count_chars(text)
    for char, count in chars.items():
        print(f"Символ '{char}' встречается {count} раз(a)")
    
    tree = add_tree(chars)
    print(f"Дерево: {tree}")
    
    codes = add_dict(tree, dict())
    print("Коды:")
    for i in codes:
        print(f"{i} - {codes[i]}")
        
    coding_s = str(code(text, codes))
    print(f"Закодированное предложение: {coding_s}")

    decoded_text = decode(coding_s, tree)
    print(f"Декодированное предложение: {decoded_text}")