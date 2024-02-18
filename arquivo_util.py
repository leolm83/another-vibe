import re
import unidecode

def normaliza_nome_arquivo(texto):
    # texto_sem_acentos = unidecode.unidecode(texto)
    return re.sub(":|\.|\?|,|#|\/|\*|\/\/|\"|\'|\|","",texto)
