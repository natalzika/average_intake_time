from generalized_average_time import CalculadoraMedia
from extract_lambda_executions import obter_tempo_execucao_lambda, obter_tempos_ultimas_execucoes
class Main:
    @staticmethod
    def main():
        nome_funcao_lambda = 'teste_funcao'
        tempos_execucao = obter_tempos_ultimas_execucoes(nome_funcao_lambda)

        if tempos_execucao:
            print("Tempos de Execução:")
            print(tempos_execucao)
        else:
            print("Não foi possível obter os tempos de execução.")

        media_unitaria = CalculadoraMedia.calcular_media_exec_lambda(
            tempos_execucao
        )
        
        media_conjunto_lambdas = CalculadoraMedia.calcular_media_lambdas(
            media_unitaria
        )
        if media_conjunto_lambdas is not None:
            print(media_conjunto_lambdas)
        

if __name__ == "__main__":
    Main.main()