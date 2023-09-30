# Ejemplo de package en python
###### **Por ➡️ Natalia Cortés**

--- 
⚠️**REQUERIMINTO PARA EL PROGRAMA TENER INSTALADO PYTEST**⚠️
    
> Esto se hace mediante línea de commandos con la libreria de pip
```bash
pip install pytest
```
> Atención ⚠️ asegurate de que el path de windows esté correcto si no lo está pide ayuda.
--- 

En este programita se ha creado unos package en python para una serie de funciones creadas en [Logica](./Logica/suma.py) para poder ser testeadas en [Tests](./Test_Logica/test_suma.py) 

> La importación del módulo a testear se hace en [Tests](./Test_Logica/test_suma.py) de la siguiente forma: 

```python
from package.módulo import funcion
# package es el nombre de la carpeta.
# módulo es el nombre del archivo donde hemos programado la función.
# función es la función que hemos creado dentro del archivo.
```

> Para la ejecución del mismo deberemos irnos a la terminal y ejecutar el siguiente comando: 

```shell
pytest -s .\Test_Logica\test_suma.py
```

> Durante la ejecución, se irán pidiendo las diferentes variables que van a ser usadas para la comprobación del programa.
> 
> La introducción de las variables en la terminal es gracias al -s en el comando pytest.

- [x] Se ha creado una función como mínimo para el test
- [x] Se ha trabajado con la terminal
- [x] Se ha ejecutado los test

