import xlrd, os, xlwt


dirs = os.listdir()
lista = []
lista_final_sinvacios = []
lista_final_sinletras = []

def es_numero(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

for file in dirs:
    if file.endswith(".xls"):
        print(file)
        data = xlrd.open_workbook(file)
        sheet1 = data.sheet_by_index(0)
        a = sheet1.col_values(3)
        lista.extend(a)


#elimino valores vacios
lista_final_sinvacios = [string for string in lista if string !=""]

#elimino valores duplicados
lista_final_sinvacios = set(lista_final_sinvacios)  

for elem in lista_final_sinvacios:
    if es_numero(elem):
        lista_final_sinletras.append(float(elem))
         


##################################################################################

def extractDigits(lst): 
    return [[el] for el in lst]

lista_final_convertida_a_listas = extractDigits(lista_final_sinletras)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("hoja1")


for i in range(0,len(lista_final_convertida_a_listas)):
    for j in range(0,1):
        sheet.write(i, j, lista_final_convertida_a_listas[i][j])
workbook.save("prueba.xls")