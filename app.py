import pyautogui
import time
import os

pyautogui.PAUSE = 1

pyautogui.click(x=328, y=224)
pyautogui.press('enter')
pyautogui.sleep(3)


#colocar cpf e nome depois de clicar em novo
pyautogui.click(x=848, y=443)
pyautogui.sleep(1)
pyautogui.click(x=1200, y=668)
pyautogui.sleep(1)
pyautogui.click(x=773, y=801)
pyautogui.write('') #colocar cpf
pyautogui.press('tab')
pyautogui.write('Andre')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.click(x=897, y=654)
pyautogui.sleep(1)

#NAVEGAÇÃO DE FAVORITOS
#funçao para clicar em um ponto do menu de ficha de declaração

def clicar_em(imagem_menu, imagem_seta, tentativas=10, cliques_seta=20):
    """
    Procura o menu na tela. Se não encontrar, clica na seta para baixo
    até encontrar ou atingir o limite de tentativas.
    """
    caminho_menu = os.path.join("imagens", imagem_menu)
    caminho_seta = os.path.join("imagens", imagem_seta)

    for i in range(tentativas):
        try:
            pos_menu = pyautogui.locateCenterOnScreen(caminho_menu, confidence=0.9)
            if pos_menu:
                pyautogui.click(pos_menu)
                print(f"[✔] Clicado no menu: {imagem_menu}")
                return True
        except pyautogui.ImageNotFoundException:
            pos_menu = None

        try:
            pos_seta = pyautogui.locateCenterOnScreen(caminho_seta, confidence=0.9)
            if pos_seta:
                pyautogui.click(pos_seta, clicks=cliques_seta, interval=0.01)
                print(f"[↧] Cliquei na seta {cliques_seta}x rapidamente")
            else:
                print("[⚠] Seta não encontrada!")
                return False
        except pyautogui.ImageNotFoundException:
            print("[⚠] Erro ao procurar a seta!")
            return False

    print(f"[✘] Menu '{imagem_menu}' não encontrado após {tentativas} tentativas.")
    return False


clicar_em('ficha_declaracao.png', 'seta_para_baixo.png')   # Antes: x=405, y=196
clicar_em('atividade_rural.png','seta_para_baixo.png')    # Antes: x=399, y=230
clicar_em('ganhos_capital.png','seta_para_baixo.png')     # Antes: x=406, y=261
clicar_em('renda_variavel.png','seta_para_baixo.png')     # Antes: x=400, y=290
clicar_em('resumo_declaracao.png','seta_para_baixo.png')  # Antes: x=407, y=326
clicar_em('govbr.png','seta_para_baixo.png')              # Antes: x=405, y=356
clicar_em('declaracao.png','seta_para_baixo.png')         # Antes: x=407, y=473
clicar_em('imprimir.png','seta_para_baixo.png')           # Antes: x=403, y=504
clicar_em('ferramentas.png','seta_para_baixo.png')        # Antes: x=408, y=539
clicar_em('ajuda.png','seta_para_baixo.png')              # Antes: x=402, y=566


pyautogui.click(x=436, y=137) #topo do menu

# pagina indent. do contribuinte
def clicar(x, y, clicks=1):
    pyautogui.click(x=x, y=y, clicks=clicks)
    time.sleep(0.2)

def escrever(texto):
    pyautogui.write(texto)
    time.sleep(0.2)

def tab(times=1):
    for _ in range(times):
        pyautogui.press('tab')
        time.sleep(0.2)

def preencher_dados_contribuinte():
    # Abertura da página do contribuinte
    clicar(201, 202)
    clicar(140, 240)
    clicar(590, 339)  # Tipo de declaração anual
    clicar(1143, 399)  # Campo do recibo da última declaração
    escrever('123456789012')  # Número do recibo

    # Dados do contribuinte
    clicar(567, 592, clicks=2)  # Data de nascimento
    escrever('12/09/2090')

    # Alteração de dados cadastrais
    clicar(509, 660)  # Sim

    # Possui companheiro(a)
    clicar(511, 719)  # Sim
    

    # Residente exterior → Brasil
    clicar(510, 789)  # Sim
    clicar(1191, 795)  # Data de retorno
    escrever('12/09/2023')
    # Scroll para baixo
    clicar(1896, 922)

    # Endereço - Tipo
    clicar(552, 451)
    clicar(581, 591)  # Chácara
    tab()
    escrever("rua gavioes")
    tab()
    escrever("123")
    tab()
    escrever("Ao lado da chacara vila lobos")
    tab()
    escrever("Novo horizonte")

    # Estado - Pará
    clicar(602, 577)  # Sigla
    clicar(639, 699)  # Scroll sigla
    clicar(566, 734)  # Seleciona Pará
    tab()
    escrever("Marabá")
    tab()
    escrever("68701-921")

    # Contato
    tab(2)
    escrever("94")
    tab()
    escrever("1111235")
    tab(3)
    escrever("sebastiao@gmail.com")

    # Ocupação
    clicar(1098, 854)  # Campo ocupação
    clicar(774, 679)   # Escolha da ocupação
    clicar(956, 550)   # Clique adicional se necessário

    print(" Dados do contribuinte preenchidos com sucesso.")       

preencher_dados_contribuinte() #cadastro do contribuinte


#menu topo: voltar ao inicio(cadastro do titular)
def preencher_rendimentos_recebidos():
    # Voltar ao início (cadastro do titular)
    clicar(514, 126)

    # Navegar até "Rendimentos Tributáveis Recebidos de Pessoa Jurídica"
    clicar_em('ficha_declaracao.png', 'seta_para_baixo.png')
    clicar_em('rendimentos_tribu_recebidos_pj.png', 'seta_para_baixo.png')

    # Acessar idetificação do contribuinte e retornar
    clicar(662, 118)
    time.sleep(2)
    clicar(514, 126)
    time.sleep(2)
    clicar(898, 126)

    # Novo rendimento
    clicar(1567, 935)

    # Preencher dados
    clicar(573, 352)  # Campo CPF/CNPJ
    escrever('159753654852')
    tab()
    escrever('andre')
    tab()
    escrever('900000')  # Rendimentos
    tab()
    escrever('7200')    # Contribuição previdenciária
    tab()
    escrever('21000')   # Imposto retido
    tab()
    escrever('35800')   # 13º salário
    tab()
    escrever('6520')    # IRRF 13º

    # Confirmar/criar
    clicar(1597, 998)

    print(" Rendimentos recebidos preenchidos com sucesso.")

preencher_rendimentos_recebidos() #cadastro de rendimentos recebidos de pessoa juridica

pyautogui.click(x=1012, y=439) #selecionar o rendimento
pyautogui.click(x=932, y=562)#confirmar a exclusão do rendimento
pyautogui.click(x=1817, y=934) #excluir rendimento

def deslogar_sistema():
    print(" Iniciando processo de logout...")

    clicar(160, 80)     # Menu inicial
    clicar(838, 483)    # Opção de sair ou configurações
    clicar(1427, 351)   # Confirmar saída ou avançar
    clicar(927, 568)    # Próximo passo do logout
    clicar(1894, 6)     # Fechar janela
    clicar(932, 553)    # Confirmar encerramento

    print(" Logout realizado com sucesso.")

# deslogar_sistema()