# 🧱 Gerenciando Infraestrutura com AWS CloudFormation

## 📘 Descrição

Este arquivo contém anotações e aprendizados sobre o **AWS CloudFormation**, do módulo *Desenvolvimento e Ferramenta*.  
O objetivo é consolidar o entendimento sobre como **modelar, criar e gerenciar recursos na AWS automaticamente** usando templates (JSON/YAML).  


---

## 📑 Sumário

1. [O que é o AWS CloudFormation](#-o-que-é-o-aws-cloudformation)  
2. [Benefícios do CloudFormation](#-benefícios-do-cloudformation)  
3. [Formatos de Templates (JSON e YAML)](#-formatos-de-templates-json-e-yaml)  
4. [Infraestrutura como Código (IaC)](#-infraestrutura-como-código-iac)  
5. [Criação da Stack no Console AWS](#-criação-da-stack-no-console-aws)  
6. [Diferença entre CloudFormation e Terraform](#-diferença-entre-cloudformation-e-terraform)  
7. [Insights Pessoais e Aprendizados](#-insights-pessoais-e-aprendizados)

---

## ☁️ O que é o AWS CloudFormation

O **AWS CloudFormation** é um serviço que permite **definir toda a infraestrutura AWS em arquivos de template (JSON ou YAML)** e provisionar automaticamente os recursos descritos.  
Ao invés de criar manualmente EC2, RDS, S3, Security Groups e outros serviços, descrevemos tudo em código e o CloudFormation gerencia a criação, dependências e ordem de provisionamento.

### Componentes principais de um template
- **Resources:** definição dos recursos (ex.: `AWS::EC2::Instance`, `AWS::RDS::DBInstance`).  
- **Parameters:** entradas para customizar a stack (ex.: tipo de instância, usuário do BD).  
- **Mappings:** tabelas de valores por região/ambiente.  
- **Outputs:** valores retornados após a criação (ex.: IP público, endpoint RDS).  
- **Conditions:** criação condicional de recursos.

---

## ⚙️ Benefícios do CloudFormation

- 🤖 **Automação:** provisionamento e configuração automáticos.  
- 🔒 **Segurança:** aplicação consistente de políticas e integração com IAM.  
- 💰 **Economia de custos:** reaproveitamento de templates e redução de erros humanos.  
- 🧱 **Consistência e padronização:** ambientes idênticos entre dev/test/prod.  
- 🔁 **Reprodutibilidade:** recriação da infraestrutura com o mesmo template sempre que necessário.

---

## 🧾 Formatos de Templates (JSON e YAML)

O CloudFormation aceita **JSON** e **YAML**. YAML costuma ser preferido pela legibilidade.

### Exemplo JSON
```json
{
  "Resources": {
    "MyInstance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t2.micro",
        "ImageId": "ami-12345678"
      }
    }
  }
}
```

### Exemplo YAML
```YAML
Resources:
  MyInstance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-12345678"
```

## 🧰 Infraestrutura como Código (IaC)

**IaC (Infrastructure as Code)** significa tratar a infraestrutura como software: versionar templates, revisar por PR, auditar mudanças e automatizar deploys.

### 🔹 Vantagens práticas:
- Controle de versão (Git).  
- Reprodutibilidade e rollback.  
- Integração com pipelines CI/CD.  
- Menor risco de configuração manual inconsistente.  

O **Infrastructure Composer** é uma ferramenta visual no console AWS que permite montar a arquitetura (Canvas) e gerar o template em YAML, facilitando o aprendizado e a prototipagem.

---

## 🚀 Criação da Stack no Console AWS

### Passos seguidos na prática:
1. Acessar **CloudFormation** no console AWS.  
2. Clicar em **Create stack → With new resources (standard)**.  
3. Selecionar o template (upload do YAML gerado pelo Composer ou URL).  
4. Preencher **Parameters** (ex.: `InstanceType`, `DBUser`, `DBPassword`, `KeyName`).  
5. Revisar configurações (tags, permissões IAM, rollback) e criar a stack.  
6. Acompanhar eventos até o status **CREATE_COMPLETE**.

### 🧩 Trecho de exemplo (parâmetro `InstanceType` com `AllowedValues`):

```yaml
Parameters:
  InstanceType:
    Description: Tipo de instância EC2
    Type: String
    Default: t2.small
    AllowedValues:
      - t2.nano
      - t2.micro
      - t2.small
      - t2.medium
    ConstraintDescription: Deve ser um tipo de instância válido

```

## ⚖️ Diferença entre CloudFormation e Terraform

| Aspecto | CloudFormation | Terraform |
|----------|----------------|------------|
| **Provedor** | Exclusivo AWS | Multi-cloud (AWS, Azure, GCP...) |
| **Linguagem** | JSON / YAML | HCL |
| **Estado** | Gerenciado pela AWS | Estado gerenciado local/remote (S3, etc.) |
| **Integração** | Nativa com serviços AWS | Requer providers |
| **Interface** | Infrastructure Composer (visual) | Sem IDE visual nativo |

---

## 💬 Insights Pessoais e Aprendizados

Durante a prática, ficou claro que o **CloudFormation** facilita a padronização e a automação de ambientes.

### 🔹 Pontos observados:
- O **Infrastructure Composer** ajuda a visualizar dependências antes de gerar o YAML.  
- Parâmetros e outputs tornam os templates reutilizáveis entre ambientes.  
- Testar templates em uma conta sandbox evita custos inesperados.  

> 💭 “CloudFormation permite transformar o desenho da arquitetura em um arquivo reproduzível — isso muda como você pensa a infraestrutura.”

---
