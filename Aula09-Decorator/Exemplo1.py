from abc import ABC, abstractmethod

# Componente Base (Interface)
class Bebida(ABC):
    @abstractmethod # // Define que a função abaixo é obrigatória para qualquer subclasse
    def custo(self): # // Método abstrato que força todas as bebidas a implementarem seu próprio preço
        pass
    
    @abstractmethod
    def descricao(self):
        pass
    
# Componente Concreto
class CafeSimples(Bebida):
    def custo(self):
        return 5.0
        
    def descricao(self):
        return "Café Simples"
        
# Decorator Base
class DecoradorBebida(Bebida):
    def __init__(self, bebida): # // Construtor que recebe e armazena o objeto 'bebida' para ser "embrulhado"
        self._bebida = bebida

    def custo(self):
        return self._bebida.custo()

    def descricao(self):
        return self._bebida.descricao()
        
# Decoradores Concretos
class Leite(DecoradorBebida):
    def custo(self):
        return self._bebida.custo() + 2.0 # // Chama o custo do objeto guardado e soma o valor do leite (R$ 2,00)
        
    def descricao(self):
        return self._bebida.descricao() + ", Leite"
        
class Chocolate(DecoradorBebida):
    def custo(self):
        return self._bebida.custo() + 3.0
    
    def descricao(self):
        return self._bebida.descricao() + ", Chocolate"
        
# Utilização
# 1. Começamos com o café simples (R$ 5.00)
bebida = CafeSimples()

# 2. Adicionamos Leite (5.00 + 2.00)
bebida = Leite(bebida)

# 3. Adicionamos Chocolate (7.00 + 3.00)
bebida = Chocolate(bebida)

# Resultado final
print("Descrição:", bebida.descricao())
print(f"Custo total: R$ {bebida.custo():.2f}")