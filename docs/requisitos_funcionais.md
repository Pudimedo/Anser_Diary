# Documento de Requisitos Funcionais - Diario_Virtual

**Tema** Sistema para criar Diários virtuais.


## 1. Cadastro e autenticação

- **RF01**: Usuário poderá criar sua conta com e-mail e senha.
- **RF02**: Usuário poderá fazer login/logout na sua conta.
- **RF03**: Senhas serão armazenadas com hash seguro (*werkzeug security*).


## 2. Gerenciamento dos recursos

- **RF04**: Usuário poderá criar um diário, informando o nome do diário e descrição (opcional).
- **RF05**: Usuário poderá visualizar todos os diários que ele criou.
- **RF06**: Usuário poderá editar o conteúdo de seus diários .
- **RF07**: Usuário poderá excluir um diário de sua lista de diários.
- **RF08**: Usuário poderá adicionar fotos nos seus diários.
- **RF09**: Usuário poderá editar informações do perfil, como nome, foto e outros dados pessoais.
- **RF10**: Usuário poderá visualizar seu perfil conforme atualizações.
- **RF11**: Usuário poderá escolher quais de seus diários serão públicos 


## 3. Banco de Dados

- **RF12**: Usar SQLite para armazenar dados do usuário, nome dos diários, descrição etc, separando em duas tabelas, uma para as informações do usuário e outra para os conteúdos dos diários.


## 4. Templates e navegação

- **RF13**: Uso de `extends` e `includes` para layout base.
- **RF14**: Página inicial (Home Page) apresentando o sistema e com opção de login e cadastro.
- **RF15**: Página pessoal do usuário com seus diários e suas informações pessoais.
- **RF16**: Página de edição e criação de diários.
- **RF17**: Páginas de erro personalizadas (404 e 500).


## 5. Requisitos Técnicos

- **RF18**: Uso de `request` para os formularios de cadastro, login e criaçã de diários.
- **RF19**: Uso de `url_for` e `redirect` para navegação.
- **RF20**: Uso de `make_response` para cookies.
- **RF21**: Código versionado no GitHub.
- **RF22**: README detalhado com instruções de instalação, dependências e capturas de telas.
