# Conexão Hospitalar - Backend (Django)

## 🚀 Pré-requisitos
- Windows 10/11
- Python 3.12+ ([Download](https://www.python.org/downloads/))
- Git instalado ([Git para Windows](https://gitforwindows.org/))

## ⚙️ Configuração Inicial

1. **Clonar o repositório**:
```cmd
git clone https://github.com/seu-usuario/conexao-hospitalar.git
cd conexao-hospitalar/backend
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