"""
Archivo : notificaciones.py
Descripción: Define la jerarquía de Abstracciones del patrón Bridge.
             Notificacion mantiene una referencia a un Canal (el puente)
             y delega el envío a él. Las subclases (NotificacionPedido,
             AlertaStock) definen qué se comunica; los Canales definen cómo.
             Esto evita la explosión n×m de subclases.
Patrón GoF : Bridge — Abstraction (Estructural)
Curso : Diseño de Patrones (UCA-IEP026)
Autores : Luis Alejandro Casillas Hernandez — correo@uca.edu.sv — 00000000
             Luis Alejandro Casillas Hernandez — correo@uca.edu.sv — 00000000
Fecha : 2026
"""
from abc import ABC, abstractmethod
from src.notificacion.canales import Canal

class Notificacion(ABC):
    def __init__(self, canal: Canal):
        self._canal = canal  

    @abstractmethod
    def enviar(self, destinatario: str) -> None: pass

    def cambiar_canal(self, canal: Canal):
        """Intercambio en caliente — imposible con herencia"""
        self._canal = canal

class NotificacionPedido(Notificacion):
    def __init__(self, canal: Canal, numero: str, estado: str):
        super().__init__(canal)
        self._numero = numero
        self._estado = estado

    def enviar(self, destinatario):
        self._canal.enviar(destinatario,
        f"Pedido #{self._numero} → Estado: {self._estado}")
        pass

class AlertaStock(Notificacion):
    def __init__(self, canal: Canal, producto: str, unidades: int):
        super().__init__(canal)
        self._producto = producto
        self._unidades = unidades

    def enviar(self, destinatario):
        self._canal.enviar(destinatario,
        f"⚠ Stock bajo — {self._producto}: {self._unidades} unidades")
        pass