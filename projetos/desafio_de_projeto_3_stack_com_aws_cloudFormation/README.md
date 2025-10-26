# ☁️ Implementando sua Primeira Stack com AWS CloudFormation



## 📘 Descrição

Este arquivo contém anotações e aprendizados sobre o **implementar a primeira Stack utilizando o AWS CloudFormation**, do módulo *Gerenciamento e governança na AWS*.  
O objetivo foi explorar os conceitos de infraestrutura como código (IaC), criação de templates e automação de recursos na nuvem.  



---

## 📘 Sumário
1. [O que é o AWS CloudFormation](#-o-que-é-o-aws-cloudformation)  
2. [Conceitos Fundamentais](#-conceitos-fundamentais)  
3. [Templates Criados](#-templates-criados)  
4. [Etapas da Implementação](#-etapas-da-implementação)  
5. [Insights e Aprendizados](#-insights-e-aprendizados)  
6. [Conclusão](#-conclusão)

---

## ☁️ O que é o AWS CloudFormation
O **AWS CloudFormation** é um serviço que permite **criar e gerenciar recursos de infraestrutura na AWS de forma automatizada**, usando arquivos de template em formato YAML ou JSON.  
Com ele, é possível provisionar, atualizar e excluir recursos de maneira padronizada, reduzindo erros manuais e garantindo consistência entre ambientes.

---

## 🧩 Conceitos Fundamentais

Durante o laboratório, foram revisados conceitos importantes:

- **Stack** → Conjunto de recursos criados e gerenciados como uma única unidade.  
- **Template** → Arquivo que define os recursos que serão criados (ex.: EC2, Security Group, S3, etc).  
- **Parameters e Outputs** → Permitem personalizar valores e exibir informações após a criação da Stack.  
- **Resources** → Bloco principal onde são definidos os serviços e suas configurações.  
- **IaC (Infrastructure as Code)** → Conceito de tratar infraestrutura como código versionável e automatizado.

---

## 🧱 Templates Criados

Durante o desafio, foram construídos e testados **quatro templates principais**:

### 1️⃣ `ec2.yaml`
Cria uma instância **EC2** do tipo `t2.micro`, configurada para executar um servidor **Apache** automaticamente.  
Inclui:
- Instância EC2 com Amazon Linux 2  
- Script de inicialização (UserData) instalando e iniciando o Apache  
- Associação a um Security Group específico  

### 2️⃣ `apache.yaml`
Template voltado à configuração do **servidor Apache**:
- Instalação e inicialização automática via UserData  
- Criação de uma página HTML simples de teste  

### 3️⃣ `firewall.yaml`
Responsável por definir as **regras de segurança (Security Groups)**:
- Liberação da porta 80 (HTTP) e 22 (SSH)  
- Associação das regras à instância EC2 criada  

### 4️⃣ `ec2_s3_usergroup.yaml`
Define um **usuário e grupo IAM** com permissões de acesso ao S3:
- Criação de usuário IAM  
- Associação a um grupo com política de acesso ao S3  
- Permite interação segura entre EC2 e S3  

---

## ⚙️ Etapas da Implementação

As principais etapas realizadas foram:

1. **Criação e upload dos templates YAML** no CloudFormation.  
2. **Execução de três Create Stack**:
   - Upload e validação do template (`ec2.yaml`, `apache.yaml`, `firewall.yaml`).  
   - Definição de parâmetros como nome da instância e tipo (t2.micro).  
   - Acompanhamento do processo de criação no painel do CloudFormation.  
3. **Verificação dos recursos criados** no EC2 e IAM.  
4. **Testes de conectividade** ao acessar o servidor Apache via IP público.  

---



## 💡 Insights e Aprendizados

Durante a prática, foi possível compreender:

- A importância da **automação da infraestrutura** com CloudFormation.  
- Como os **templates YAML** simplificam a criação e o gerenciamento de recursos.  
- O funcionamento do **UserData** para configurar automaticamente serviços como Apache.  
- O uso de **Stacks interdependentes**, que permitem gerenciar múltiplos componentes de forma modular.  
- A vantagem de **versionar templates** para manter histórico e rastreabilidade das mudanças.  

---


