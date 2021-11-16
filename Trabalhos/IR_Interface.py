import PySimpleGUI as sg
# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Bem-vindo(a) ao cálculo do Imposto de Renda!')],
    [sg.Text('Digite o total de horas trabalhadas na semana'), sg.Input(key='nro_h', size=(10, 1))],
    [sg.Text('Digite o salário bruto mensal R$'), sg.Input(key='salario', size=(10, 1))],
    [sg.Text('Digite o número de filhos e/ou dependentes'), sg.Input(key='nro_filhos', size=(10, 1))],
    [sg.Button('Calcular')],
    [sg.Button('Calcula', visible=False, bind_return_key=True)],
    [sg.Output(size=(40, 10))]
    ]
# janela
janela = sg.Window('Cálculo Imposto de Renda', layout=layout, grab_anywhere=True, return_keyboard_events=True)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Escape:27':
        break
    elif eventos == 'Calcular' or eventos == 'Calcula':
        if valores['nro_h'] == '' or valores['nro_filhos'] == '' or valores['salario'] == '':
            print('Estão faltando algumas informações\n')
        else:  
            horas_mes = int(valores['nro_h']) * 4
            aliquota = 0
            deducao = 0
            deducao_filhos = int(valores['nro_filhos']) * 189.59
            calculo = float(valores['salario']) - deducao_filhos
            if calculo <= 1903.98:
                print('Valor do IR a ser pago: R$0.00')
            elif float(valores['salario']) > 1903.98 and calculo <= 2826.65:
                aliquota = 0.075
                deducao = 142.80
            elif 2826.65 < calculo <= 3751.05:
                aliquota = 0.15
                deducao = 354.80
            elif 3751.05 < calculo <= 4664.68:
                aliquota = 0.225
                deducao = 636.13
            else:  # se calculo > 4664.68:
                aliquota = 0.275
                deducao = 869.36
            calculo_ir = (calculo * aliquota) - deducao
            print(f'Valor do IR a ser pago: R${calculo_ir:.2f}')
janela.close()
print("Fonte utilizada: https://www.debit.com.br/tabelas/tabelas-irrf.php")