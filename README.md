## 🗂️ Estrutura do Projeto — Matéria de PSI

📁 Sistema de Projetos IF/         ← Pasta principal do projeto  
├── 📁 ambiente/                   ← Ambiente virtual 
├── 📁 static/                     ← Arquivos estáticos (CSS, imagens, etc.)  
│   └── 📄 base.css                ← Arquivo principal de estilos  
|   └── 📄 cadastrarprojetos.css   ← Estilo para cadastro dos projetos  
|   └── 📄 index.css               ← Estilo para da página inicial  
|   └── 📄 logincadastro.css       ← Estilo para os formulários de login e cadastro de usuários
|
├── 📁 templates/                  ← Páginas HTML da aplicação  
│   ├── 📄 404.html                ← Página para erro 404
│   ├── 📄 500.html                ← Página para 500 
│   ├── 📄 base.html               ← Template base de toda a aplicação
│   ├── 📄 cadastrar_pessoa.html   ← Página de cadastro de pessoa  
│   ├── 📄 cadastrar_projeto.html  ← Página de cadastro de projeto 
│   ├── 📄 editar_projeto.html     ← Página para editar um projeto existente
|   ├── 📄 index.html              ← Página inicial    
|   ├── 📄 login.html              ← Página de login   
│   ├── 📄 logout.html             ← Página de sair  
│   ├── 📄 meus_projetos.html      ← Página que lista os projetos do usuário logado
│   ├── 📄 projetos.html           ← Página de visualização de projetos 
│   ├── 📄 sobre.html              ← Página de detalhes sobre criadores e sobre o projeto
│
├── 📄 app.py                      ← Arquivo principal da aplicação Flask  
├── 📄 banco.py                    ← Página onde é criado o banco de dados
├── 📄 database.py                 ← Página de conexão com o banco de dados
├── 📄 jogo.db                     ← Página onde é armazenado todos os dados do sistema
├── 📄 README.md                   ← Arquivo de instruções/documentação do projeto
├── 📄 schema.sql                  ← Arquivo que define as tabelas usuarios e projetos 
├── 📄 requirements.txt            ← Lista de dependências da aplicação


# Sistema de Projetos IF

O **Sistema de Projetos IF** é uma aplicação web desenvolvida em **Flask** que permite aos usuários cadastrar, visualizar, editar e excluir projetos acadêmicos de forma prática, organizada e segura. Cada usuário possui controle total sobre seus projetos, podendo registrar informações como título e descrição, garantindo personalização e acompanhamento detalhado de cada atividade. O sistema oferece uma interface simples e intuitiva, construída com **HTML, CSS** e **templates Jinja2**, que permite a renderização dinâmica das páginas. Funcionalidades importantes, como edição e exclusão de projetos, incluem confirmações antes de ações críticas, protegendo os dados contra alterações acidentais. As informações são armazenadas em um banco de dados **SQLite**, e a segurança das senhas é garantida por hashing, seguindo boas práticas de desenvolvimento web. O projeto também adota separação de templates, uso de rotas específicas para **GET** e **POST** e validação de dados, proporcionando uma experiência confiável e organizada. O objetivo principal é facilitar o gerenciamento de projetos acadêmicos, centralizando todas as informações em um único sistema, permitindo que estudantes e acadêmicos acompanhem de forma eficiente o progresso de suas atividades, mantendo registros claros e acessíveis.

---

## Tecnologias e Dependências
- **Linguagem de Programação:** Python  
- **Framework Web:** Flask  
- **Banco de Dados:** SQLite  
- **Templates:** Jinja2  
- **Frontend:** HTML, CSS  
- **Segurança:** Werkzeug (para hashing de senhas)  

---

## Configuração Local

### Pelo GitHub
1. Acesse o repositório do projeto: [Link do GitHub](https://github.com/TaynnaMontello/Projeto_Atualizado.PSI.git)  
2. Clique em **Code → Download ZIP**  
3. Salve o arquivo no seu computador e extraia o conteúdo em uma pasta  

### Abrir o projeto
No terminal, navegue até a pasta onde você extraiu o projeto:
cd caminho/para/pasta-do-projeto

### Criar e ativar ambiente virtual
python -m venv nome_do_ambiente

### Para ativar o ambiente virtual:
### Windows:
nome_do_ambiente\Scripts\activate

### Instalar dependências
pip install -r requirements.txt

### Rodar a aplicação
python app.py
# ou 
python flask run --debug

### Acessar pelo navegador
### Abra o navegador e digite:
http://localhost:5000

### Uso do Sistema
O sistema permite aos usuários gerenciar projetos acadêmicos de forma prática e organizada.

### Funcionalidades Principais
Cadastrar Projeto
Adicionar um novo projeto preenchendo título e descrição
Cada projeto fica associado ao usuário que o cadastrou
Visualizar Projetos
Ver a lista de todos os projetos cadastrados
### Caso não haja projetos, o sistema informa que a lista está vazia
Editar Projeto
Alterar o título ou a descrição de um projeto existente
### Apenas o usuário dono do projeto pode modificar
Excluir Projeto
Remover projetos que não são mais necessários
Confirmar antes de excluir para evitar perdas acidentais

### Exemplo de Uso
Faça login ou cadastre-se no sistema
Clique em “Cadastrar Projeto” e preencha os dados
Visualize os projetos na lista principal
Para alterar um projeto, clique em Editar
Para remover um projeto, clique em Excluir e confirme
Para voltar à página inicial, clique em Sistema de Projetos IF

### Vídeo de Uso
Vídeo de Uso - Sistema de Projetos IF (https://youtu.be/EvOnI5spdJ8)

### Contribuições da Equipe
Integrante	Contribuições
Alex Bruno	Implementou a funcionalidade de exclusão de projetos, contribuiu no CSS da interface e desenvolveu a rota da página inicial (index).
Kessya Cauanny	Desenvolveu as rotas cadastrar_pessoa e lembrar_usuario, construiu a estrutura do projeto e implementou a documentação do README.
Ludimila Erika	Implementou funcionalidades de login e logout, criou as páginas de erro 404 e 500 e funcionalidades relacionadas a projetos.
Taynná Montel	Atualizou o projeto e fez correções, contribuiu para o cadastro de pessoas, criou a rota projetos/novo, desenvolveu o banco de dados e escreveu o documento do projeto.
Marcos Cassiano	Realizou atualizações importantes, editou e corrigiu erros, ajudou na criação do banco de dados, desenvolveu o CSS das páginas e implementou as funcionalidades de editar projetos e meus projetos.
