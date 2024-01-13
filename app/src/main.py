from generalized_average_time import CalculadoraMedia
class Main:
    @staticmethod
    def main():
        ingest = [10, 3, 4, 9, 7]
        persist = [5, 12, 11, 8, 3]
        catalog = [2, 8, 4, 6, 5]

        arquivo_erro = "erros.txt"

        resultado_df = CalculadoraMedia.calcular_media(
            ingest, persist, catalog, arquivo_erro=arquivo_erro
        )
        if resultado_df is not None:
            print(resultado_df)
        else:
            print(f"Erro encontrado. Detalhes no arquivo: {arquivo_erro}")

if __name__ == "__main__":
    Main.main()