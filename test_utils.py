from utils import es_primo

def test_es_primo():
    es_primo(2) is True
    es_primo(3) is True
    es_primo(4) is False
    es_primo(6) is False
    