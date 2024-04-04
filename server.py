import http.server
import socketserver
from decouple import config

PORT = config('PORT', cast=int)

# http.server.SimpleHTTPRequestHandler: um manipulador de 
# solicitações HTTP simples que serve arquivos do diretório 
# atual e de qualquer um de seus subdiretórios.
HANDLER = http.server.SimpleHTTPRequestHandler

# Uma instância do TCPServer descreve um servidor que usa o 
# protocolo TCP para enviar e receber mensagens 
# (http é um protocolo de camada de aplicativo na parte superior do TCP).

# o endereço TCP é passado como uma tupla de (endereço IP, número da porta)
with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
  print("🐍 Server ON => localhost:{}".format(PORT))
  httpd.serve_forever()


# Um servidor web é um processo que escuta 
# solicitações recebidas em um endereço TCP específico.

# Um endereço TCP é identificado por um endereço IP e 
# um número de porta. Segundo, um servidor web também precisa 
# ser informado sobre como lidar com solicitações recebidas.


# Essas solicitações de entrada são tratadas por manipuladores 
# especiais. Você pode pensar em um servidor da Web como 
# um expedidor, uma solicitação é recebida, o servidor 
# http inspeciona a solicitação e a envia para um manipulador 
# designado.