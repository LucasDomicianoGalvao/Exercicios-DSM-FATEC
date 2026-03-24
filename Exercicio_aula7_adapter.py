import json

# 1. ADAPTEE 
class SistemaCSV:
    def get_dados_csv(self):
        # Simula o retorno de uma API ou arquivo CSV
        return "nome,idade\nLucas Galvao,20\nAna Souza,25"

# 2. TARGET 
class InterfaceJSON:
    def get_dados(self):
        pass

# 3. ADAPTER
class CSVparaJSONAdapter(InterfaceJSON):
    def __init__(self, sistema_csv):
        self.sistema_xml = sistema_csv # Armazena a referência do adaptee

    def get_dados(self):
        # Chama o método do sistema legado 
        
        csv_data = self.sistema_xml.get_dados_csv()
        
        # Lógica de conversão 
        
        linhas = csv_data.split("\n")
        cabecalho = linhas[0].split(",")
        corpo = linhas[1:]
        
        lista_objetos = []
        for linha in corpo:
            valores = linha.split(",")
            dicionario = dict(zip(cabecalho, valores))
            lista_objetos.append(dicionario)
        
        # Retorna os dados no formato esperado (JSON) 
        
        return json.dumps(lista_objetos, indent=4)

# 4. CLIENT (Uso prático)
sistema_legado = SistemaCSV() # Instancia o sistema antigo 

adaptador = CSVparaJSONAdapter(sistema_legado) # Cria o adapter 

print(adaptador.get_dados()) # Cliente usa interface JSON sem saber do CSV 