Para la practica de este laboratorio lo primero que realizamos fue la adquisición de la señal, para esto colocamos los electrodos en el antebrazo para analizar el músculo cubital posterior, y colocamos una tierra cercana a iniciar la palma de la mano como se muestra en la siguiente figura, utilizamos un amplificador AD8232 y para gráficar la señal utilizamos la tarjeta de Arduino.

![image](https://github.com/user-attachments/assets/4a11d6a7-10da-49d7-aae4-491e9158b328)

El codigo realizado en arduino es el siguiente

![image](https://github.com/user-attachments/assets/ef873c2d-21c7-4457-8f66-dc135bb140a4)
Luego le pedimos al sujeto de prueba que realizara una contracción del musculo hasta llegar a la fatiga con una pesa de 10kg, en total tuvimos 7 repeticiones. Con la señal capturada la agregamos a Spyder para empezar a realizar su análisis. la manera de pasarla fue con todos los vectores de voltaje, valor y tiempo para poder imprimir la señal exacta que teniamos en arduino, posterior a esto lo primero que hicimos fue limpiar un poco la señal eliminado el ruido en ella mediante el codigo, aplicamos un filtro pasa altas para deshacer los componentes de baja frecuencia, como el movimiento que podia tener la persona que o a la linea de base. Y un filtro pasa bajas para eliminar frecuencias altas no deseadas, como el ruido electromagnético o de interferencia de alta frecuencia. la frecuencia de muestreo con la que se trabajó fue : 250 Hz


![image](https://github.com/user-attachments/assets/64b68cb6-9f5d-4a07-85d0-b5e212b21d15)
![image](https://github.com/user-attachments/assets/775df0e4-58d9-47ef-9467-c763a5cf8ff2)
Aplicamos un aventamiento a la señal, en cada contracción ya que es una función que se aplica multiplicativamente sobre una señal para limitarla o suavizarla en su dominio de tiempo o espacio. La señal completa se "ventanea", lo que significa que la señal original se multiplica por la función de ventana en cada punto, normalmente antes de hacer un análisis en el dominio de la frecuencia. El aventanamiento que utilizamos fue la hanning, que es una técnica usada comúnmente en el procesamiento de señales y análisis espectral. Se aplica para suavizar una señal y reducir los efectos de las discontinuidades en los bordes de la señal cuando se realiza una Transformada de Fourier (FFT), esta tiene una forma de campana que esta diseñada para reducir las discontinuidades en los extremos de la señal. La utilizamos debido a que cuando se trabaja con señales finitas como señales electromiográficas, a menudo tenemos que analizar pequeños fragmentos de la señal, y las discontinuidades o saltos bruscos en los extremos de estos fragmentos pueden generar artefactos no deseados al realizar la transformada de Fourier (FFT), lo que se conoce como fugas espectrales.

Fugas espectrales: Esto ocurre cuando una señal discontinua en el dominio del tiempo introduce componentes de alta frecuencia no presentes originalmente en la señal. La ventana Hanning suaviza estos extremos, reduciendo las fugas espectrales, lo que resulta en un espectro de frecuencias más preciso y más limpio. Cuando aplicamos la ventana Hanning, los valores en los extremos de la señal son multiplicados por 0 (o casi 0), mientras que los valores en el centro son multiplicados por 1 o por valores cercanos a 1. Esto produce una señal suavizada que tiende a tener valores pequeños en los bordes y se comporta de manera más gradual a lo largo del tiempo o del espacio.

![image](https://github.com/user-attachments/assets/3ad4b1e9-3a05-46de-9e88-1aa6275d9d9b)

Luego realizamos un fraccionamiento a esa señal de la ventana hanning, para poder hacer el analisis espectral a cada contracción. cada fragmento de la señal representa un periodo de la actividad muscular, y los gráficos de FFT (Transformada Rápida de Fourier) muestran la distribución de frecuencias en cada segmento.
![image](https://github.com/user-attachments/assets/d5cfb90f-99bf-465c-9299-b2a0d5168363)
![image](https://github.com/user-attachments/assets/2ed60193-9317-4590-8032-f46576ebc6ff)
![image](https://github.com/user-attachments/assets/a4e85af6-0a00-4bf1-83f8-e70726152c3c)
![image](https://github.com/user-attachments/assets/5885adaa-02a0-4337-9bb9-ef9e0cf6bf29)
![image](https://github.com/user-attachments/assets/a6bc8a0d-afed-4bb9-8f62-cf6884f12895)
![image](https://github.com/user-attachments/assets/25f91e37-4443-4410-b8ec-e4bf8eb2b0e1)

![image](https://github.com/user-attachments/assets/f612fb92-3ea6-4121-8372-2d1fe15962ac)

![image](https://github.com/user-attachments/assets/ffc5e653-f82c-41a9-b5d4-0358b8ea3419)
![image](https://github.com/user-attachments/assets/f8ee16c9-dfbe-442f-8925-b91d4e5d637a)
![image](https://github.com/user-attachments/assets/93b3ee7b-a35a-4902-81c4-55ba7f09d2dd)






