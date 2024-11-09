import math
import sqlite3
from colorama import Fore, Style, init

init()

#conexão com o sqlite3 e com o arquivo .dba
#################################
conexao = sqlite3.connect("dba_simulfactor.dba")
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS loguins (Nome, Loguin, Usuario, CPF)''')

###################################


#classe do menu principal, e estruturas de decisão.
###################################
class MenuPrincipal:  #@@@@@@
	def __init__(self):    ###
		print(Fore.GREEN + "\t\t\n\nSeja Bem-Vindo ao SimulFactor\t\t\tV1.0\n\nDigite o que você deseja fazer:\n\n"
			  "[1] • Cálculos de Engenharia Mecânica\n"
			  "[2] • Cálculos de Engenharia Civil\n"
			  "[3] • Cálculos de Engenharia Elétrica\n"
			  "[4] • Mecânica dos Fluidos\n"
			  "[5] • Elementos de Máquinas\n"
			  "[exit] • Sair\n")
		self.decision1_menu = input(">>> ")
	def decisao_menu_principal(self): ###
		if self.decision1_menu == "1":
			EngMecanica().menu_calc_mecanica()
		elif self.decision1_menu == "2":
			EngCivil().menu_calc_civil()
		elif self.decision1_menu == "3":
			EngEletrica().menu_calc_eletrica()
		elif self.decision1_menu == "4":
			EngFluidos().menu_calc_fluidos()
		elif self.decision1_menu == "5":
			ElementosMaquinas().calc_elementos_maquinas()
		elif self.decision1_menu.lower() == "exit":
			print("Saindo...\n\t\t\tSimulFactor")
			exit()
		else:	
			print("Opção inválida. Tente novamente.")
			
####################################		

#Classe que determina os calculos de engenharia mecanica
#######################22###########
class EngMecanica: #@@@@@@@
	def __init__(self):  ###
		print("Menu de Simulações e Cálculos")
	def menu_calc_mecanica(self):  ###
		print("Cálculos de engenharia mecânica")
		input("\nPressione Enter para voltar ao menu principal...\t")  

##################2#################


#Classe com os calculos de engenharia civil
####################################
class EngCivil: #@@@@@@
	def __init__(self):  ###
		print("Menu de Simulações e Cálculos")
	def menu_calc_civil(self):   ###
		print("Cálculos de engenharia civil")
		input("Pressione Enter para voltar ao menu principal...")  

####################################


#classe principal dos calculos essenciais da engenharia eletrica
####################################
class EngEletrica:  #@@@@@
	def __init__(self):  ###
		pass																
	def menu_calc_eletrica(self):   ###
		print("Cálculos de engenharia elétrica:\n\n\t[1] Calculo Formulas de Kirchoff.\n\t[2] Impedância\n\t[3] Calcular resistencia do condutor\n\t[4] Dissipação de Potência\n\t[5] Fluxo de carga\n\n ")
		self.decision = input("\t>>>")
		self.menu_eng_eletrica()
	def menu_eng_eletrica(self):   ###
		if self.decision == "1":
			self.calculo_kirchoff()
		elif self.decision == "2":
			self.impedancia()
		elif self.decision == "3":
			self.resistencia_condutor()
		elif self.decision == "4":
			self.dissipacao_potencia()
		elif self.decision == "5":
			self.fluxo_de_carga()
	def calculo_kirchoff(self):     ###
		print("\n\t\t[1] Lei dos nós LKC\n\t\t[2] Lei das malhas LKT\n\t\t[3] Tensão, Corrente e Resistência")
		decision_kirchoff = input("\n\t\t>>>")
		if decision_kirchoff == "1":
			self.lei_dos_nos()
		elif decision_kirchoff == "2":
			self.lei_das_malhas()
		elif decision_kirchoff == "3":
			self.tensao_corrente_resistencia()
		def resistencia_condutor(self):  ###
			pass
		def impedancia():    ###
			print("impedancia")
	def dissipacao_potencia(self):   ###
		print("O que você deseja descobrir?\n1 - Tensão\n2 - corrente\n3- Potência")
		menu_potencia = input("\n>>>")
		if menu_potencia == "3":
			print("Digite o valor da tensão elétrica:\n\t")
			U = float(input(">>>"))
			print("Digite o valor da corrente elétrica:\n\t")
			I = float(input(">>>"))
			potencia_eletrica = U*I
			print("O resultado da Potência Elétrica é {} Watts".format(potencia_eletrica))
		elif menu_potencia == "2":
			print("Digite o valor da tensão:\n")
			U = float(input(">>>"))
			print("Digite o valor da potência elétrica em watts\n")
			P = float(input(">>>"))
			resistencia_eletrica = U/P
			print("O resultado da Corrente Elétrica é {} Ohms ".format(resistencia_eletrica))
		elif menu_potencia == "1":
			print("Digite o Valor da Resistência:\n")
			R = float(input(">>>"))
			print("Digite o valor da potência:\n")
			P = float(input(">>>"))
			tensao = None
			stop(self)
	def fluxo_de_carga(self):  ###
		pass
	def lei_dos_nos(self):  ###
		pass
	def lei_das_malhas(self):  ###
		pass
	def tensao_corrente_resistencia(self):  ###
		print("O que você deseja descobrir?\n1 - Tensão\n2 - corrente\n3- Resistência\n\n")
		decision = input(">>>")
		if decision == "1":
			print("Digite o valor da Resistência EQUIVALENTE do circuito:\n")
			R = float(input(">>>"))
			print("Digite o valor da corrente:\n")
			I = float(input(">>>"))
			tensao = R*I
			print("A tensão do circuito é {:.2f}Volts".format(tensao))
			stop(self)
			
####################################
		

#Classe principal dos cálculos de mecânica dos fluidos/ metodos de continuidade
##################################
class EngFluidos:  #@@@@@
	def __init__(self):   ###
		pass
		
	def menu_calc_fluidos(self):  ###
		print("CÁLCULOS DE MECANICA DOS FLUIDOS\n\n\t[1] - Equação da Continuidade\n\t[2] - Lei de Pascal\n\t[3] - Equação de Torricceli\n\t[4] - Equação de Bernoulli\n")
		self.decisao = input(">>>")
		if self.decisao == "1":
			EngFluidos().equacao_continuidade(self)
			
	def equacao_continuidade():  ###
		print("\nUsado para garantir a conservaçao da massa em um fluxo incomprensível. A fórmula se da por:\n\n")
		formula_equacao_continuidade = (Fore.RED + "A1 • V1 = A2 • V2")
		print("\t\t\t" + formula_equacao_continuidade +Fore.GREEN+ "\n\nA1 - Área sa secção transversal do tubo 1\nV1 - A velocidade do fluido no tubo 1\nA2 - Área da secção transversal do Tubo 2\nV2 -  A velocidade do Fluido no tubo 2\n\nInsira as valores:\n")
		print("\nInsira A1:\n")
		A1 = float(input("\n>>>"))
		print("\nInsira V1\n")
		V1 = float(input("\n>>>"))
		print("\nInsira A2\n")
		A2 = float(input("\n>>>"))
		print("\nInsira V2\n")
		V2 = float(input("\n>>>"))
		calculo_equacao_continuidade1 = 'Teste1'
		print(calculo_equacao_continuidade1)
		stop(self)
	def lei_pascal(self):  ###
		print("Lei de Pascal\n\nDigite o valor da força: ")
		F = float(input("\n>>>"))
		print("Digite o valor da Área:\n")
		A = float(input("\n>>>"))
		P = F/A
		print("O valor da pressão é {:.2f} psi".format(P))
	def equacao_toricelli(self):   ###
		print("Usada para determinar a velocidade de saída de um fluido através de um orifício. A fórmula é dada por:\n\n\t\t\tv = √2•G•h\nh = altura da coluna do fluido acima do orifício de saída.\n\n")
		
#################################


#Classe formulas de elememtos de maquinas
#################################
class ElementosMaquinas:  #@@@@@
	def __init__(self):   ###
		print("Menu de Simulações e Cálculos")

	def calc_elementos_maquinas(self):  ###
		print("Cálculos de elementos de máquinas")
		input("Pressione Enter para voltar ao menu principal...") 
		
#################################

#classes e funçõea estrururais 
#################################
def stop(self):  ###
	decisao = input("\n\nPressione Enter para voltar ao menu anterior...\t\t")


##################################

#logo do SimulFactor
##################################
codigo_ascii = Fore.BLUE + """  _____  _                    _
 / ____|(_)                  | |
| (___   _  _ __ ___   _   _ | |
 \___ \ | || '_ ` _ \ | | | || |
 ____) || || | | | | || |_| || |
|_____/ |_||_| |_| |_| \__,_||_|


"""
codigo_ascii2 = """ ______               _
|  ____|             | |
| |__     __ _   ___ | |_   ___   _ __
|  __|   / _` | / __|| __| / _ \ | '__|
| |     | (_| || (__ | |_ | (_) || |
|_|      \__,_| \___| \__| \___/ |_|


"""
print(codigo_ascii,"\n",codigo_ascii2)
###############################



#Estrutura de repetição da interface principal
while True:
	menu = MenuPrincipal()  
	menu.decisao_menu_principal()