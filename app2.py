import openpyxl

#carregar arquivo
teste = openpyxl.load_workbook('PlanilhaTeste.xlsx')
#selecionando pag
test_page = teste['TESTE']
#imprimir dados de cada linha
for rows in test_page.iter_rows(min_row=2,max_row=8):
    #imprimir os dados um ao lado do outro
    print(rows[0].value,rows[1].value,rows[2].value)    