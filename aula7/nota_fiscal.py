# -*- coding: UTF-8 -*-
from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal(object):

    #parametros opcionais em Python tem que ficar por último
    def __init__(self, razao_social, cnpj, itens, data_de_emissao = date.today(), detalhes = "", observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        #recebendo uma lista de observadores podemos iterar sobre ela
        #e executar as funções passadas na lista,
        #desta forma não precisamos alterar a classa Nota Fiscal
        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

if __name__ == '__main__':

    from criador_de_nota_fiscal import Criador_de_nota_fiscal
    from observadores import imprime, envia_por_email, salva_no_banco

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    # recursos do Python para criar objetos
    #parametros nomeados, podemos enviar eles sem ordens
    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        data_de_emissao=date.today(),
        razao_social='FHSA Limitada',
        detalhes='',
        itens = itens,
        observadores=[imprime, envia_por_email, salva_no_banco]
    )

    #Criando objetos com Python Builder
    #nota_fiscal_criada_com_builder = (Criador_de_nota_fiscal().
    #    com_razao_social('FHSA Limitada').
    #    com_cnpj('012345678901234').
    #    com_itens(itens).constroi())