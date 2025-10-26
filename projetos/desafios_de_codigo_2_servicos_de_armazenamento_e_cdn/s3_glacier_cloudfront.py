entrada = input()

def descrever_armazenamento(servico):
  if servico == "Amazon S3 Versioning":
    return "Controle de versões de objetos no S3"

  elif servico == "Amazon CloudFront":
    return "CDN para entrega rápida de conteúdo"

  elif servico == "Amazon Glacier":
    return "Arquivamento de longo prazo com baixo custo"

  elif servico == "Amazon S3":
    return "Armazenamento de objetos na nuvem"

print(descrever_armazenamento(entrada))