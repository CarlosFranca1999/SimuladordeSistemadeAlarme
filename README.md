# Sistema de Alarme IoT — Detector de Movimento

Projeto desenvolvido em Python utilizando **Flask** para simular um sistema de alarme com detector de movimento e interface web.

## 🚀 Funcionalidades
- Armar e desarmar o alarme
- Simular detecção de movimento
- Consultar estado do sistema em tempo real
- Registro do horário da última detecção

## 🧰 Tecnologias
- Python
- Flask
- HTML/CSS
- JSON

## ▶️ Como executar
1. Instale o Flask:
```bash
pip install flask

Execute o projeto:

python main.py

Acesse no navegador:

http://localhost:5000
🌐 Rotas principais

GET / → Página principal

GET /state → Estado do sistema

POST /arm → Armar alarme

POST /disarm → Desarmar alarme

POST /motion → Simular movimento

📌 Observação

O estado do alarme é armazenado apenas em memória e reinicia ao fechar o servidor.
