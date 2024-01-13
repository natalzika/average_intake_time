class TratadoraErros:
    @staticmethod
    def tratar_erro(excecao, arquivo_erro=None):
        mensagem_erro = f"Erro: {excecao}"
        print(mensagem_erro)
        
        return None