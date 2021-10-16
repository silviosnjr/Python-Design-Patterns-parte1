# -*- coding: UTF-8 -*-
class Calculador_de_descontos(object) :
    def calcula(self, orcamento):
        if (orcamento.total_itens > 5):
            return orcamento.valor * 0.1
        elif (orcamento.valor > 500):
            return orcamento.valor * 0.07


if __name__ == "__main__" :
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item - 1", 100))
    orcamento.adiciona_item(Item("Item - 2", 50))
    orcamento.adiciona_item(Item("Item - 3", 400))

    print(orcamento.valor)
    calculador = Calculador_de_descontos()
    desconto = calculador.calcula(orcamento)

    print ("Desconto calculado %s" % (desconto))