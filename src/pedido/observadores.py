"""
Archivo : observadores.py
Descripción: Define la interfaz ObservadorPedido y sus implementaciones
             concretas (NotificadorCliente, RegistroAuditoria,
             ActualizadorInventario). Cada observador reacciona de forma
             independiente a los cambios de estado del pedido, sin que el
             sujeto (GestorPedidos) los conozca directamente.
Patrón GoF : Observer — ConcreteObserver (Comportamiento)
Curso : Diseño de Patrones (UCA-IEP026)
Autores : Nombre Apellido — correo@uca.edu.sv — 00000000
             Nombre Apellido — correo@uca.edu.sv — 00000000
Fecha : 2026
"""
from abc import ABC, abstractmethod

class ObservadorPedido(ABC):
    @abstractmethod
    def actualizar(self, numero: str, estado: str) -> None: pass

class NotificadorCliente(ObservadorPedido):
    def actualizar(self, numero, estado):
        print(f"[CLIENTE] Tu pedido #{numero} está: {estado}")

class RegistroAuditoria(ObservadorPedido):
    def __init__(self):
        self.historial: list[str] = []

    def actualizar(self, numero, estado):
        entrada = f"#{numero} → {estado}"
        self.historial.append(entrada)
        print(f"[AUDITORÍA] {entrada}")

class ActualizadorInventario(ObservadorPedido):
    def actualizar(self, numero, estado):
        if estado == "enviado":
            print(f"[INVENTARIO] Descontando stock del pedido {numero}")