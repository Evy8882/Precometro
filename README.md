# PREÇOMETRO
> Software de comparação de preços em lojas virtuais através de web scrabing

> PROJETO CRIADO APENAS COM A FINALIDADE DE ESTUDOS

## Funcionalidades
- Comparação de preços entre diferentes lojas virtuais.
- Coleta de dados automatizada via web scraping.

## Tecnologias

  <p><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height=32 align="center"/> Python</p>
  <p><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" height=32 align="center"/> Flask</p>
  <p><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" height=32 align="center"/> React</p>
  <p><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" height=32 align="center"/> CSS</p>

## Funcionamento

#### BackEnd
- API construída em python utilizando estrutura MVC;
- Web Scrabing através do BeautifulSoup e API's de lojas;

#### FrontEnd
- Aplicação React com VITE e Typescript
- Utilização do react-router-dom para navegação

## Estrutura

```
📦 projeto
├── 📁 backend
│   ├── 📁 controllers
│   │   └── 🐍 results_controller.py
│   ├── 📁 models
│   │   └── 🐍 searches_model.py
│   ├── 📁 venv
│   └── 🐍 app.py
│
├── 📁 frontend
│   ├── 📁 node_modules
│   ├── 📁 public
│   ├── 📁 src
│   │   ├── 📁 assets
│   │   ├── 📁 pages
│   │   ├── ⚛️ App.css
│   │   ├── ⚛️ App.tsx
│   │   ├── ⚛️ index.css
│   │   └── ⚛️ main.tsx
│   ├── 📄 index.html
│   ├── 📄 package-lock.json
│   ├── 📄 package.json
│   ├── 📄 tsconfig.app.json
│   ├── 📄 tsconfig.json
│   ├── 📄 tsconfig.node.json
│
├── 📄 .env
```
