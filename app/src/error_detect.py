class TratadoraErros:
    @staticmethod
    def tratar_erro(excecao):
        mensagem_erro = f"Erro: {excecao}"
        print(mensagem_erro)
        
        return None