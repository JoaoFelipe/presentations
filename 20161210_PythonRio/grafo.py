import os
from subprocess import Popen, PIPE as P

class Grafo:
    def __init__(self, adjacentes):
        self.adjacentes = adjacentes
    
    def dottext(self):
        result = [
            "  {} -> {};".format(no, adjacente)
            for no, lista in self.adjacentes.items()
            for adjacente in lista
        ]
        return "digraph G {{\n  ranksep=0.25;\n{}\n}}".format("\n".join(result))

    def dot(self, format="png"):  # ToDo: Tratar erro
        kwargs = {} if os.name != 'nt' else {"creationflags": 0x08000000}
        p = Popen(['dot', '-T', format], stdout=P, stdin=P, stderr=P, **kwargs)
        return p.communicate(self.dottext().encode('utf-8'))[0]
    
    def __repr__(self):
        return self.dottext()
    
    def _repr_svg_(self):
        return self.dot("svg").decode("utf-8")
    
    def _repr_png_(self):
        return self.dot("png")
    
