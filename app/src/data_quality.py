class DataQuality:
    @staticmethod
    def data_quality_list(*payload):
        # Exemplo: Verificar se todas as listas têm o mesmo número de elementos
        tamanhos = set(len(lista) for lista in payload)
        if len(tamanhos) > 1:
            raise ValueError("As listas têm tamanhos diferentes. Certifique-se de que todas as listas tenham o mesmo tamanho.")
        
        print("As Listas de entrada foram validadas com sucesso. Passando para o próximo passo.")
    
    def data_quality_dict(*payload):
        # Exemplo: Verificar se todos os valores são listas não vazias
        payload = payload[0]
        for chave, valor in payload.items():
            if not valor or not chave:
                raise ValueError(f"O valor associado à chave '{chave}' não é uma lista válida.")
        print("O dicionário de entrada foi validado com sucesso. Passando para o próximo passo.")
