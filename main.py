#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:09:38 2019

@author: tgremi
"""
from Calcula import Calculate
from Processador import Processador
import queue
import numpy as np
import random 

#def main:
posicoesNaFila = int(input("Insira quantidade de requisicoes: "))
tempoObservacao = float(input("Insira o tempo de observacao (segundos): "))
fila = queue.Queue()
for i in range(posicoesNaFila):
    name = random.randint(0, 10)
    fila.put(name)
    



resultado = Processador.processaFila(fila, tempoObservacao)

###############################################################################
tempoDeservico = Calculate.tempServico(resultado["pacotesProcessados"], tempoObservacao)
print ("Tempo de servico (S): ")
print (tempoDeservico)

###############################################################################
utilizacao = Calculate.getUtilizacao(resultado["pacotesProcessados"], float(resultado["tempoOcupado"]), tempoObservacao)
print ("Utilizacao (U): ")
print (utilizacao)

###############################################################################
vazao = Calculate.calcVazao(resultado["pacotesProcessados"], tempoObservacao)
print ("Vazao (X): ")
print (vazao, "req/seg")

###############################################################################
mediaDeChegadas = Calculate.mediaDeChegadas(posicoesNaFila, tempoObservacao)
print ("Media de chegadas (lambda): ")
print (mediaDeChegadas, "req/seg")

###############################################################################
requisicoesAguardandoProcessamento = fila.qsize()
print ("Requisicoes nao processadas (fila): ")
print (requisicoesAguardandoProcessamento, "req")