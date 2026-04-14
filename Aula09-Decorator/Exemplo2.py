from abc import ABC, abstractmethod

# Componente
class Notificador(ABC): # // Classe abstrata que define o contrato para todos os notificadores
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Componente Concreto
class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        return f"Enviando por Email: {mensagem}"

# Decorador Base
class DecoradorNotificador(Notificador):
    def __init__(self, notificador): # // Inicializa o decorador guardando a instância do notificador base
        self._notificador = notificador

    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem)

# Decoradores Concretos
class NotificadorSMS(DecoradorNotificador):
    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem) + f"\nEnviando por SMS: {mensagem}"

class NotificadorWhatsapp(DecoradorNotificador):
    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem) + f"\nEnviando por Whatsapp: {mensagem}"

# Utilização
# Linha 35 
notificador = NotificadorEmail() # // Cria o objeto base que faz o envio principal via e-mail

# Linha 39 
notificador = NotificadorSMS(notificador) # // "Envolve" o notificador de e-mail com a funcionalidade de SMS

# Linha 43 
notificador = NotificadorWhatsapp(notificador) # // Adiciona mais uma camada, incluindo o envio por Whatsapp ao conjunto

print(notificador.enviar("Sistema em manutenção."))
    