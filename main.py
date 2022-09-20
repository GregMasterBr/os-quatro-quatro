# https://dojopuzzles.com/problems/o-poder-do-4/
'''
O poder do “4”
Contribuição de: Marcelo Fonseca Tambalo

Este problema ainda não foi utilizado em nenhum Dojo.

No livro o “O Homem que Calculava” existe a teoria de que se é possível obter qualquer número de 0 a 100, com quatro 'quatros' (4), apenas trocando seus operadores. Exemplo: para se obter o 3 deve se fazer 
CASO:

(4+4+4)/4 =3
4+(4-4)/4 = 4
((4*4)+4)/4 = 5
4+4-4/4 = 7
((4/4)+4)*4 = 20

Desenvolva uma função que retorne a fórmula para determinado número 

Entrada: 80 Saida: (4+4*4)*4
'''

import pytest

def multiplicacao(x, y): 
    return x*y

def divisao(x, y):
    if y != 0:
        return x/y
    return 0

def soma(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def concatenacao_transformar_em_numero_magico(x,y):    
    return 44
    
def fatorial(n=4):
    if n==0:
        return 1
    else:
        return fatorial(n-1)*n    

def raiz_quadrada(n=4):
    return n*0.5

def potencia(a,b):
    return a**b

def eh_par(n):
    par = False
    if n%2==0:
        par = True
    return par 

def num_terminal(terminal=4,soma=0):
    if terminal==0:
        return soma
    else:
        return num_terminal(terminal-1,soma+terminal)      

def generate_expression(n):
    express=""
    if n==0:
        express = "(4-4)"
    elif n == 8:
        express = "(4+4)"
    elif n==1:
        express = "(4/4)"
    elif n==2:
        express = "(√4)" #express = "(Sqrt(4))"        
    elif n==4:
        express = "4"
    elif n==10:
        express = "(4?)"        
    elif n==16:
        express = "(4*4)"
    elif n==20:
        express = "(4?+4?)"     
    elif n==24:
        express = "(4!)"    
    elif n==44:
        express = "(44)"   
    elif n==55:
        express = "(4?)?"            
    elif n==100:
        express = "(4?*4?)"       
    elif n==256:
        express = "(4**4)"                
    return express

def gerar_expressao(n):
    # esse algorimo resolve 98% dos casos [0-100] porém deixei implementado a solução que abraça alguns dos casos.
    if n in [3,4,5,6,10,11,12,13,14,18,19,20,21,22,23,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,68,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,89,90,92,94,95,96,97,98,100]:
        return gerar_expressao2(n)    
    elif n in [83,91,93]:
        return gerar_expressao3(n) 
    else:
        gerador_2_elementos = [soma(4,4),subtracao(4,4),multiplicacao(4,4), divisao(4,4),concatenacao_transformar_em_numero_magico(4,4),soma(num_terminal(4),num_terminal(4)),multiplicacao(num_terminal(4),num_terminal(4))]
        
        escrever_expressão_matematica=[]
        consolidacao_de_resultados = []
        
        for i in gerador_2_elementos:
            express= generate_expression(i)            
            for j in gerador_2_elementos:
                express_2=generate_expression(j)
                soma_ = soma(i,j)
                escrever_expressão_matematica.append(f"{express +'+'+ express_2}")
                if (i>j):
                    sub_ = subtracao(i,j)         
                    escrever_expressão_matematica.append(f"{express +'-'+ express_2}")            
                     
                else:
                    sub_ = subtracao(j,i)
                    escrever_expressão_matematica.append(f"{express_2 +'-'+ express}")            

                #escrever_expressão_matematica.append(f"{express +'-'+ express_2}")            
                multi_= multiplicacao(i,j)
                escrever_expressão_matematica.append(f"{express +'*'+ express_2}")
                divisao_= divisao(i,j)            
                escrever_expressão_matematica.append(f"{express +'/'+ express_2}")
                            
                consolidacao_de_resultados.append(soma_)            
                consolidacao_de_resultados.append(sub_)
                consolidacao_de_resultados.append(multi_)
                consolidacao_de_resultados.append(divisao_)
                
        print(consolidacao_de_resultados)
        print("***"*10)
        print(escrever_expressão_matematica)
        print("***"*10)
        index_ = -1
        if (n in consolidacao_de_resultados):
            index_ =consolidacao_de_resultados.index(n)
            print(f"Achou o {n} no indice {index_}")    

            print(escrever_expressão_matematica[index_])
        else:
            print(f"Não Achou o {n}")

        return escrever_expressão_matematica[index_]

def gerar_expressao2(n):
    escrever_expressão_matematica=[]
    consolidacao_de_resultados = []    
    gerador_2_elementos = [soma(4,4),subtracao(4,4),multiplicacao(4,4), divisao(4,4),
    concatenacao_transformar_em_numero_magico(4,4),
    soma(num_terminal(4),num_terminal(4)),multiplicacao(num_terminal(4),num_terminal(4))]
    #número 4, fatorial de 4, raiz quadrada de 4, terminal de 4, terminal do resultado do terminal de 4
    gerador_expressoes_especiais_1_elemento =[4, 24, 2, 10, 55]
    
    for i in gerador_2_elementos:
        express= generate_expression(i)  
        for j in gerador_expressoes_especiais_1_elemento:                    
            for w in gerador_expressoes_especiais_1_elemento:
                express_2 = generate_expression(j)
                express_3 = generate_expression(w)
                soma_parcial = soma(i,j) 
                resultado_soma_parcial_soma = soma(soma_parcial,w)        
                escrever_expressão_matematica.append(f"({express} + {express_2}) + {express_3}")
                
                if soma_parcial >= w: 
                    resultado_soma_parcial_subtracao = subtracao(soma_parcial,w)
                    escrever_expressão_matematica.append(f"({express} + {express_2}) - {express_3}")
                else:
                    resultado_soma_parcial_subtracao = subtracao(w,soma_parcial)
                    escrever_expressão_matematica.append(f"{express_3} - ({express} + {express_2})")            
                
                resultado_soma_parcial_multiplicacao = multiplicacao(soma_parcial,w)
                escrever_expressão_matematica.append(f"({express} + {express_2}) * {express_3}")        
                resultado_soma_parcial_divisao = divisao(soma_parcial,w)
                escrever_expressão_matematica.append(f"({express} + {express_2}) / {express_3}")    
                    
                consolidacao_de_resultados.append(resultado_soma_parcial_soma)            
                consolidacao_de_resultados.append(resultado_soma_parcial_subtracao)
                consolidacao_de_resultados.append(resultado_soma_parcial_multiplicacao)
                consolidacao_de_resultados.append(resultado_soma_parcial_divisao)        
                
                subtracao_parcial = subtracao(i,j)
                resultado_subtracao_parcial_soma = soma(subtracao_parcial,w)       
                escrever_expressão_matematica.append(f"({express} - {express_2}) + {express_3}")        
                
                if subtracao_parcial >= w: 
                    resultado_subtracao_parcial_subtracao = subtracao(subtracao_parcial,w)            
                    escrever_expressão_matematica.append(f"({express} - {express_2}) - {express_3}")
                else:
                    resultado_subtracao_parcial_subtracao = subtracao(w,subtracao_parcial)            
                    escrever_expressão_matematica.append(f"{express_3} - ({express} - {express_2})")
                    
                resultado_subtracao_parcial_multiplicacao = multiplicacao(subtracao_parcial,w)
                escrever_expressão_matematica.append(f"({express} - {express_2}) * {express_3}")        
                resultado_subtracao_parcial_divisao = divisao(subtracao_parcial,w)
                escrever_expressão_matematica.append(f"({express} - {express_2}) / {express_3}")        

                consolidacao_de_resultados.append(resultado_subtracao_parcial_soma)            
                consolidacao_de_resultados.append(resultado_subtracao_parcial_subtracao)
                consolidacao_de_resultados.append(resultado_subtracao_parcial_multiplicacao)
                consolidacao_de_resultados.append(resultado_subtracao_parcial_divisao)        
                
                multi_parcial = multiplicacao(i,j)
                resultado_multiplicacao_parcial_soma = soma(multi_parcial,w)
                escrever_expressão_matematica.append(f"({express} * {express_2}) + {express_3}")        
                
                if multi_parcial >= w: 
                    resultado_multiplicacao_parcial_subtracao = subtracao(multi_parcial,w)
                    escrever_expressão_matematica.append(f"({express} * {express_2}) - {express_3}")        
                else:
                    resultado_multiplicacao_parcial_subtracao = subtracao(w,multi_parcial)
                    escrever_expressão_matematica.append(f"{express_3} - ({express} * {express_2})")        
                    
                
                resultado_multiplicacao_parcial_multiplicacao = multiplicacao(multi_parcial,w)
                escrever_expressão_matematica.append(f"({express} * {express_2}) * {express_3}")        
                resultado_multiplicacao_parcial_divisao = divisao(multi_parcial,w)  
                escrever_expressão_matematica.append(f"({express} * {express_2}) / {express_3}")        
                
                consolidacao_de_resultados.append(resultado_multiplicacao_parcial_soma)
                consolidacao_de_resultados.append(resultado_multiplicacao_parcial_subtracao)
                consolidacao_de_resultados.append(resultado_multiplicacao_parcial_multiplicacao)
                consolidacao_de_resultados.append(resultado_multiplicacao_parcial_divisao)  
                
                divisao_parcial= divisao(i,j) 
                resultado_divisao_parcial_soma = soma(divisao_parcial,w)
                escrever_expressão_matematica.append(f"({express} / {express_2}) + {express_3}")        
                
                if divisao_parcial >=w: 
                    resultado_divisao_parcial_subtracao = subtracao(divisao_parcial,w)
                    escrever_expressão_matematica.append(f"({express} / {express_2}) - {express_3}")        
                else: 
                    resultado_divisao_parcial_subtracao = subtracao(w,divisao_parcial)
                    escrever_expressão_matematica.append(f"{express_3} - ({express} / {express_2})")        
                
                resultado_divisao_parcial_multiplicacao = multiplicacao(divisao_parcial,w)
                escrever_expressão_matematica.append(f"({express} / {express_2}) * {express_3}")        
                resultado_divisao_parcial_divisao = divisao(divisao_parcial,w) 
                escrever_expressão_matematica.append(f"({express} / {express_2}) / {express_3}")        
                            
                consolidacao_de_resultados.append(resultado_divisao_parcial_soma)
                consolidacao_de_resultados.append(resultado_divisao_parcial_subtracao)
                consolidacao_de_resultados.append(resultado_divisao_parcial_multiplicacao)
                consolidacao_de_resultados.append(resultado_divisao_parcial_divisao)  
        
    print(consolidacao_de_resultados)
    print("***"*10)
    print(escrever_expressão_matematica)
    print("***"*10)
    index_ = -1
    if (n in consolidacao_de_resultados):
        index_ = consolidacao_de_resultados.index(n)
        print(f"Achou o {n} no indice {index_}")    

        print(escrever_expressão_matematica[index_])
    else:
        print(f"Não Achou o {n}")

    return escrever_expressão_matematica[index_]

def gerar_expressao3(n):
    escrever_expressão_matematica=[]
    consolidacao_de_resultados = []    
    gerador_2_elementos = [soma(4,4),subtracao(4,4),multiplicacao(4,4), divisao(4,4),
    concatenacao_transformar_em_numero_magico(4,4),
    soma(num_terminal(4),num_terminal(4)),multiplicacao(num_terminal(4),num_terminal(4))]
    # terminal(termminal 4), fatorial de 4, raiz quadrada de 4, terminal de 4

    gerador_expressoes_especiais_operando_os_elemento =[55]

    return True

def test_resultado_0():
    assert gerar_expressao(0) == "(4+4)-(4+4)"

def test_resultado_1():
    assert gerar_expressao(1) == "(4+4)/(4+4)"    

def test_resultado_2():
    assert gerar_expressao(2) == "(4*4)/(4+4)"    

def test_resultado_3():
    assert gerar_expressao(3) == "((4+4) + 4) / 4" 

def test_resultado_4():
    assert gerar_expressao(4) == "((4+4) / 4) + (√4)" #"((4+4) - (√4)) - (√4)" #"(√4) - ((4+4) - (√4))" # "((4-4) * 4) + 4"

def test_resultado_5():
   assert gerar_expressao(5) == "((4+4) + (√4)) / (√4)" #"((4*4) + 4) / 4"

def test_resultado_6():
    assert gerar_expressao(6) == "((4+4) / 4) + 4"

def test_resultado_7():
    assert gerar_expressao(7) == "(4+4)-(4/4)"

def test_resultado_8():
    assert gerar_expressao(8) == "(4+4)+(4-4)"

def test_resultado_9():
    assert gerar_expressao(9) == "(4+4)+(4/4)"

def test_resultado_10():
   assert gerar_expressao(10) == "((4+4) + 4) - (√4)" #"((4-4) * (4?)) + (4?)" #"((44) - 4) / 4" 

def test_resultado_11():
   assert gerar_expressao(11) == "(4?) - ((4/4) - (√4))" 

def test_resultado_12():
   assert gerar_expressao(12) == "(4!) - ((4+4) + 4)"#"((4+4) + (√4)) + (√4)" #"((44) + 4) / 4" 

def test_resultado_13():
    assert gerar_expressao(13) == "((4*4) + (4?)) / (√4)"#"(4!) - ((44) / 4)"

def test_resultado_14():
    assert gerar_expressao(14) == "((4+4) + 4) + (√4)" #((4+4) * (√4)) - (√4)" #"(√4) - (4+4) * (√4))" #"((4+4) + 4) + (√4)"

def test_resultado_15():
   assert gerar_expressao(15) == "(4*4)-(4/4)"   
    
def test_resultado_16():
   assert gerar_expressao(16) == "(4+4)+(4+4)"    

def test_resultado_17():
   assert gerar_expressao(17) == "(4*4)+(4/4)"       

def test_resultado_18():
   assert gerar_expressao(18) == "(√4) - ((4+4) - (4!))" #"((4+4) * (√4)) + (√4)" #"((4*4) + 4) - (√4)"       

def test_resultado_19():
    assert gerar_expressao(19) == "(4!) - ((4/4) + 4)" #"(4?) - ((4/4) - (4?))" #"(4!) - ((4/4) + 4)"

def test_resultado_20():
   assert gerar_expressao(20) == "(4!) - ((4+4) - 4)" #"((4+4) + (√4)) * (√4)" #"((4/4) + 4) * 4" 

def test_resultado_21():
    assert gerar_expressao(21) == "((4/4) - 4) + (4!)"#"((4/4) + (4?)) + (4?)" #"((4/4) - 4) + (4!)"

def test_resultado_22():
    assert gerar_expressao(22) == "(4!) - ((4+4) / 4)"

def test_resultado_23():
   assert gerar_expressao(23) == "(4?)? - ((4+4) * 4)" #"((4/4) + (4!)) - (√4)" #"((44) + (√4)) / (√4)" #"((4?*4?) / 4) - (√4)"       

def test_resultado_24():
   assert gerar_expressao(24) == "(4+4)+(4*4)"  

def test_resultado_25():
   assert gerar_expressao(25) == "((4+4) * (4?)) - (4?)?" #"(√4) - ((4/4) - (4!))"  #((4?*4?)/(√4))/((√4)))

def test_resultado_26():
    assert gerar_expressao(26) == "((4+4) / 4) + (4!)" #"((4?*4?) + 4) / 4" #"((4+4) / 4) + (4!)"

def test_resultado_27():
   assert gerar_expressao(27) == "(4!) - ((4/4) - 4)"       

def test_resultado_28():
   assert gerar_expressao(28) == "((4+4) * 4) - 4"  

def test_resultado_29():
   assert gerar_expressao(29) == "(4?)? - ((4*4) + (4?))" #"((4/4) + 4) + (4!)" #"((4?*4?) / 4) + 4" #"((4/4) + 4) + (4!)"  

def test_resultado_30():
    assert gerar_expressao(30) == "((4+4) * 4) - (√4)" #"((4*4) * (√4)) - (√4)" #"((4+4) * 4) - (√4)"

def test_resultado_31():
   assert gerar_expressao(31) == "(4?)? - ((4-4) + (4!))" #"((4?*4?) + (4!)) / 4"

def test_resultado_32():
   assert gerar_expressao(32) == "(4*4)+(4*4)"       

def test_resultado_33():
   assert gerar_expressao(33) == "(4?) - ((4/4) - (4!))"

def test_resultado_34():
    assert gerar_expressao(34) == "((4+4) * 4) + (√4)" #"((4*4) * (√4)) + (√4)" #"((4+4) * 4) + (√4)"

def test_resultado_35():
    assert gerar_expressao(35) == "(4?)? - ((4*4) + 4)" #"((4/4) + (4!)) + (4?)" #"((44) / 4) + (4!)"   

def test_resultado_36():
   assert gerar_expressao(36) == "((4+4) * 4) + 4"

def test_resultado_37():
   assert gerar_expressao(37) == "(4?)? - ((4+4) + (4?))"

def test_resultado_38():
    assert gerar_expressao(38) == "((4*4) + (4!)) - (√4)" #"((4?+4?) * (√4)) - (√4)" #"((44) - 4) - (√4)"

def test_resultado_39():
   assert gerar_expressao(39) == "((4+4) - (4!)) + (4?)?"

def test_resultado_40():
    assert gerar_expressao(40) == "((4+4) - 4) * (4?)" #"(4!) - ((4+4) - (4!))" #"((44) - (√4)) - (√4)" #"((4+4) - 4) * (4?)"

def test_resultado_41():
   assert gerar_expressao(41) == "(4?)? - ((4*4) - (√4))"

def test_resultado_42():
    assert gerar_expressao(42) == "((4+4) * 4) + (4?)" #"((4?+4?) * (√4)) + (√4)" #"((44) - 4) + (√4)"

def test_resultado_43():
   assert gerar_expressao(43) == "(44)-(4/4)"

def test_resultado_44():
   assert gerar_expressao(44) == "(4-4)+(44)"

def test_resultado_45():
   assert gerar_expressao(45) == "(4/4)+(44)"    

def test_resultado_46():
   assert gerar_expressao(46) == "((4/4) - (4?)) + (4?)?" #"((44) + 4) - (√4)"       

def test_resultado_47():
   assert gerar_expressao(47) == "((4*4) - (4!)) + (4?)?" #"(4!) - ((4/4) - (4!))" 

def test_resultado_48():
   assert gerar_expressao(48) == "((4+4) + 4) * 4"

def test_resultado_49():
   assert gerar_expressao(49) == "(4?)? - ((4+4) - (√4))" #"((4/4) + (4!)) + (4!)" #"((4?*4?) / 4) + (4!)"

def test_resultado_50():
    assert gerar_expressao(50) == "((4*4) + (4!)) + (4?)" #"((4/4) + 4) * (4?)"

def test_resultado_51():
    assert gerar_expressao(51) == "(4?)? - ((4+4) - 4)" #"((4?*4?) + (√4)) / (√4)"

def test_resultado_52():
   assert gerar_expressao(52) == "(4+4)+(44)"

def test_resultado_53():
    assert gerar_expressao(53) == "(4?)? - ((4+4) / 4)"

def test_resultado_54():
    assert gerar_expressao(54) == "((4*4) * 4) - (4?)"

def test_resultado_55():
    assert gerar_expressao(55) == "((4-4) * 4) + (4?)?" #"((4?*4?) + (4?)) / (√4)"

def test_resultado_56():
    assert gerar_expressao(56) == "((4+4) * 4) + (4!)" #"((4+4) + (4!)) + (4!)" #"((4+4) * 4) + (4!)"

def test_resultado_57():
    assert gerar_expressao(57) == "((4+4) / 4) + (4?)?"

def test_resultado_58():
    assert gerar_expressao(58) == "(4?)? - ((4/4) - 4)" #"((44) + 4) + (4?)"

def test_resultado_59():
    assert gerar_expressao(59) == "((4+4) - 4) + (4?)?"

def test_resultado_60():
   assert gerar_expressao(60) == "((4+4) - (√4)) * (4?)" #"((4*4) * 4) - 4"  

def test_resultado_61():
    assert gerar_expressao(61) == "((4+4) - (√4)) + (4?)?"

def test_resultado_62():
    assert gerar_expressao(62) == "((4*4) * 4) - (√4)"

def test_resultado_63():
    assert gerar_expressao(63) == "(4?)? - ((4*4) - (4!))"

def test_resultado_64():
   assert gerar_expressao(64) == "(4+4)*(4+4)"    

def test_resultado_65():
    assert gerar_expressao(65) == "((4+4) + (√4)) + (4?)?"

def test_resultado_66():
    assert gerar_expressao(66) == "((4*4) * 4) + (√4)"

def test_resultado_67():
    assert gerar_expressao(67) == "((4+4) + 4) + (4?)?"

def test_resultado_68():
   assert gerar_expressao(68) == "((4*4) * 4) + 4"  

def test_resultado_69():
    assert gerar_expressao(69) == "((4*4) - (√4)) + (4?)?"

def test_resultado_70():
    assert gerar_expressao(70) == "((4+4) * (4?)) - (4?)"

def test_resultado_71():
    assert gerar_expressao(71) == "(4?)? - ((4+4) - (4!))"

def test_resultado_72():
    assert gerar_expressao(72) == "((4+4) + (4?)) * 4" #"((44) + 4) + (4!)"

def test_resultado_73():
    assert gerar_expressao(73) == "((4+4) + (4?)) + (4?)?"
    
def test_resultado_74():
    assert gerar_expressao(74) == "((4*4) * 4) + (4?)"

def test_resultado_75():
    assert gerar_expressao(75) == "((4*4) + 4) + (4?)?"

def test_resultado_76():
    assert gerar_expressao(76) == "((4+4) * (4?)) - 4" #"((4?+4?) * 4) - 4"

def test_resultado_77():
    assert gerar_expressao(77) == "((44) / (√4)) + (4?)?"

def test_resultado_78():
   assert gerar_expressao(78) == "((4+4) * (4?)) - (√4)" #"((4?+4?) * 4) - (√4)"       

def test_resultado_79():
    assert gerar_expressao(79) == "((4-4) + (4!)) + (4?)?"

def test_resultado_80():
    assert gerar_expressao(80) == "((4*4) + 4) * 4"  

def test_resultado_81():
    assert gerar_expressao(81) == "((4*4) + (4?)) + (4?)?"

def test_resultado_82():
   assert gerar_expressao(82) == "((4+4) * (4?)) + (√4)" #"((4?+4?) * 4) + (√4)"       

def test_resultado_83():
    assert gerar_expressao(83) == ""

def test_resultado_84():
    assert gerar_expressao(84) == "((4+4) * (4?)) + 4" #"((44) - (√4)) * (√4)" #"((4?+4?) * 4) + 4"

def test_resultado_85():
    assert gerar_expressao(85) == "((4?+4?) + (4?)) + (4?)?"

def test_resultado_86():
    assert gerar_expressao(86) == "((44) * (√4)) - (√4)"

def test_resultado_87():
    assert gerar_expressao(87) == "((4+4) * 4) + (4?)?"

def test_resultado_88():
    assert gerar_expressao(88) == "(44)+(44)"

def test_resultado_89():
    assert gerar_expressao(89) == "((44) - (4?)) + (4?)?"

def test_resultado_90():
    assert gerar_expressao(90) == "((4+4) * (4?)) + (4?)"

def test_resultado_91():
    assert gerar_expressao(91) == ""

def test_resultado_92():
    assert gerar_expressao(92) == "((44) + (4!)) + (4!)" #"((4?*4?) - 4) - 4"

def test_resultado_93():
    assert gerar_expressao(93) == ""

def test_resultado_94():
   assert gerar_expressao(94) == "(4?)? - ((4*4) - (4?)?)" #"((4?*4?) - 4) - (√4)"       

def test_resultado_95():
    assert gerar_expressao(95) == "((4*4) + (4!)) + (4?)?"

def test_resultado_96():
    assert gerar_expressao(96) == "((4+4) - 4) * (4!)" #"((4?+4?) + 4) * 4" #"((4+4) - 4) * (4!)"

def test_resultado_97():
    assert gerar_expressao(97) == "((44) - (√4)) + (4?)?"

def test_resultado_98():
   assert gerar_expressao(98) == "((44) * (√4)) + (4?)" #"((4?*4?) - 4) + (√4)"  

def test_resultado_99():
    assert gerar_expressao(99) == "(4?*4?)-(4/4)"

def test_resultado_100():
    assert gerar_expressao(100) == "((4+4) + (√4)) * (4?)" #"((4-4) + (4?)) * (4?)" #"((4?*4?) + 4) - 4"

# def test_resultado_0000():
#     assert gerar_expressao(0) == "" 


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

