# Documento de Requisitos Funcionais - Anser_Diary

**Tema** Sistema para criar Diários virtuais.


## 1. Cadastro e autenticação

- **RF01**: Usuário poderá criar sua conta com e-mail e senha.
- **RF02**: Usuário poderá fazer login/logout na sua conta.
- **RF03**: Senhas serão armazenadas com hash seguro (*werkzeug security*).


## 2. Gerenciamento dos recursos

- **RF04**: Usuário poderá criar um diário, informando o nome do diário (opcional).
- **RF05**: Usuário poderá visualizar todos os diários que ele criou.
- **RF06**: Usuário poderá editar o conteúdo de seus diários .
- **RF07**: Usuário poderá excluir um diário de sua lista de diários.
- **RF08**: Usuário poderá editar informações do perfil, como nome e outros dados pessoais.
- **RF09**: Usuário poderá visualizar seu perfil conforme atualizações.
- **RF10**: Usuário poderá escolher quais de seus diários serão públicos.


## 3. Banco de Dados

- **RF11**: Usar SQLite para armazenar dados do usuário, nome dos diários, descrição etc, separando em duas tabelas, uma para as informações do usuário e outra para os conteúdos dos diários.


## 4. Templates e navegação

- **RF12**: Uso de `extends` e `includes` para layout base.
- **RF13**: Página inicial (Home Page) apresentando o sistema e com opção de login e cadastro.
- **RF14**: Página pessoal do usuário com seus diários e suas informações pessoais.
- **RF15**: Página de edição e criação de diários.
- **RF16**: Páginas de erro personalizadas (404 e 500).


## 5. Requisitos Técnicos

- **RF17**: Uso de `request` para os formularios de cadastro, login e criaçã de diários.
- **RF18**: Uso de `url_for` e `redirect` para navegação.
- **RF29**: Uso de `make_response` para cookies.
- **RF20**: Código versionado no GitHub.
- **RF21**: README detalhado com instruções de instalação, dependências e capturas de telas.
