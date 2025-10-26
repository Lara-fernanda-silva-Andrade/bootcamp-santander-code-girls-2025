entrada = input()

def descrever_lambda_termo(termo):
  if termo == "Lambda Function":
    return "Função executada automaticamente na AWS"

  elif termo == "Trigger":
    return "Evento que dispara uma execução Lambda"

  elif termo == "Runtime":
    return "Ambiente de execução da função"

  elif termo == "Execution Role":
    return "Permissões para a função acessar serviços"

print(descrever_lambda_termo(entrada))