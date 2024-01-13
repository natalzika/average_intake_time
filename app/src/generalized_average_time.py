import numpy as np
import pandas as pd
from error_detect import TratadoraErros
from data_quality import DataQuality


class CalculadoraMedia:    
    
    @staticmethod
    def calcular_media_exec_lambda(*payload):
        try:
            payload = payload[0]
            if not payload:
                raise ValueError("Nenhum dado fornecido. Não é possível calcular a média.")
            nome_recursos_payload= payload.keys()
            
            dict_values_list= [
                np.array(nome_recursos_payload) for nome_recursos_payload in payload.values()
            ]

            DataQuality.data_quality_list(*dict_values_list)
            for i, lista in enumerate(dict_values_list):
                media_por_lambda = np.mean(lista, axis=0)
                key_names = list(nome_recursos_payload)[i]
                payload[key_names] = media_por_lambda       
    
            return payload

        except ValueError as e:
            TratadoraErros.tratar_erro(e)
            return None
    
    @staticmethod
    def calcular_media_lambdas(*payload):
        try:
            payload = payload[0]
            if not payload:
                raise ValueError("Nenhum dado fornecido. Não é possível calcular a média.")

            print(payload)
            DataQuality.data_quality_dict(payload)

            arrays_valores = [np.array(valor) for valor in payload.values()]
            media_por_posicao = np.mean(arrays_valores, axis=0).round(2)
            
            return media_por_posicao
        
        except ValueError as e:
            TratadoraErros.tratar_erro(e)
            return None


