# 🚀 Executando Tarefas Automatizadas com Lambda Function e S3

## 📘 Descrição

Este arquivo contém anotações e aprendizados sobre o a **integração de serviços AWS** utilizando **Step Functions, Lambda, S3 e DynamoDB**, do módulo *Automação e DevOps na AWS*.  
O objetivo do desafio foi compreender como **automatizar fluxos de dados** na nuvem, simulando todo o ambiente por meio do **LocalStack**, uma ferramenta que permite executar serviços da AWS localmente.

---

## 📑 Sumário

1. [O que são as Step Functions](#-o-que-são-as-step-functions)
2. [Serviços Utilizados](#-serviços-utilizados)
3. [Estrutura do Fluxo](#-estrutura-do-fluxo)
4. [Funcionamento Detalhado dos Estados](#-funcionamento-detalhado-dos-estados)
5. [Execução Local com LocalStack](#-execução-local-com-localstack)
6. [Aprendizados e Boas Práticas](#-aprendizados-e-boas-práticas)

---

## ⚙️ O que são as Step Functions

O **AWS Step Functions** é um serviço que permite **orquestrar fluxos de trabalho serverless** de maneira visual e lógica.  
Com ele, é possível definir **passos (estados)** que executam funções Lambda, tomam decisões, aguardam eventos ou interagem com outros serviços da AWS.

> 💡 Em outras palavras: o Step Functions funciona como um “roteiro” que descreve **como os serviços devem se comunicar entre si**, garantindo que cada etapa seja executada na ordem e nas condições corretas.

Cada fluxo é descrito em **Amazon States Language (ASL)**, um formato baseado em JSON, que define:
- Estados de execução;
- Condições de decisão (*Choice*);
- Ações a serem tomadas;
- E o ponto final do processo.

---

## 🧩 Serviços Utilizados

Durante o desafio, quatro serviços principais foram utilizados em conjunto:

| Serviço | Função no Fluxo | Descrição |
|----------|----------------|------------|
| **S3 (Simple Storage Service)** | Ponto inicial | Armazena os arquivos a serem processados. O fluxo começa quando há upload de um novo arquivo. |
| **Lambda** | Processamento | Executa o código que lê, valida e grava informações. Representa a “lógica” do sistema. |
| **DynamoDB** | Persistência | Recebe os dados processados e os armazena em uma tabela NoSQL. |
| **Step Functions** | Orquestração | Controla o fluxo de execução entre os serviços, definindo a ordem e as condições de cada etapa. |

---

## 🔄 Estrutura do Fluxo

O fluxo criado no **Step Functions** segue esta sequência lógica de execução:

```text
📤 Upload de Arquivo (S3)
        ↓
🧩 Estado 1: CheckBucketContents (Lambda)
        ↓
🔍 Estado 2: Choice – Verifica se há arquivos
        ├── 🗂️ Se houver arquivos → ProcessFile (Lambda)
        │           ↓
        │     💾 SaveToDynamoDB (Lambda)
        │           ↓
        │     ✅ Success (Fim do fluxo)
        │
        └── 🚫 Se o bucket estiver vazio → EmptyBucketHandler (Lambda)
                    ↓
               ⚠️ End (Encerramento)
```

Esse fluxo representa um **pipeline automatizado**:  
sempre que novos arquivos são adicionados ao bucket S3, eles são detectados, processados e armazenados, sem necessidade de intervenção manual.

---

## 🧠 Funcionamento Detalhado dos Estados

### 🧩 1. CheckBucketContents  
O primeiro estado executa uma **função Lambda** responsável por listar os arquivos existentes no bucket S3.  
O retorno contém o nome e as informações de cada objeto, permitindo que o próximo estado decida o que fazer a seguir.

---

### 🔍 2. Choice (Decisão Lógica)  
Aqui ocorre uma verificação condicional:
- Se o bucket estiver vazio, o fluxo é finalizado.  
- Caso contrário, ele segue para o estado de processamento dos arquivos.

Essa lógica demonstra o uso do **Choice State**, um dos recursos mais poderosos do Step Functions, permitindo **decisões condicionais** dentro de fluxos automáticos.

---

### ⚙️ 3. ProcessFile (Lambda)  
Cada arquivo listado é passado para uma **função Lambda**.  
Essa função lê o conteúdo, aplica validações e transforma os dados no formato adequado para armazenamento no DynamoDB.

> 📘 Nesta etapa, o Lambda representa o “cérebro” do fluxo, aplicando a lógica de negócio necessária.

---

### 🧮 4. Gravação no DynamoDB  
Após o processamento, os dados são persistidos no **DynamoDB**, um banco de dados NoSQL totalmente gerenciado pela AWS.  
Cada item é armazenado em uma tabela com **chaves únicas** e atributos definidos conforme o tipo de dado gerado.

---

### ✅ 5. Finalização do Fluxo  
Por fim, o **Step Functions** marca o estado como concluído.  
Isso garante que todos os passos foram executados com sucesso e permite auditoria do histórico de execução.

## 🧰 Execução Local com LocalStack

Como parte do desafio, todo o ambiente foi **simulado localmente** utilizando o **LocalStack**, uma ferramenta que recria os principais serviços da AWS em um ambiente de desenvolvimento **offline**.


### 🔹 Vantagens do uso do LocalStack

- ✅ Permite testar e validar fluxos **sem custos reais** na AWS.  
- 🔁 Facilita o **desenvolvimento iterativo** (criar, ajustar, testar).  
- 🔒 Garante **isolamento e segurança** em experimentos locais.  

Durante a prática, os testes foram realizados através de **comandos no PowerShell** e no **Postman**, enviando requisições para os endpoints simulados.  
O comportamento dos serviços foi monitorado por meio de **logs** e **respostas JSON** retornadas pelas funções Lambda e pelo próprio Step Functions.

---

## 💬 Aprendizados e Boas Práticas


### 🧠 Principais aprendizados

- 📦 Entender a diferença entre **armazenamento em objetos (S3)** e **banco de dados NoSQL (DynamoDB)**.  
- 🔄 Compreender como o **Step Functions** coordena funções **Lambda** de forma visual e controlada.  
- 🧩 Praticar o uso do **Choice State**, responsável por decisões condicionais no fluxo.  
- 🧱 Aplicar o **LocalStack** como ambiente de testes local confiável.  

---

### ⚙️ Boas práticas observadas

- 🧮 Dividir as **funções Lambda** por responsabilidade (ex: leitura, processamento, gravação).  
- 🪶 Utilizar **logs e mensagens de retorno claras** em cada etapa.  
- 🧪 Testar o fluxo com **diferentes cenários** (bucket vazio, erro de leitura, arquivo válido).  
- 🗂️ **Versionar o fluxo** no repositório GitHub para acompanhamento de evolução.  
