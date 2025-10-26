# 📄 Introdução aos Conceitos e Serviços da AWS

Este guia foi elaborado para fornecer os **fundamentos essenciais** e os principais serviços da **Amazon Web Services (AWS)**. Ele serve como uma introdução aos conceitos abordados nos desafios práticos contidos nesta pasta.


***

## 📚 Sumário

1.  [Conceitos Fundamentais da Infraestrutura Global](#1-conceitos-fundamentais-da-infraestrutura-global)
2.  [Modelos de Serviço em Nuvem](#2-modelos-de-serviço-em-nuvem)
3.  [Principais Serviços da AWS](#3-principais-serviços-da-aws)
    * [3.1. Computação](#31-computação)
    * [3.2. Armazenamento](#32-armazenamento)
    * [3.3. Banco de Dados](#33-banco-de-dados)
    * [3.4. Rede e Entrega de Conteúdo (CDN)](#34-rede-e-entrega-de-conteúdo-cdn)
4.  [Segurança e Otimização na AWS](#4-segurança-e-otimização-na-aws)

***

## 1. Conceitos Fundamentais da Infraestrutura Global

A **Amazon Web Services (AWS)** é a principal plataforma de computação em nuvem do mercado, conhecida por sua infraestrutura robusta, alta escalabilidade e um modelo de negócios focado no **pagamento por uso (OPEX)**, em contraste com o modelo tradicional de investimento inicial (**CAPEX**).

A infraestrutura da AWS é projetada para máxima tolerância a falhas e alta disponibilidade:

* **Regiões (Regions):** São áreas geográficas distintas e isoladas. A escolha da Região deve levar em consideração **Compliance**, **Latência**, **Custo** e **Disponibilidade de Serviços**.
* **Zonas de Disponibilidade (AZs - Availability Zones):** São data centers separados fisicamente dentro de uma Região, mas conectados por links de rede de baixa latência. O uso de múltiplas AZs garante **alta disponibilidade** e tolerância a falhas.
* **Pontos de Presença (POPs - Points of Presence):** Locais estratégicos usados para fazer o **caching** de conteúdo (via CloudFront), reduzindo a latência para os usuários finais em todo o mundo.

## 2. Modelos de Serviço em Nuvem

A AWS oferece serviços que se enquadram em diferentes modelos de computação em nuvem, definindo o nível de responsabilidade do cliente:

| Modelo | Sigla | Nível de Controle | Exemplo de Serviço na AWS |
| :--- | :--- | :--- | :--- |
| **Infraestrutura como Serviço** | **IaaS** | O usuário gerencia o S.O., aplicações e dados. | **Amazon EC2** (Máquinas Virtuais) |
| **Plataforma como Serviço** | **PaaS** | O usuário foca na aplicação e nos dados. | Amazon RDS, AWS Lambda |
| **Software como Serviço** | **SaaS** | O usuário apenas utiliza o software final. | Amazon WorkMail |

## 3. Principais Serviços da AWS

### 3.1. Computação

* **Amazon EC2 (Elastic Compute Cloud):**
    * São as **máquinas virtuais (Instâncias)** da AWS, classificadas como IaaS.
    * Uma instância é composta por: CPU, Memória, Disco, Rede e Sistema Operacional (Windows ou Linux).
    * **Tipos de Preços (Foco em Custo):**
        * **Sob Demanda:** Taxa fixa por hora; ideal para cargas de trabalho irregulares e testes.
        * **Instâncias Reservadas:** Exigem compromisso de uso (1 ou 3 anos) em troca de um custo menor.
        * **Instâncias SPOT:** Oferecem até 90% de desconto, ideais para cargas de trabalho tolerantes a falhas, mas podem ser encerradas pela AWS a qualquer momento.

### 3.2. Armazenamento

* **Amazon S3 (Simple Storage Service):**
    * Serviço de **armazenamento de objetos** em nuvem (backups, logs, *assets* de sites).
    * Escalável, seguro e permite **Regras de Ciclo de Vida** para mover objetos automaticamente para classes de *storage* mais baratas (como Glacier), otimizando custos.
* **Amazon EBS (Elastic Block Store):**
    * Serviço de **armazenamento em bloco** de alta performance e confiabilidade.
    * Funciona como um "HD externo" que é **anexado** a uma instância EC2, ideal para armazenar bancos de dados e logs de sistema.

### 3.3. Banco de Dados

* **Amazon DynamoDB:**
    * Um serviço de **Banco de Dados NoSQL** totalmente gerenciado.
    * Oferece escalabilidade e desempenho de baixa latência em qualquer escala, sendo ideal para dados não estruturados ou semiestruturados. Usado por empresas como Netflix e Airbnb.

### 3.4. Rede e Entrega de Conteúdo (CDN)

* **Amazon CloudFront:**
    * É a **Rede de Entrega de Conteúdo (CDN)** da AWS.
    * Reduz a latência e melhora o desempenho, armazenando em **cache** cópias de recursos estáticos (imagens, vídeos, CSS, JS) nos **Pontos de Presença (POPs)** mais próximos aos usuários.

## 4. Segurança e Otimização na AWS

### 🔒 Segurança (Práticas Fundamentais)

* **Conta Root:** Possui super permissões e deve ser protegida e evitada para tarefas diárias.
* **MFA (Autenticação Multifator):** Uso obrigatório para a conta root e usuários importantes.
* **IAM (Identity and Access Management):** Serviço para gerenciar identidades, usuários, grupos e **políticas de acesso**, aplicando o princípio de menor privilégio.

### 💸 Otimização de Custo (Otimização de Recurso)

* **Estratégias de Redução de Custo:**
    * Desligar instâncias não utilizadas em ambientes de desenvolvimento e teste (períodos noturnos/finais de semana).
    * Remover recursos ociosos.
    * **Escalabilidade Vertical:** Aumentar ou diminuir os recursos de um único nó (vCPUs/Memória) para lidar com picos.
    * **Escalabilidade Horizontal:** Adicionar mais recursos (mais instâncias, mais discos) para suportar o crescimento da aplicação.