import numpy as np
import pandas as pd
from error_detect import TratadoraErros


class CalculadoraMedia:
    @staticmethod
    def aplicar_regras_data_quality(*listas):
        # Exemplo: Verificar se todas as listas têm o mesmo número de elementos
        tamanho_listas = [len(lista) for lista in listas]

        if len(set(tamanho_listas)) > 1:
            raise ValueError("As listas têm tamanhos diferentes. Certifique-se de que todas as listas tenham o mesmo tamanho.")

    @staticmethod
    def calcular_media(*listas, arquivo_erro=None):
        try:
            if not listas:
                raise ValueError("Nenhum valor fornecido. Não é possível calcular a média.")

            CalculadoraMedia.aplicar_regras_data_quality(*listas)

            media_por_posicao = np.mean(listas, axis=0)

            df_resultado = pd.DataFrame(data={'Lista' + str(i+1): lista for i, lista in enumerate(listas)})
            df_resultado['Media'] = media_por_posicao

            return df_resultado

        except ValueError as e:
            TratadoraErros.tratar_erro(e, arquivo_erro)
            return None


