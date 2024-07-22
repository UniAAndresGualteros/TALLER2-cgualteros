from models.gato import Gato
from models.perro import Perro
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron



def obtener_sonidos():
    animales = [Gato(),Perro(),Huron(),Boa_Constrictor()]
    sonidos = {animal.__class__.__name__: animal.hacer_sonido() for animal in animales}
    return sonidos

def obtener_sonido_por_animal(nombre_animal):
    animales = {
        'Perro': Perro(),
        'Gato': Gato(),
        'Huron': Huron(),
        'Boa': Boa_Constrictor()
    }
    animal = animales.get(nombre_animal)
    if animal:
        return animal.hacer_sonido()
    return None