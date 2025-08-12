# Versionamento
- Esse documento tem como função a organização do versionamento do sistema Anser Diary. 

## 1. Major commit (21/07/2025) "Preparação de ambiente, estruturação de repositório, configuração inicial do banco de dados SQLite e documentação":

- Feito a documentação dos requisitos funcionais <a href='/docs/requisitos_funcionais.md'>Requisitos Funcionais</a>
- Feito o documento de organização de versionamento <a href='/docs/versionamento.md'>Versionamento</a>
- Feito README com a introdução do sistema "Anser_Diary" e instruções para execução local <a href='/README.md'>README</a>
- Feito a estruturação do repositório
- Feito a configuração do banco de dados SQLite

## 2. Major commit (29/07/2025) "Implementação das páginas principais, segurança de dados e backend para login, logout e register":

- Feito página de Home page, registro, login, logout, header e footer com implmentação de Templates com extends/includes
- Feito implementação geral do banco de dados na area do usuário
- Feito segurança de dados com implementação de senhas com hash seguros  
- Feito login, logout e registro funcionais
- Utilizado Flask-Login para manter usuário autenticado

## 3. Major commit (05/08/2025) "Implementação do CRUD parcialmente completo"

- Feito as funções de criar, editar e deletar diários
- Feito as funções de criar, editar e deletar usuários
- Feito a funcionalidade de publicação dos diários
- Feito a funcionalidade de visualização de profiles de outros usuários
- Feito a funcionalidade de visualização de diários de outros usuários

## 3.1. Minor commit (10/08/2025) "Finalizado a implementação do CRUD e mudança da estrutura dos templates"

- Corrigido bugs em relação ao CRUD
- Implementação do footer.html e header.html direto na base.html
- Adição da logo

## 4. Major commit (12/08/2025) "Implementação de estilo, páginas de erro personalizadas e melhoria no README"

- Feito o `main.css` com estilo de todas as páginas
- Feito páginas de erro personalizadas com `@app.errorhandler()`
- Modificação geral nas páginas html
- Reorganização de caminhos bugados no README