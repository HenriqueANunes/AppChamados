# 📌 Sistema de Chamados — Django + Vue

Este projeto é um sistema completo de abertura e gerenciamento de chamados.  
Ele possui **dois frontends independentes**, cada um com um propósito bem definido, além de uma API central escrita em Django Rest Framework.

---

## 🖥️ 1. Frontend Web (Django Template + Bootstrap) — Atendentes

Interface tradicional renderizada pelo Django.  
Projetada para o time de **atendimento**, onde os chamados são criados e gerenciados de forma rápida e prática.

Funcionalidades:
- Login pelo próprio Django.
- Criação de novos chamados.
- Lista completa dos chamados.
- Filtros por status.
- Acesso rápido e visual simples usando Bootstrap.

Indicado para o pessoal que recebe solicitações e precisa abrir chamados para o time técnico.

---

## 🛠️ 2. Frontend CDN (Vue.js) — Técnicos

Aplicação em Vue 3 que consome a API.  
Criada para os **técnicos**, que precisam atualizar o progresso e o status dos chamados em tempo real.

Funcionalidades:
- Cadastro e login via API.
- Alteração rápida de status dos chamados (Aberto → Em Atendimento → Resolvido etc.).
- Filtragem por status.
- Proteção via token JWT.

Perfeito para quem está executando os atendimentos e precisa de agilidade.

---

## 🧩 Backend (Django + DRF)

A API centraliza toda a lógica do sistema:
- Autenticação
- Criação e listagem de chamados
- Atualização de status via PATCH
- Retorno em JSON
- Permissões separadas para cada frontend

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/HenriqueANunes/AppChamados.git
cd AppChamados
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

## 🌐 Acessos principais

- **Frontend Django (Atendentes):**  
  [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

- **Frontend Vue (Técnicos):**  
  [http://127.0.0.1:8000/vue/login/](http://127.0.0.1:8000/vue/login/)

- **API:**  
  [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
