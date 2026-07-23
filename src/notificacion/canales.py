"""
Archivo : canales.py
Descripción: Define la jerarquía de Implementadores (Implementor) del patrón
             Bridge. Cada Canal encapsula cómo se entrega físicamente un
             mensaje: por email, SMS o consola. Las abstracciones no conocen
             los detalles de ningún canal específico.
Patrón GoF : Bridge — Implementor (Estructural)
Curso : Diseño de Patrones (UCA-IEP026)
Autores : Luis Alejandro Casillas Hernandez — correo@uca.edu.sv — 00000000
             Luis Alejandro Casillas Hernandez — correo@uca.edu.sv — 00000000
Fecha : 2026
"""
from abc import ABC, abstractmethod

class Canal(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str) -> None: pass

class CanalEmail(Canal):
    def enviar(self, destinatario, texto):
        print(f"[EMAIL → {destinatario}] {texto}")
        pass

class CanalSMS(Canal):
    def enviar(self, destinatario, texto):
        print(f"[SMS → {destinatario}] {texto}")
        pass

class CanalConsola(Canal):
    """Útil para pruebas y logging interno"""
    def enviar(self, destinatario, texto):
        print(f"[LOG] {destinatario}: {texto}")
        pass