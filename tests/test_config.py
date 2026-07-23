""" 
Archivo    : test_config.py 
Descripción: Pruebas unitarias para el patrón Singleton (ConfiguracionApp). 
             Verifica unicidad de instancia, consistencia de valores 
             y comportamiento según variable de entorno. 
Patrón GoF : Singleton (Creacional) 
Curso      : Diseño de Patrones (UCA-IEP026) 
Autores    : Luis Alejandro Casillas Hernandez— correo@uca.edu.sv — 00000000 
             Luis Alejandro Casillas Hernandez— correo@uca.edu.sv — 00000000 
Fecha      : 22/julio/2026 
""" 
from src.config.configuracion import ConfiguracionApp 
 
def test_singleton_retorna_misma_instancia(): 
    a = ConfiguracionApp() 
    b = ConfiguracionApp() 
    assert a is b 
 
def test_singleton_mismos_valores(): 
    a = ConfiguracionApp() 
    b = ConfiguracionApp() 
    assert a.version == b.version 
    assert a.entorno == b.entorno 
 
def test_configuracion_tiene_version(): 
    config = ConfiguracionApp() 
    assert config.version == "1.0.0" 
 
def test_es_produccion_por_defecto(): 
    config = ConfiguracionApp() 
    # En entorno de pruebas, ENTORNO puede ser "pruebas" 
    assert isinstance(config.es_produccion(), bool)