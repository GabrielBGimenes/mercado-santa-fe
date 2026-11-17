# Mercado Santa Fé — Controle de Estoque e Vendas

Sistema web para apoiar o cadastro de produtos, o acompanhamento do estoque e o registro de vendas do Mercado Santa Fé.

## Objetivo

Organizar as informações de produtos e movimentações, reduzir controles manuais e facilitar a identificação de itens que precisam de reposição.

## Funcionalidades previstas

- Cadastro, edição e consulta de produtos.
- Controle de entradas, saídas e ajustes de estoque.
- Registro de vendas com atualização do estoque.
- Histórico de movimentações.
- Aviso de produtos no nível mínimo ou abaixo dele.
- Acesso autenticado para usuários autorizados.

> **Status:** estrutura inicial do projeto. As funcionalidades serão implementadas e testadas gradualmente. Esta versão inicial inclui a configuração Django, o modelo de Produto e o cadastro/consulta básica de produtos.

## Tecnologias

- Python 3.14
- Django 6.0.x
- Bootstrap 5.3
- PostgreSQL
- Django ORM e Django TestCase

Django 6.0 é compatível com Python 3.12, 3.13 e 3.14. Para PostgreSQL, consulte a versão mínima suportada pela documentação oficial do Django.

## Estrutura

```text
mercado-santa-fe/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── estoque/
│   ├── migrations/
│   ├── templates/estoque/
│   │   ├── base.html
│   │   ├── produto_lista.html
│   │   └── produto_form.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

## Como executar localmente

### 1. Pré-requisitos

Instale Python 3.14 e, se for usar PostgreSQL, instale também o PostgreSQL.

### 2. Criar e ativar o ambiente virtual

Windows (PowerShell):

```powershell
py -3.14 -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Copie `.env.example` para `.env` e ajuste os valores. Não publique o arquivo `.env`.

Para usar PostgreSQL, crie previamente o banco e configure `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` e `DB_PORT`.

Se `DB_NAME` não estiver definido, o projeto utiliza SQLite apenas para facilitar a primeira execução local.

### 5. Criar as tabelas e usuário administrador

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse:

- Aplicação: http://127.0.0.1:8000/
- Administração: http://127.0.0.1:8000/admin/

## Testes

```bash
python manage.py test
```

## Segurança

- Senhas são gerenciadas pelo sistema de autenticação do Django.
- Dados de conexão e chave secreta devem ficar em variáveis de ambiente.
- A validação é realizada no servidor.
- O Django Admin deve ser acessado somente por usuários autorizados.
- Em produção, configurar `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS, cookies seguros e backups.

## Escopo do MVP

O MVP prioriza cadastro e consulta de produtos, movimentações de estoque e registro de vendas. Pagamentos, emissão fiscal, aplicativo nativo e relatórios financeiros avançados não fazem parte da primeira versão.

## Licença

Projeto acadêmico desenvolvido para fins educacionais.

## Objetivo do projeto

O Sistema de Controle de Estoque e Vendas do Mercado Santa Fé tem como objetivo facilitar o gerenciamento de produtos, movimentações de estoque e vendas do estabelecimento.

## Tecnologias utilizadas

- Python
- Django
- Bootstrap
- PostgreSQL
- HTML e CSS

## Funcionalidades previstas

- Cadastro e consulta de produtos.
- Controle de entradas e saídas.
- Registro de vendas.
- Atualização automática do estoque.
- Identificação de produtos com estoque baixo.

## Desenvolvimento

O projeto está sendo desenvolvido em etapas, começando pela estrutura inicial e evoluindo conforme os requisitos definidos para o MVP.
