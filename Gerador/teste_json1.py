import json
class GerarJson():
    
    def __init__(self, dict):
        self.dict = dict
        self.arquivo = 'register.json'
        self.read_json(self.arquivo)
    def read_json(self, arquivo):
        new = []
        try:
            with open(arquivo, 'r') as f:
                reader = json.load(f)
            new.append(self.dict)  
            if reader:
                for r in reader:
                    print(r)
                    new.append(r)
                    
                self.make_json(new, arquivo)
            else:
                self.make_json(new, arquivo)
        
        except FileNotFoundError:
            new.append(self.dict)
            self.make_json(new, arquivo)     
    def make_json(self, conteudo, file):
        with open(file, 'w') as f:
            json.dump(conteudo, f)
