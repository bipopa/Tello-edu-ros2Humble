# Tello-edu-ros2Humble
Bienvenidos al repositorio de Tello-edu con ros2Humble. En este repositorio encontraran información sobre como utilizar los drones tello edu con python y su integración con ROS2.

## ¿Qué necesitas para comenzar a trabajar con los drones?
* Computador/VM con python3 y tu editor de texto preferido, como Visual Studio Code.
* Si deseas utilizar la interfaz con ROS2 se recomienda tener Ubuntu 22.04 e instalar ROS2 Humble: https://docs.ros.org/en/humble/index.html

Si deseas probar las librerias de djitellopy puedes instalarlas de la siguiente forma:

```
pip install djitellopy
```

Esta librería permite tener una primera aproximación al manejo de los drones debido a su facilidad de uso. djitellopy se encuentra documentada y con ejemplos en el siguiente repositorio: https://github.com/damiafuentes/DJITelloPy/tree/master.

Aunque djitellopy ha demostrado ser una herramienta muy util para comenzar a trabajar con los drones, se encuentra limitada al control de un unico dron. Ademas, cada comando que se envia desde esta libreria espera a recibir una respuesta del dron antes de continuar, esta carateristica puede ser deseable en situaciones donde se desea sincronizar el movimiento un dron, sin embargo el codigo se detiene cuando el dron no ha respondido. Esto genera un gran inconveniente al tratar  de controlar los drones a traves de una maquina virtual pues con la libreria pues a menos que se haga un redireccionamiento de puertos desde el Host, esta nunca escuchara la respuesta

Por este motivo se propone utilizar la comunicación UDP a partir de python como se muestra en la carpeta Python-tello-UDP
