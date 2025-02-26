# Conexão Hospitalar - Backend (Django)

## 🚀 Pré-requisitos
- Windows 10/11
- Python 3.12+ ([Download](https://www.python.org/downloads/))
- Git instalado ([Git para Windows](https://gitforwindows.org/))

## ⚙️ Configuração Inicial

1. **Clonar o repositório**:
```cmd
git clone https://github.com/eligado/Conexao-Hospitalar---Backend.git
cd Conexao-Hospitalar---Backend
```
2. **Ambiente Virtual:**
```cmd
python -m venv venv
venv\Scripts\activate
```
3. **Instalar Dependências:**
```cmd
pip install -r requirements.txt
```
4. **Banco de Dados:**
```cmd
python manage.py makemigrations
python manage.py migrate
```
5. **Criar Superusuário:**
```cmd
python manage.py createsuperuser
```
6. **Iniciar Servidor:**
```cmd
python manage.py runserver
```
## 🔑 Acessos Cruciais
- Painel Admin: http://localhost:8000/admin

## ⚠️ Solução de Problemas Comuns
- Erro de Porta: Use python manage.py runserver 8001
- Dependências Missing: Reinstale com pip install -r requirements.txt
- Erros de Migração: Delete a pasta migrations/ e o arquivo db.sqlite3

## 📌 Dicas Windows
- Sempre execute o Terminal como Administrador
- Ambiente virtual ativo = (venv) no prompt
- Desativar ambiente: deactivate

## 🔗 Documentação Oficial: [Django Docs](https://docs.djangoproject.com/) 

## 🛠️ Contribuição (Importante!)

⚠️ **Aviso para Desenvolvedores:**  
```diff
- NUNCA TRABALHE DIRETAMENTE NA BRANCH MAIN!
+ Sempre crie e utilize uma nova branch para suas alterações!
```

**Passos Seguros:**  
1. Crie uma nova branch a partir da `main`:  
```cmd
git checkout main
git pull origin main
git checkout -b feature/nome-da-sua-feature
```

2. Trabalhe APENAS na sua branch:  
```cmd
git add .
git commit -m "Descrição clara das mudanças"
git push origin feature/nome-da-sua-feature
```

3. Abra um **Pull Request** para revisão antes de mesclar com a `main`

🔒 A branch `main` está protegida - mudanças só serão aceitas via Pull Request aprovado!