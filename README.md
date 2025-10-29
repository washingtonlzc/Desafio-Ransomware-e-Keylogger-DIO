# 🔐 Projeto Educacional: Simulação de Malware em Python

Este projeto foi desenvolvido como parte de um desafio prático de cibersegurança para demonstrar, em um ambiente **100% controlado e com fins estritamente educacionais**, o funcionamento de dois tipos comuns de malware: **Ransomware** e **Keylogger**.

> ⚠️ **AVISO ÉTICO E LEGAL:** O código contido neste repositório é para fins de **estudo, análise e defesa** de sistemas. O uso deste material para qualquer atividade maliciosa, ilegal ou não autorizada é estritamente proibido e de total responsabilidade do usuário. Use-o apenas em ambientes controlados (sandboxes, máquinas virtuais) e com total consentimento.

## 🎯 Objetivos de Aprendizagem

*   Compreender o mecanismo de criptografia e sequestro de dados de um Ransomware.
*   Entender a captura e exfiltração de dados de um Keylogger.
*   Identificar vulnerabilidades e brechas de segurança.
*   Refletir sobre as estratégias de defesa e mitigação contra ameaças digitais.

## 🛠️ Configuração do Ambiente

Este projeto requer Python 3.x e as seguintes bibliotecas.

### Pré-requisitos

1.  **Instalar Dependências:**
    ```bash
    pip3 install -r requirements.txt
    ```

2.  **Ferramentas de Compilação (Linux):** Se houver erros na instalação de `pynput` (que requer compilação), pode ser necessário instalar as ferramentas de desenvolvimento:
    ```bash
    sudo apt update
    sudo apt install -y build-essential python3-dev
    ```

## 📂 Estrutura do Projeto

```
malware-simulado/
├── ransomware/
│   ├── ransomware_simulado.py  # Script de criptografia e descriptografia
├── keylogger/
│   ├── keylogger_simulado.py   # Script de captura de teclas e envio por e-mail
│   └── INSTRUCOES_EMAIL.md     # Guia para configurar o envio de e-mail (App Password)
├── docs/
│   └── defesa_e_prevencao.md   # Documentação sobre estratégias de defesa
├── requirements.txt
└── README.md
```

## 1. Ransomware Simulado

O script simula um ataque de Ransomware utilizando a biblioteca `cryptography` (módulo Fernet) para criptografia AES simétrica.

### ⚙️ Funcionamento

1.  **Geração de Chave:** Uma chave de criptografia única é gerada e salva em `chave.key`.
2.  **Criptografia:** O script escaneia o diretório e criptografa arquivos com a extensão `.test` (para segurança, apenas arquivos de teste são alvos). O arquivo original é substituído pela versão criptografada com a extensão `.encrypted`.
3.  **Nota de Resgate:** Cria o arquivo `LEIA_ME_RESGATE.txt` contendo instruções simuladas e a chave de descriptografia (em um cenário real, essa chave seria enviada ao atacante).

### 🚀 Como Executar

**1. Criptografar (Simular o Ataque):**

```bash
cd ransomware
python3 ransomware_simulado.py encrypt
```

**2. Descriptografar (Simular a Recuperação):**

```bash
python3 ransomware_simulado.py decrypt
```
*Nota: A descriptografia só funciona se o arquivo `chave.key` estiver presente no mesmo diretório.*

---

## 2. Keylogger Simulado

O script simula a captura furtiva de teclas e a exfiltração de dados via e-mail.

### ⚙️ Funcionamento

1.  **Captura:** Utiliza a biblioteca `pynput` para escutar eventos de teclado no sistema operacional.
2.  **Log:** As teclas capturadas são salvas em um buffer e periodicamente escritas no arquivo `log_captura.txt`.
3.  **Exfiltração:** Um *timer* periódico é configurado para enviar o arquivo de log por e-mail, utilizando a biblioteca `yagmail` e, em seguida, apagar o log localmente para manter a furtividade.

### ⚠️ Configuração de E-mail (CRÍTICO)

O envio de e-mail requer credenciais. **É fundamental usar uma Senha de Aplicação (App Password) e NUNCA sua senha principal.**

Consulte o guia detalhado em:
[keylogger/INSTRUCOES_EMAIL.md](keylogger/INSTRUCOES_EMAIL.md)

### 🚀 Como Executar

```bash
cd keylogger
python3 keylogger_simulado.py
```
*Pressione algumas teclas e aguarde o intervalo de envio configurado (padrão 60 segundos) para que o log seja processado.*

---

## 🛡️ Reflexão sobre Defesa e Prevenção

O objetivo final deste estudo é a defesa. A melhor forma de se proteger é entender como os atacantes operam.

A documentação completa sobre as estratégias de defesa, incluindo Antivírus, Firewall, Sandboxing, Backup 3-2-1 e a importância da Conscientização do Usuário, pode ser encontrada aqui:

[docs/defesa_e_prevencao.md](docs/defesa_e_prevencao.md)

---

**Autor:** Manus AI (para o desafio prático)
**Data:** Outubro de 2025
