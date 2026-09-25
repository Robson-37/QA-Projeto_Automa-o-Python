# 🚀 QA Automation Project - PyAutoGUI & Page Object Model (POM)

Projeto profissional de automação de testes de interface gráfica (GUI) desenvolvido em **Python**, utilizando **PyAutoGUI** para interação com elementos visuais da tela e **PyTest** para estruturação e execução dos testes. A arquitetura segue rigorosamente o padrão **Page Object Model (POM)** para proporcionar facilidade de manutenção, reuso de código e alta escalabilidade.

---

## 📋 Funcionalidades

- **Automação Desktop & Web:** Capacidade de interagir com qualquer aplicação gráfica executada no sistema operacional.
- **Reconhecimento de Imagem (Image Recognition):** Localização de botões, campos e elementos dinâmicos por meio de capturas em formato `.png`.
- **Evidências Automáticas de Falhas:** Captura automática de tela (screenshot) no momento exato em que um teste falhar, salvando a evidência no diretório `logs/`.
- **Arquitetura Escalonável (POM):** Separação clara das responsabilidades entre mapeamento de interface (`pages/`), elementos visuais (`assets/`) e cenários de teste (`tests/`).
- **Relatórios de Teste:** Suporte integrado a relatórios visuais com PyTest e Allure Report.

---

## 📁 Estrutura do Projeto

```text
QA_Automation_Project/
.
├── .pytest_cache/     # Cache do Pytest (dados temporários de execuções anteriores)
├── .venv/            # Ambiente virtual Python (dependências e bibliotecas do projeto)
├── __pycache__/      # Ficheiros compilados em bytecode (.pyc) gerados pelo Python
├── allure-results/   # Ficheiros brutos (JSON/XML) para geração de relatórios do Allure
├── assets/           # Recursos estáticos auxiliares (imagens, logótipos, estilos)
├── logs/             # Registos de eventos, rastreios e mensagens de erro da execução
├── pages/            # Classes do Page Object Model (POM) com mapeamento dos elementos
├── tests/            # Scripts com os cenários e casos de teste automatizados
├── .gitattributes    # Regras do Git para gestão de formatos de texto/linha entre SOs
├── .gitignore        # Lista de ficheiros e pastas ignorados pelo controlo de versões Git
├── conftest.py       # Configurações globais, fixtures e hooks partilhados do Pytest
├── login.html        # Página HTML local para testes de interface ou simulações
├── README.md         # Documentação com instruções de utilização e instalação do projeto
└── requirements.txt  # Lista de dependências e versões dos pacotes Python do projeto
```

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes componentes instalados em seu ambiente local:

1. **Python 3.10 ou superior:** Instalado diretamente no sistema operacional. Verifique a instalação no terminal:
   - **Windows:** `python --version`
   - **Linux / macOS:** `python3 --version`
2. **Git:** Para clonar e gerenciar o repositório.
3. **Editor de Código:** Recomenda-se o **Visual Studio Code (VS Code)** com as extensões de Python e PyTest habilitadas.
4. **Permissões do Sistema Operacional:** O PyAutoGUI requer permissões de acessibilidade/controle de tela no macOS, Linux ou Windows para simular eventos de teclado e mouse.

---

## ⚙️ Instalação das Dependências na Máquina

Como a instalação será feita diretamente no sistema operacional (sem ambiente virtual `venv`), siga os passos abaixo no seu terminal ou prompt de comando:

### 1. Clonar o repositório

```bash
git clone https://github.com/Robson-37/QA_Automation_Project.git
cd QA_Automation_Project
```

### 2. Instalar as bibliotecas globais

Atualize o instalador de pacotes (`pip`) e instale as dependências diretamente na sua máquina:

- **No Windows (Prompt de Comando ou PowerShell):**
  ```cmd
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

- **No Linux / macOS:**
  ```bash
  python3 -m pip install --upgrade pip
  pip3 install -r requirements.txt
  ```

> 💡 **Nota para usuários Linux/macOS:** Se o sistema exibir um aviso sobre ambiente gerenciado pelo sistema (*externally-managed-environment*), você pode usar a flag `--break-system-packages` ou instalar via `pip3 install --user -r requirements.txt`.

## 📄 Licença

Este projeto é disponibilizado sob a licença MIT. Sinta-se à vontade para modificar e reutilizar em seus projetos de automação de testes.
