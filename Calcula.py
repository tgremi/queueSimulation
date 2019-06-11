#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:25:51 2019

@author: tgremi
"""

class Calculate :
    
    def calcVazao(reqProcessada, temp):
        return  reqProcessada/temp
        
    
    def mediaDeChegadas(nReq,temp):
        return nReq/temp
    
    def tempServico(nReq, temp):
        return temp/nReq
    
    
    def getUtilizacao(nReq, tempo, tempObservado):
        return (nReq * (nReq/tempo))/tempObservado