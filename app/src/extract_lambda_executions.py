import boto3

def obter_tempo_execucao_lambda(nome_funcao_lambda, invocation_id, logs_client):
    try:
        # Obtenha os eventos de log para calcular o tempo de execução
        response = logs_client.get_log_events(logGroupName=f'/aws/lambda/{nome_funcao_lambda}', logStreamName=invocation_id, limit=1, startFromHead=True)
        events = response['events']

        if events:
            start_time = events[0]['timestamp'] / 1000.0  # Converta para segundos
            end_time = events[0].get('ingestionTime') / 1000.0  # Pode usar ingestionTime se o timestamp não estiver disponível
            tempo_execucao = end_time - start_time
            tempo_execucao = round(tempo_execucao, 3)

            return tempo_execucao

    except Exception as e:
        print(f"Erro ao obter tempo de execução: {e}")

    return None

def obter_tempos_ultimas_execucoes(nome_funcao_lambda, num_execucoes=5, regiao='us-east-1'):
    try:
        # Crie um cliente CloudWatch Logs usando o Boto3
        logs_client = boto3.client('logs', region_name=regiao)

        # Liste grupos de logs
        response = logs_client.describe_log_groups(logGroupNamePrefix=f'/aws/lambda/{nome_funcao_lambda}')
        log_groups = response['logGroups']

        # Selecione o grupo de log da função Lambda (assumindo que há apenas um)
        if log_groups:
            log_group_name = log_groups[0]['logGroupName']

            # Liste as invocações recentes da função Lambda
            response = logs_client.describe_log_streams(logGroupName=log_group_name, orderBy='LastEventTime', descending=True, limit=num_execucoes)
            log_streams = response['logStreams']

            # Dicionário para armazenar os tempos de execução
            resultado_lambda_exec = {}
            tempos_execucao_list = []

            for stream in log_streams:
                invocation_id = stream['logStreamName']
                
                # Obtenha o tempo de execução
                tempo_execucao = obter_tempo_execucao_lambda(nome_funcao_lambda, invocation_id, logs_client)

                if tempo_execucao is not None:
                    resultado_lambda_exec[nome_funcao_lambda] = tempos_execucao_list
                tempos_execucao_list.append(tempo_execucao)

            return resultado_lambda_exec

    except Exception as e:
        print(f"Erro ao obter tempos de execução: {e}")
        return None

    
