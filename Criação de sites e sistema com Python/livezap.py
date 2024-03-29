# pip install flet

# titulo Livezap
# Botão de iniciar o chat
    # popup
        # Bem vindo ao Livezap
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Juan entrou no chat
    # Mensagens dos usuario
# campo para enviar a mensagem
# botao enviar
import flet as ft 

def main(pagina):
    titulo = ft.Text("Livezap")

# Criar caixa de texto
    nome_usuario = ft.TextField(label="Escreva seu nome")

# criando campo da mensagem e botao enviar mensagem
    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        # colocar o nome do usuario na menssagem
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value} "
        pagina.pubsub.send_all(texto_campo_mensagem)
        # limpar o campo_mensagem
        campo_mensagem.value = ""
        pagina.update()


    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

# Evento do botao entrar chat
    def entrar_chat(evento):
        # Feche o popup
        popup.open = False
        # tirar o botão "iniciar chat" da tela
        pagina.remove(botao_iniciar)
        # adicionar o chat
        pagina.add(chat)
        # criar o campo de enviar mensagem
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        # botao de enviar mensagem
        pagina.add(botao_enviar)
        # Vai mostra que usuario entrou no chat
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

#  Criar um popup  
    popup = ft.AlertDialog(
                open=False,
                modal=True, 
                title=ft.Text("Bem vindo ao Livezap"),
                content=nome_usuario,
                actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
                 )
# Evento do botao iniciar chat  
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

# Criar botão
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)


#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)