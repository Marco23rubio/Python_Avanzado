# my_set1 ={"Carlos","Daniel","Abel","Cholo","Chino"}
# my_set2 ={"Marco","Carlos","Pedro","Juanito","Ines"}
# my_set3 ={"María","Mata","Mozart","Carlos","Santiago"}

# my_set4 = my_set1 & my_set2 & my_set3
# print(my_set4)

# my_set5 = my_set4 | my_set1
# print(my_set5)

#def make_unique_list(funct):
    # no_duplicates = []
    # for element in funct:
    #     if element not in no_duplicates:
    #         no_duplicates.append(element)
    # return set(no_duplicates)

def run():
    lista = [1,2,3,4,4,6,"r",7,5,"r","a","b","b"]
    print(set(lista))

if __name__ == '__main__':
    run()