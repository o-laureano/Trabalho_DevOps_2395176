# **Documentação do Projeto**

**Autor**: Henrique Laureano de Souza
**RA**: 239517-6

---

## **Visão Geral**

Este projeto automatiza a criação de um ambiente de monitoramento com o Grafana, configurado para exibir um dashboard que rastreia requisições de um servidor Prometheus. A solução integra o Jenkins para gerenciar todo o pipeline de execução.

---

## **Requisitos do Sistema**

1. **Jenkins** em execução.
2. **Docker** e **Docker Compose** configurados no servidor Jenkins.
3. Navegador para acessar o Grafana em `http://localhost:3000`.

---

## **Guia de Configuração e Execução**

### **1. Inicializar o Jenkins**

- Certifique-se de que o Jenkins está ativo. O acesso padrão é em `http://localhost:8080`.

---

### **2. Criar uma Pipeline no Jenkins**

1. **Acessar o Jenkins**

   - Navegue para `http://localhost:8080` e faça login.

2. **Criar um Novo Item**

   - Clique em **"Nova Tarefa"**.
   - Insira um nome para a pipeline, como `Pipeline-Grafana`.
   - Escolha a opção **"Pipeline"** e clique em **"OK"**.

3. **Configurar o Pipeline**

   - Na seção **Build Triggers**, habilite a opção **Consultar periodicamente o SCM**.
   - Use o agendamento `H/5 * * * *` para verificar atualizações no repositório a cada 5 minutos.
   - Na seção **Pipeline**, selecione **Pipeline Script from SCM**.

4. **Configurar Repositório SCM**
   - Em **SCM**, escolha **Git**.
   - Insira o URL do repositório do projeto:  
     `https://github.com/GabNasci/trabalho-devops-2397834.git`.
   - Adicione credenciais, se necessário.
   - Clique em **Salvar**.

---

### **3. Executar a Pipeline**

1. Retorne à página inicial do Jenkins e selecione a pipeline criada.
2. Clique em **"Construir Agora"** para iniciar a execução.
3. Monitore a execução:
   - Acompanhe os logs para garantir que os containers Docker (Prometheus e Grafana) sejam provisionados com sucesso.
   - Certifique-se de que o log final confirma a execução do Grafana.

---

### **4. Acessar o Grafana**

1. No navegador, acesse `http://localhost:3000`.
2. Faça login no Grafana com as seguintes credenciais padrão:
   - **Usuário**: `admin`
   - **Senha**: `admin` (ou a senha definida no ambiente).
3. Explore o dashboard provisionado automaticamente para visualizar as métricas monitoradas.

---

## **Resumo das Etapas**

1. Inicialize o Jenkins.
2. Configure uma nova pipeline no Jenkins conforme as instruções.
3. Execute a pipeline para provisionar os serviços.
4. Acesse o Grafana em `http://localhost:3000` e analise os dados no dashboard.

---

**Dúvidas ou problemas? Entre em contato!** 😊
