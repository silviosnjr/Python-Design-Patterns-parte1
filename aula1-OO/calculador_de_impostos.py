from impostos import ISS, ICMS

class Calculador_de_impostos(object):

    """
    realiza_calculo faz um ducktype com o parametro imposto
    que pode ser um ISS e ICMS os dois tem o mesmo nome de método calcula
    """
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == "__main__" :
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())


