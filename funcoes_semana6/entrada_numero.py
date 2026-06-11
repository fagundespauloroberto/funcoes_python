# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Este módulo contém duas classes, IntEntry e FloatEntry, que permitem
que o usuário insira um número inteiro ou um número decimal em um
widget Entry do tkinter.
"""

import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info


class _NumberEntry(Entry):
    _ESTILO_ERRO = {"bg": "pink", "fg": "black"}

    def __init__(self, parent, datatype, nome_tipo,
                 lower_bound, upper_bound, padrao, kwargs):
        super().__init__(parent)

        assert type(self) != _NumberEntry, \
            "não é possível instanciar _NumberEntry diretamente; use classes filhas"

        assert isinstance(lower_bound, datatype), \
            f"lower_bound deve ser {nome_tipo}"
        assert isinstance(upper_bound, datatype), \
            f"upper_bound deve ser {nome_tipo}"
        assert lower_bound < upper_bound, \
            "lower_bound deve ser menor que upper_bound"

        self.__tipo_dado = datatype
        self.__nome_tipo = nome_tipo
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound

        if padrao is not None:
            assert isinstance(padrao, datatype), \
                f"valor padrão deve ser {nome_tipo}"
            assert self._dentro_dos_limites(padrao), \
                "valor padrão deve estar dentro dos limites"
            self.delete(0, tk.END)
            self.insert(0, str(padrao))

        self.__configurar_tk(kwargs)
        self.bind("<FocusIn>", _NumberEntry.__selecionar_tudo)

    def __configurar_tk(self, kwargs):
        """Define configurações do tkinter."""
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = max(len(str(self.__lower_bound)),
                                  len(str(self.__upper_bound)))

        kwargs["validate"] = "focusin"
        kwargs["validatecommand"] = (
            self.register(self.__validar_tudo), "%V", "%s", "%P"
        )

        self.config(**kwargs)
        self._estilo_original = {"bg": self["bg"], "fg": self["fg"]}

    @staticmethod
    def __selecionar_tudo(event):
        """Seleciona todo o texto ao receber foco."""
        entrada = event.widget
        entrada.select_range(0, tk.END)
        entrada.icursor(tk.END)

    @staticmethod
    def _tem_espaco(texto):
        for ch in texto:
            if ch.isspace():
                return True
        return False

    def __validar_tudo(self, motivo, texto_atual, texto_novo):
        if motivo == "key":
            return self._validar_tecla(texto_atual, texto_novo)
        elif motivo == "focusin":
            return self.__validar_foco(texto_atual)
        elif motivo == "focusout":
            return self.__validar_foco(texto_atual)
        return False

    def __validar_foco(self, texto):
        try:
            n = self._converter(texto)
            valido = self._dentro_dos_limites(n)
        except ValueError:
            valido = False

        estilo = self._estilo_original if valido else _NumberEntry._ESTILO_ERRO
        self.config(estilo)
        return valido

    def _dentro_dos_limites(self, n):
        return self.__lower_bound <= n <= self.__upper_bound

    def set(self, n):
        """Mostra um número para o usuário."""
        assert isinstance(n, self.__tipo_dado), \
            f"n deve ser {self.__nome_tipo}"
        assert self._dentro_dos_limites(n), \
            "n fora dos limites permitidos"

        self.delete(0, tk.END)
        self.insert(0, str(n))

    def get(self):
        """Retorna o número digitado pelo usuário."""
        n = self._converter(super().get())
        if not self._dentro_dos_limites(n):
            raise ValueError("número fora dos limites")
        return n

    def clear(self):
        self.config({"validate": "focusin"})
        self.config(self._estilo_original)
        self.delete(0, tk.END)


class IntEntry(_NumberEntry):
    """Entrada que aceita apenas números inteiros."""

    def __init__(self, parent, *, lower_bound=-2**63,
                 upper_bound=2**63 - 1, padrao=None, **kwargs):
        super().__init__(parent, int, "um inteiro",
                         lower_bound, upper_bound, padrao, kwargs)

        self.__limite_tecla_min = lower_bound if lower_bound <= 1 else 1
        self.__limite_tecla_max = upper_bound if upper_bound >= -1 else -1
        self.__permite_negativo = (lower_bound < 0)

    def _validar_tecla(self, texto_atual, texto_novo):
        permitido = valido = False

        try:
            if not _NumberEntry._tem_espaco(texto_novo):
                n = int(texto_novo)
                permitido = self.__limite_tecla_min <= n <= self.__limite_tecla_max

                if permitido:
                    valido = self._dentro_dos_limites(n)

        except ValueError:
            permitido = (len(texto_novo) == 0 or
                         (self.__permite_negativo and texto_novo == "-"))

        if not permitido:
            try:
                n = int(texto_atual)
                valido = self._dentro_dos_limites(n)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _NumberEntry._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto):
        return int(texto)


class FloatEntry(_NumberEntry):
    """Entrada que aceita apenas números decimais."""

    def __init__(self, parent, *,
                 lower_bound=-float_info.max,
                 upper_bound=float_info.max,
                 padrao=None, **kwargs):

        super().__init__(parent, Number, "um número",
                         lower_bound, upper_bound, padrao, kwargs)

        self.__limite_tecla_min = lower_bound
        self.__limite_tecla_max = upper_bound

        self.__permite_negativo = (lower_bound < 0)
        self.__permite_ponto_inicial = True

    def _validar_tecla(self, texto_atual, texto_novo):
        permitido = valido = False

        try:
            if not _NumberEntry._tem_espaco(texto_novo):
                n = float(texto_novo)
                permitido = self.__limite_tecla_min <= n <= self.__limite_tecla_max

                if permitido:
                    valido = self._dentro_dos_limites(n)

        except ValueError:
            permitido = (
                len(texto_novo) == 0 or
                (self.__permite_negativo and texto_novo == "-") or
                (self.__permite_ponto_inicial and texto_novo == ".") or
                (self.__permite_negativo and texto_novo == "-.")
            )

        if not permitido:
            try:
                n = float(texto_atual)
                valido = self._dentro_dos_limites(n)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _NumberEntry._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto):
        return float(texto)