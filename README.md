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
├── assets/             # Prints e recortes dos elementos gráficos (.png)
├── logs/               # Screenshots e evidências de falhas (gerado automaticamente)
├── pages/              # Classes do Page Object Model (BasePage, LoginPage, etc.)
│   |
│   ├── base_page.py    # Ações genéricas do PyAutoGUI (clique, digitação, busca de imagem)
│   └── login_page.py   # Mapeamento e fluxos específicos da tela de login
├── tests/              # Scripts de teste automatizados
│   |
│   └── test_login.py   # Suíte de testes com validações PyTest
├── conftest.py         # Hooks do PyTest para capturas de tela e configurações globais
├── requirements.txt    # Lista de dependências e bibliotecas do Python
└── README.md           # Documentação completa do projeto
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
