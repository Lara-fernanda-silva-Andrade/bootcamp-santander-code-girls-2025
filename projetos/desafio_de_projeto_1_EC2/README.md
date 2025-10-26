# ☁️ Gerenciando Instâncias EC2 na AWS

## 📘 Descrição

Este arquivo contém anotações e aprendizados sobre o **Amazon EC2 (Elastic Compute Cloud)**, do módulo *Computação na Nuvem com EC2*.  
O objetivo é consolidar o entendimento sobre o funcionamento das instâncias EC2, o gerenciamento de armazenamento com **EBS**, o uso do **S3** e as estratégias de **otimização de custos e desempenho** na AWS.

---

## 📑 Sumário

1. [O que é o Amazon EC2](#-o-que-é-o-amazon-ec2)
2. [Gerenciamento e Segurança](#-gerenciamento-e-segurança)
3. [Armazenamento: Amazon EBS](#-armazenamento-amazon-ebs)
4. [Armazenamento Complementar: Amazon S3](#-armazenamento-complementar-amazon-s3)
5. [Otimização de Recursos na AWS](#-otimização-de-recursos-na-aws)
6. [Boas Práticas para EC2](#-boas-práticas-para-ec2)
7. [Insights Pessoais e Aprendizados](#-insights-pessoais-e-aprendizados)

---



## ☁️ O que é o Amazon EC2

O **Amazon EC2 (Elastic Compute Cloud)** é o serviço de **máquinas virtuais** da AWS, que permite criar e gerenciar servidores (instâncias) configuráveis de acordo com as necessidades da aplicação.

Cada instância EC2 é composta por:
- 🧮 **CPU**
- 💾 **Memória**
- 🧱 **Disco (EBS)**
- 🌐 **Rede**
- ⚙️ **Sistema Operacional (Linux ou Windows)**

> 💡 **Tipo de serviço:** *IAAS* (*Infrastructure as a Service*)  
> A responsabilidade do usuário é gerenciar os aplicativos, dados e conexões dentro da instância.

---

## ⚙️ Gerenciamento e Segurança

Ao criar uma instância EC2, é possível configurar diversos parâmetros importantes para o controle e segurança do ambiente:

- **Imagem de Máquina (AMI):** Define o sistema operacional e os softwares base da instância.  
- **Tipo da Instância:** Determina a combinação de CPU, memória, rede e armazenamento (ex: `t2.micro`, `m5.large`).  
- **Grupos de Segurança (Security Groups):** Funcionam como um *firewall virtual*, controlando portas, protocolos e IPs de acesso.  
- **Par de Chaves (Key Pair):** Permite autenticação segura via SSH (Linux) ou RDP (Windows).

Essas configurações são fundamentais para garantir **segurança, performance e escalabilidade** no ambiente de nuvem.

---

## 💽 Armazenamento: Amazon EBS

O **Amazon EBS (Elastic Block Store)** é um serviço de **armazenamento em blocos** altamente confiável, utilizado pelas instâncias EC2.  
Ele funciona como um **HD externo virtual**, que pode ser anexado e removido facilmente.

### 🔹 Características principais:
- Alta confiabilidade e performance.  
- Capacidade de expansão rápida.  
- Persistência dos dados mesmo após desligar a instância.  
- Flexibilidade para anexar volumes em diferentes instâncias.

### 🔹 Exemplos de uso:
- Armazenamento de **bancos de dados** como MySQL, PostgreSQL e Oracle.  
- Armazenamento de **dados de aplicações web** e **logs de sistema**.  

Com o EBS, é possível criar novas partições, ajustar o tamanho do volume e garantir que os dados estejam sempre disponíveis para a aplicação.

---

## 🧰 Armazenamento Complementar: Amazon S3

O **Amazon S3 (Simple Storage Service)** é o serviço de **armazenamento de objetos** da AWS.  
Ideal para armazenar grandes volumes de dados, oferece **segurança, durabilidade e escalabilidade**.

### 🔹 Características:
- Armazenamento baseado em objetos (arquivos, imagens, logs, backups).  
- Permite organizar e recuperar dados de forma simples.  
- Oferece diferentes **classes de armazenamento**, otimizando custos conforme a frequência de acesso.  

### 🔹 Exemplo prático:
Resultados de exames médicos podem ser armazenados inicialmente no **S3 Standard** (acesso frequente) e, após um tempo, migrar automaticamente para o **S3 Glacier** (acesso eventual) através de **regras de ciclo de vida (Lifecycle Rules)**.

---

## 💡 Otimização de Recursos na AWS

Otimizar recursos significa **aumentar eficiência e reduzir custos** na nuvem.  
Mesmo pequenas ações podem gerar grande economia ao longo do tempo.

### 🔹 1. Desligar instâncias não utilizadas
- Em ambientes de **teste, desenvolvimento ou treinamento**, desligue as instâncias fora do horário de uso (noite e fins de semana).  
- Isso reduz custos sem afetar o desempenho do ambiente produtivo.

### 🔹 2. Remover recursos ociosos
- Revise regularmente **volumes EBS**, **snapshots**, **instâncias** e **endereços IP elásticos**.  
- Recursos parados continuam sendo cobrados, é como pagar aluguel de um carro parado na garagem.

### 🔹 3. Escalar recursos conforme a demanda
Existem duas formas principais de escalonamento:

- **Escalonamento Vertical:** Aumentar CPU, memória ou armazenamento de uma instância existente.  
- **Escalonamento Horizontal:** Adicionar novas instâncias para dividir a carga de trabalho.

Ambas ajudam a lidar com picos de consumo, mantendo o custo sob controle.

### 🔹 4. Tipos de instâncias e custo

| Tipo | Descrição | Uso Recomendado |
|------|------------|----------------|
| **On-Demand** | Pagamento por hora. Flexibilidade total. | Testes e workloads imprevisíveis. |
| **Reservadas** | Pagamento anual com desconto. | Ambientes estáveis e contínuos. |
| **Spot** | Descontos de até 90%, mas podem ser interrompidas. | Processos tolerantes a falhas. |

Essas opções permitem alinhar custo e desempenho de acordo com o perfil de uso da aplicação.

---

## 🧾 Boas Práticas para EC2

- 🔐 Configure **grupos de segurança** com o mínimo de portas abertas.  
- 🕵️ Use **CloudWatch** para monitorar uso, métricas e alertas de performance.  
- 🧮 Utilize **Auto Scaling** para ajustar a capacidade automaticamente conforme a demanda.  
- 🧑‍💼 Atribua **IAM Roles** às instâncias com o princípio de menor privilégio.  
- 💾 Faça **backups regulares** com snapshots do EBS.  
- ⚠️ Evite deixar portas **22 (SSH)** ou **3389 (RDP)** abertas ao público.  
- 📉 Faça análises periódicas de custo e uso com o **AWS Cost Explorer**.

---

## 💬 Insights Pessoais e Aprendizados

Durante a prática com o EC2, ficou evidente que este serviço é o **núcleo da infraestrutura AWS**, servindo como base para diversas soluções em nuvem.  
A combinação entre EC2, EBS e S3 permite criar **ambientes completos, escaláveis e resilientes**.  

Aprender sobre **otimização de custos** foi essencial para compreender a importância de monitorar e ajustar recursos de forma inteligente.  
Registrar este aprendizado no GitHub torna o processo de estudo mais sólido e cria um material de referência para futuras implementações.

---

