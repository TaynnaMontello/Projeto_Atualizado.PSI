## 🗂️ Estrutura do Projeto — Matéria de PSI

📁 Sistema de Projetos IF/        ← Pasta principal do projeto  
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
├── 📄 schema.sql                  ← Arquivo que define as tabelas usuarios e projetos do banco de dados
├── 📄 requirements.txt            ← Lista de dependências da aplicação
