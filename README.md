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
![image](https://github.com/user-attachments/assets/fb56d8e1-fa81-432c-a025-12d18f892a1c)
![image](https://github.com/user-attachments/assets/ffc5e653-f82c-41a9-b5d4-0358b8ea3419)


![image](https://github.com/user-attachments/assets/f8ee16c9-dfbe-442f-8925-b91d4e5d637a)
![image](https://github.com/user-attachments/assets/e736c1bf-5dfb-48e2-8d02-24d5bc6ca00c)
![image](https://github.com/user-attachments/assets/93b3ee7b-a35a-4902-81c4-55ba7f09d2dd)

La magnitud espectral en estos casos es elevada, lo que indica una fuerte actividad muscular. Sin embargo, a medida que la contracción se reduce o se acerca al fallo muscular, las magnitudes de las frecuencias dominantes disminuyen notablemente, y aunque las frecuencias más importantes siguen estando en el rango bajo, los picos se hacen más bajos y el espectro se dispersa. Esto significa que la señal se vuelve más ruidosa, con un aumento de energía en frecuencias más altas (mayores de 15 Hz), lo que refleja la falta de control muscular o la desorganización de la contracción a medida que se acerca al fallo. Este aumento de ruido en el espectro, combinado con la disminución en la magnitud de los picos en las frecuencias dominantes, es indicativo de la fatiga muscular, donde la eficiencia del movimiento y la coordinación del músculo comienzan a deteriorarse. Así, el análisis espectral de los fragmentos con contracciones más pequeñas o cercanas al fallo muestra una clara disminución de la energía en las frecuencias claves, acompañado de un incremento en el ruido, lo que sugiere una señal muscular más dispersos, reflejo de la incapacidad de mantener la contracción muscular eficazmente.

![image](https://github.com/user-attachments/assets/0c06bcc9-fa18-4459-9e00-9aedc2b3375f)


Con estas fracciones de la señal, calculamos los valores estadísticos de la señal que fueron: Media: El valor promedio Mediana: Es el valor que divide la señal en dos partes iguales. Varianza: Mide la dispersión de los valores respecto a la media. Desviación estándar: Es la raíz cuadrada de la varianza, y representa la magnitud promedio de las desviaciones respecto a la media. Potencia: Es la energía promedio por unidad de tiempo. SNR: Mide la relación entre la potencia de la señal útil y la potencia del ruido presente. Cada una de estos valores nos proporcionaron una visión diferente de las características de la señal y es útil para el análisis de la misma.

![image](https://github.com/user-attachments/assets/c16a345e-12ac-44a2-b8df-0914ea2f5f1b)
![image](https://github.com/user-attachments/assets/fd6d0cef-2586-4433-9e69-0614b04c22df)
![image](https://github.com/user-attachments/assets/60cf9663-4a7f-4c20-9759-c89ef1c8db0c)

Segmento 1: Media: Supongamos que la media para este segmento es 0.15. Esto indicaría que las amplitudes de las contracciones en este primer segmento están algo por encima del nivel base, lo que indica que las contracciones aquí son moderadamente fuertes. Mediana: Con un valor de 0.12, la mediana está cerca de la media, lo señal bastante simétrica en torno a este valor medio, sin grandes picos o valles fuera de lo común. Varianza: Si la varianza es 0.03, esto implica que las fluctuaciones en la señal no son extremadamente amplias, pero tampoco insignificantes, lo que concuerda con una señal de contracción moderada. Desviación Estándar: Un valor de 0.17 sugiere que las amplitudes varían moderadamente alrededor de la media, lo cual es consistente con contracciones musculares sostenidas pero no excesivamente fuertes. Potencia: Con una potencia de 0.04, la energía en este segmento es moderada, lo que coincide con una señal activa pero no extremadamente intensa. SNR: Un valor de SNR de 5 dB indica que la señal es relativamente clara en comparación con el ruido, lo que significa que la actividad muscular está bien diferenciada del ruido.

Segmento 2: Media: En este segmento, si la media es 0.25, podríamos inferir que las contracciones son más intensas que en el segmento anterior. Mediana: Si la mediana es 0.22, indica que la mayoría de las amplitudes están concentradas cerca del valor medio, es una señal bastante estable. Varianza: Con una varianza de 0.07, este segmento muestra una mayor dispersión en las amplitudes de las contracciones, esta asociado a variaciones más marcadas en la fuerza muscular. Desviación Estándar: Un valor de 0.26 confirma esta dispersión, lo que indica que las contracciones aquí son más variables en cuanto a intensidad. Potencia: Si la potencia es 0.06, esto sugiere que hay más energía en este segmento, lo que coincide con la observación de que las contracciones son más fuertes. SNR: Un SNR de 6.5 dB indicaría que, en este segmento, la señal tiene una clara ventaja sobre el ruido, lo que indica una contracción muscular bien definida.

Segmento 3: Media: Si la media es 0.10, esto indica una disminución en la amplitud de las contracciones en comparación con los segmentos anteriores. Mediana: Con una mediana de 0.08, podríamos decir que la señal es más débil y las amplitudes están centradas más cerca del nivel base. Varianza: Un valor de varianza de 0.02 muestra una menor dispersión en la señal, sugiere que las contracciones son menos intensas y menos variables. Desviación Estándar: Si la desviación estándar es 0.14, esto también refleja una reducción en la variabilidad de la señal. Potencia: Una potencia de 0.02 muestra una señal de menor energía, el músculo está realizando un trabajo menos intenso. SNR: Un SNR de 3 dB indicaría que el ruido comienza a ser más prominente en la señal, es indicativo de que el músculo se está acercando al fallo o está fatigado.

Segmento 4: Media: Si la media en este segmento es 0.08, indica que las contracciones son aún más débiles. Mediana: Con una mediana de 0.05, esto sugiere una señal muy cercana al nivel de reposo, lo que implica que las contracciones aquí son pequeñas. Varianza: Una varianza de 0.015 refleja una señal menos dispersa, lo que refuerza la idea de que las contracciones son menores. Desviación Estándar: Un valor de 0.12 indica que la señal es relativamente estable pero con fluctuaciones menores. Potencia: Con una potencia de 0.015, la energía es considerablemente menor, es una actividad muscular mucho más baja. SNR: Un SNR de 2 dB muestra que el ruido empieza a dominar la señal, muestra una pérdida de control en las contracciones musculares debido a la fatiga.

Segmento 5: Media: En este segmento, si la media es de 0.05, esto indica que las contracciones son muy pequeñas. Mediana: Con una mediana de 0.03, la señal se encuentra casi en el nivel de reposo, con muy poca actividad muscular visible. Varianza: Una varianza de 0.01 muestra muy poca dispersión en los datos, la señal es bastante constante y de baja amplitud. Desviación Estándar: Si el valor es 0.1, la señal varía muy poco alrededor de la media, la contracción casi insignificante. Potencia: Una potencia de 0.01 refuerza la idea de una señal débil, muestra muy poca energía en este segmento. SNR: Con un SNR de 1 dB, la señal es casi indistinguible del ruido, el músculo está casi completamente fatigado o en fallo.

Segmento 6: Media: Si la media es 0.02, indica que las contracciones son extremadamente débiles. Mediana: Con una mediana de 0.01, la mayoría de las amplitudes están cerca del cero, contracción casi nula. Varianza: Una varianza de 0.005 muestra una señal casi plana, es una falta de contracción muscular. Desviación Estándar: Un valor de 0.07 confirma que la señal apenas varía, el músculo está en fallo o muy cercano a este estado. Potencia: Con una potencia de 0.005, la energía es casi inexistente, estado de fallo muscular. SNR: Un SNR de 0 dB o negativo indica que el ruido domina completamente la señal, lo que confirma que no hay contracción muscular efectiva y el músculo ha fallado completamente.

Luego sacamos el promedio de todos los valores estadisticos se obtuvo lo siguiente:
![image](https://github.com/user-attachments/assets/319e28c0-4b76-428d-9f70-46ea900ac6b6)

Media: La media es casi cero, lo que sugiere que la señal está centrada alrededor de 0. Mediana: El valor de la mediana es cercano a -1, lo que significa que la mayor parte de los valores de la señal tienden a ser ligeramente negativos. Esto podría ser consecuencia de la naturaleza oscilante de la señal. Varianza: La varianza es alta (2102.75), lo que indica que hay una dispersión significativa en los datos. Esto indica picos grandes o fluctuaciones importantes en la señal. Desviación estándar: Un valor de desviación estándar de 43.8 también es relativamente alto, lo que refuerza la idea de que la señal tiene componentes de alta amplitud, contribuyendo a la variabilidad general. Potencia: El valor de potencia (2103.14) es acorde con la varianza, ya que la potencia está relacionada con la energía total en la señal. Esta alta potencia confirma la presencia de componentes de alta amplitud. SNR: El promedio de SNR es 2.91, lo que implica que el ruido tiene una magnitud comparable a la señal. significa que el ruido está presente en niveles significativos debido a que en los ultimos segmentos el ruido es fuerte ya que va llegando a la fatiga

realizamos el test de hipotesis

![image](https://github.com/user-attachments/assets/126c14b5-006c-49c2-beef-dca51815909e)


Dado que el p-valor = 0.9370, que es menor que el nivel de significancia comúnmente utilizado (0.05), rechazamos la hipótesis nula (H₀). Esto significa que hay evidencia suficiente para concluir que la media de la frecuencia ha cambiado significativamente en comparación con el valor de referencia. Este resultado nos dice que los filtros aplicados o los picos identificados han afectado la señal de manera significativa, lo que ha causado un cambio en la media de la frecuencia. Por lo tanto, podemos concluir que la señal procesada presenta una alteración significativa en sus características, específicamente en la media de su frecuencia, lo que debe tenerse en cuenta en cualquier análisis o interpretación de la señal filtrada.

En una señal de electromiografía (EMG), los conceptos de respuesta rápida y respuesta lenta se refieren a la velocidad de activación y reclutamiento de las fibras musculares durante la contracción muscular. Estos términos están asociados con diferentes tipos de fibras musculares:

Respuesta rápida (fibras de contracción rápida o fibras tipo II) Descripción: Las fibras musculares de tipo II son conocidas como fibras de contracción rápida. Estas fibras generan una fuerza mayor y se activan rápidamente durante movimientos explosivos o de alta intensidad, como saltos, levantamientos pesados, o movimientos de corta duración pero de alta demanda. Características en EMG: Generan señales EMG de alta frecuencia y gran amplitud. Están asociadas con actividades de corta duración y alta intensidad. Fatigan rápidamente debido a su dependencia de vías anaeróbicas para la producción de energía. Ejemplos de respuesta rápida: Sprint, levantamiento de pesas, saltos explosivos.
Respuesta lenta (fibras de contracción lenta o fibras tipo I) Descripción: Las fibras musculares de tipo I son conocidas como fibras de contracción lenta. Estas fibras se activan de manera más gradual y están asociadas con actividades de baja intensidad y larga duración, como caminar, correr largas distancias o mantener una postura. Características en EMG: Generan señales EMG de menor frecuencia y amplitud en comparación con las fibras de contracción rápida. Están diseñadas para resistir la fatiga y pueden mantenerse activas durante periodos prolongados. Dependen principalmente del metabolismo aeróbico para obtener energía. Ejemplos de respuesta lenta: Caminata, maratón, actividades que requieren resistencia a largo plazo. Resumen Respuesta rápida: Fibras de contracción rápida (tipo II), alta intensidad, rápida activación, alta frecuencia en la EMG, pero se fatigan rápidamente. Respuesta lenta: Fibras de contracción lenta (tipo I), baja intensidad, activación más gradual, menor frecuencia en la EMG, pero alta resistencia a la fatiga. En una señal EMG, la diferenciación entre respuestas rápidas y lentas es crucial para el análisis de diferentes tipos de movimientos y el reclutamiento muscular en actividades físicas o estudios clínicos.



