# Instruções para o Keylogger Simulado (Envio por E-mail)

O script `keylogger_simulado.py` utiliza a biblioteca `yagmail` para simular o envio automático dos logs de teclas por e-mail.

**ATENÇÃO:** Você **NÃO** deve usar sua senha de e-mail principal diretamente no código.

## Configuração Necessária

Para que o envio funcione, você deve configurar uma **Senha de Aplicação** (App Password) no seu provedor de e-mail (Gmail, Outlook, etc.).

### Para Gmail:

1.  Acesse sua **Conta Google**.
2.  Vá em **Segurança**.
3.  Em "Como você faz login no Google", ative a **Verificação em Duas Etapas** (se ainda não estiver ativa).
4.  Após ativar, a opção **Senhas de app** aparecerá abaixo. Clique nela.
5.  Crie uma nova senha de app (selecione "Outro" e dê um nome, como "Keylogger Simulado").
6.  A senha gerada (uma sequência de 16 caracteres) é a que você deve usar no código.

## Edição do Código

Abra o arquivo `keylogger_simulado.py` e substitua os placeholders pelas suas credenciais e e-mail de destino:

\`\`\`python
EMAIL_USER = "SEU_EMAIL_AQUI@gmail.com"  # Seu e-mail (o mesmo que você usou para gerar a senha de app)
EMAIL_PASSWORD = "SUA_SENHA_DE_APLICACAO_AQUI" # A senha de 16 caracteres gerada
EMAIL_TO = "EMAIL_DE_DESTINO_AQUI@exemplo.com" # O e-mail para onde o log será enviado
\`\`\`

**Lembre-se:** Este é um projeto educacional. Use-o apenas em ambientes controlados e com total consentimento.
