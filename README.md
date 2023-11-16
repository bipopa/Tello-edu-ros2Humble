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

Aunque djitellopy ha demostrado ser una herramienta muy útil para comenzar a trabajar con los drones, se encuentra limitada al control de un único dron. Además, cada comando que se envía desde esta librería espera recibir una respuesta del dron antes de continuar; esta característica puede ser deseable en situaciones donde se desea sincronizar el movimiento de un dron, sin embargo, el código se detiene cuando el dron no ha respondido. Esto genera un gran inconveniente al tratar de controlar los drones a través de una máquina virtual, ya que, a menos que se haga un redireccionamiento de puertos desde el Host, esta nunca escuchará la respuesta.

Por este motivo, se propone utilizar la comunicación UDP a partir de Python, como se muestra en la carpeta 'Python-tello-UDP'."
