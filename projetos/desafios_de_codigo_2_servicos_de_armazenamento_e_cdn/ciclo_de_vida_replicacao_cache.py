entrada = input()

def descrever_politica(servico):
  if servico == "Lifecycle Policy":
    return "Regras para mover ou excluir arquivos"

  elif servico == "Cross-Region Replication":
    return "Replica objetos S3 em outra região"

  elif servico == "Cache Behavior":
    return "Define como o CloudFront armazena conteúdo"

  elif servico == "Storage Class":
    return "Define o tipo de armazenamento no S3"

print(descrever_politica(entrada))