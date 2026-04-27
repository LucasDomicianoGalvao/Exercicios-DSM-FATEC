
class Pizza:
    def get_descricao(self):
        return "Pizza Base"
    def get_custo(self):
        return 20.00

class PizzaDecorator(Pizza):
    def __init__(self, pizza_decorada):
        self._pizza = pizza_decorada
    def get_descricao(self):
        return self._pizza.get_descricao()
    def get_custo(self):
        return self._pizza.get_custo()

class Queijo(PizzaDecorator):
    def get_descricao(self):
        return self._pizza.get_descricao() + ", Queijo"
    def get_custo(self):
        return self._pizza.get_custo() + 5.00

class Calabresa(PizzaDecorator):
    def get_descricao(self):
        return self._pizza.get_descricao() + ", Calabresa"
    def get_custo(self):
        return self._pizza.get_custo() + 7.00

class Bacon(PizzaDecorator):
    def get_descricao(self):
        return self._pizza.get_descricao() + ", Bacon"
    def get_custo(self):
        return self._pizza.get_custo() + 8.00

class BordaRecheada(PizzaDecorator):
    def get_descricao(self):
        return self._pizza.get_descricao() + ", Borda Recheada"
    def get_custo(self):
        return self._pizza.get_custo() + 6.00

if __name__ == "__main__":
    pedido = Pizza()
    pedido = Queijo(pedido)
    pedido = Calabresa(pedido)
    pedido = BordaRecheada(pedido)

    print("--- PEDIDO DA PIZZARIA ---")
    print(f"Ingredientes: {pedido.get_descricao()}")
    print(f"Total: R$ {pedido.get_custo():.2f}")
