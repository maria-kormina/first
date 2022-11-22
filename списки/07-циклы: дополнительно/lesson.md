<style>
red { color: #ff7dbc }
</style>
# Дополнительные операторы
## in

Данный оператор часто встречается в циклах и он может обрабатывать любые значения, которые можно перебрать.

    for i in range(3):
        print (i)
                            # 0
                            # 1
                            # 2

***
    l = [2,4,6]
    for i in l:
        print(i)
                            # 2
                            # 4
                            # 6

***    
    string = 'abc'
    for i in string:
        print (i)
                            # a
                            # b
                            # c

Также его можно использовать для проверки вхождения

    string = 'study python'
    if 'python' in string:
        print ('python in string')
                                    # python in string

## enumerate

Данный оператор возвращает пару `номер : значение` для каждого элемента.

    for index,value in enumerate(['a','b','c']):
        print (index,value)  
                                    # 0 a
                                    # 1 b
                                    # 2 c

Также стоит обратить внимание на переменную <red>_</red>
Она часто используется для "отбрасывания" ненужных значений.

Предположим, нам нужно перебрать список с помощью цикла <red>for</red>, однако нам требуются только индексы элементов. 

    for i,_ in enumerate(['a','b','c']):
        print (i)  
                                    # 0
                                    # 1
                                    # 2
 