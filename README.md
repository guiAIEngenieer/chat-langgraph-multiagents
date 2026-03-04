# Chat Multiagente com LangGraph e Gemini

Este projeto implementa um chat inteligente multiagente utilizando **LangGraph**, **LangChain** e o modelo **Gemini**, com:

- Roteamento automático da conversa para o setor mais adequado (suporte técnico, contabilidade ou marketing).
- Memória de conversa por sessão, para que o agente lembre do contexto ao longo do diálogo.
- Uma arquitetura em grafo de estados, simples de entender e fácil de evoluir.

A ideia é simular um atendimento em que, a partir da primeira pergunta, o sistema decide qual “especialista” deve responder, e mantém a conversa com esse mesmo agente até o fim da sessão.

---

## O que este projeto faz?

Este projeto cria um sistema de IA conversacional capaz de:

- Ler a mensagem do usuário e identificar automaticamente o setor mais adequado:
  - `technician` → suporte técnico 
  - `accountant` → contabilidade 
  - `marketing` → marketing 

- Roteia a primeira mensagem para o agente correto usando um nó de roteamento (`router`).
- Fixa o agente escolhido para o restante da sessão, evitando ficar trocando de setor a cada nova pergunta.
- Mantém o histórico da conversa por `session_id`, usando `RunnableWithMessageHistory` do LangChain.
- Usa o modelo **Gemini** para gerar respostas naturais e contextualizadas a partir desse histórico.

---

## Como funciona o roteamento e a memória?

### Na primeira mensagem da sessão:

- O grafo chama o nó `node_router`.
- Um chain de classificação (`chain_router`) usa o Gemini para decidir se a conversa é:
  - técnico  
  - contábil  
  - marketing  

- O setor escolhido é salvo no `SessionManager` junto com o `session_id`.

### Nas próximas mensagens da mesma sessão:

- O `node_router` verifica se já existe um setor salvo para aquele `session_id`.
- Se existir, não chama mais o modelo para decidir: apenas reutiliza o mesmo setor.
- A conversa segue sempre com o mesmo agente, que tem acesso ao histórico de mensagens dessa sessão.

Assim, você tem um atendimento contínuo, com contexto mantido e especialização por área.

---

## Tecnologias utilizadas

- Python  
- LangChain e LangGraph 
- Google Gemini (`gemini-2.5-flash`)
- `RunnableWithMessageHistory` para memória de conversa por sessão  
- Gerenciamento simples de sessão em memória via `SessionManager`  

---

## Como rodar o projeto?

### Antes de começar:

- Tenha o **Python 3.10+** instalado.
- Use uma IDE de sua preferência (VSCode, PyCharm, Cursor, etc.).

---

### 1. Clonar o repositório

```bash
git clone <url-do-repo>
cd IA-LangGraph
```
---

## 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configurar a API Key do Gemini

1. Crie uma API Key em:  
   https://aistudio.google.com  
   (Google AI Studio)

2. No projeto, defina a variável de ambiente usada em `app/settings.py`  
   (por exemplo `GEMINI_API_KEY`) ou configure o `.env` de acordo com esse arquivo.

3. Verifique se o logger está indicando:

```text
GEMINI_API_KEY configured
```

ao iniciar o projeto.

---

## 5. Ajustar o `SESSION_ID` (opcional para testes locais)

No arquivo `app/config/constants.py`:

```python
SESSION_ID = "Teste"
```

Para testes simples via terminal, você pode manter um valor fixo.

Em um cenário real, esse valor pode ser trocado por um ID único por usuário/aba/sessão.

---

## 6. Iniciar o chat

No terminal, na raiz do projeto:

```bash
py -m app.main
```

Você verá algo como:

```text
prompt:
```

Digite sua pergunta (por exemplo):

- Quero falar sobre a minha conta bancária  
- Estou com um problema no meu computador  
- Preciso de ajuda para divulgar meu produto  

O sistema vai:

- Roteá-la automaticamente para o setor correto.
- Escolher o agente especializado.
- Manter o histórico da conversa com esse mesmo agente durante toda a sessão.

Para sair, basta digitar:

```text
sair
```

--- 

## Agradecimentos

Fala, pessoal! 

É com muita satisfação que compartilho a publicação de mais um projeto, desenvolvido com o objetivo de demonstrar na prática tudo o que venho aprendendo até aqui.

Trata-se de um projeto simples, mas que representa um grande avanço na minha jornada com LangGraph e LangChain. Nele, aplico conceitos como grafos de estados, nodes e chains para construir uma IA capaz de analisar o contexto da conversa e decidir automaticamente qual especialista é mais adequado para responder.

Desenvolvi esse projeto também como forma de consolidar o conhecimento adquirido no curso da Alura que concluí recentemente: “LangChain e Python: criando ferramentas com a OpenAI”. Colocar a teoria em prática foi essencial para fortalecer meu entendimento e ganhar mais segurança na construção de aplicações com IA.

Esse projeto reforçou muitos conhecimentos adquiridos no meu primeiro desenvolvimento e, ao mesmo tempo, me proporcionou novos aprendizados sobre a arquitetura e as possibilidades do ecossistema LangChain/LangGraph.

Agradeço de verdade a quem tirar um tempo para conhecer o projeto 
Fico totalmente aberto a feedbacks e sugestões. Vamos juntos evoluir e crescer cada vez mais na área de IA! 
