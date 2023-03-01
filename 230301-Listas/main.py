from circular_list import CircularList


numbers: CircularList[int] = CircularList()
names: CircularList[str] = CircularList()
aprobados: CircularList[bool] = CircularList()

numbers.prepend(1)
numbers.prepend(23)


names.prepend('Jorge')
names.prepend('Ruben')


print(numbers.transversal())
