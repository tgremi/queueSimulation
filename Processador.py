# -*- coding: utf-8 -*-
"""
 -- Analise e desempenho de Software 
"""
import numpy as np
import copy
import matplotlib.pyplot as plt
import time, threading
import random



class Processador :
    
    ocupedTime = 0
    packagesProcess = 0 
    packagesFinished = 0
    flagProcess = False
    
    def setFlagProcessamento (self, flag) :
        return self.flagProcess == flag    
    
    def processaFila(fila, tempo):
        ocupedTime = 0
        packagesProcess = 0 
        packagesFinished = 0 
        ocupedTime = random.randint(1, 5)
        start = time.time()
        i = 0 
        resultado = { "pacotesProcessados": 0, "tempoOcupado": 0}
        while (tempo > i) :
            while not (fila.empty()):
                print("flagando 1:", flagProcess)
                self.setFlagProcessamento(True)
                print("flagando 2:", flagProcess)
                time.sleep(random.random())
                packageNumber = fila.get()
                end = time.time()
                packagesFinished = packagesFinished + 1
                timeElapsed = end - start 
                
                print('time : {:.1f}s'.format(timeElapsed))
                
                print(packageNumber)
                
                if(tempo <= float("{:.1f}".format(timeElapsed))):
                    fimProcesso = True
                    break
            resultado = { "pacotesProcessados": packagesFinished, "tempoOcupado": "{:.1f}".format(timeElapsed)}

            if(fimProcesso):
                break
                                
        return resultado
    
