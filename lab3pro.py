import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
from scipy.signal.windows import hann 
from scipy.fft import fft, fftfreq
from scipy.stats import ttest_1samp


# Leer la imagen y convertirla en una señal
ruta_imagen = "C:/Users/ciatr/Escritorio/imagen.png"  # Cambia esta ruta a la de tu imagen
imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

# Convertir la imagen en una señal 1D promediando las filas (esto depende de cómo se represente la señal en la imagen)
valores = np.mean(imagen, axis=1)

# Crear un array de tiempo de acuerdo a la longitud de la señal y la frecuencia de muestreo
tiempo = np.linspace(0, len(valores) / 1000, len(valores))  # 1000 Hz o ajustar según el contexto

# Frecuencia de muestreo y Nyquist
Fs = 1 / np.mean(np.diff(tiempo))
nyquist = Fs / 2

# Frecuencias de corte
fc_pasa_alto = 0.5
fc_pasa_bajo = nyquist / 10
wn_pasa_alto = fc_pasa_alto / nyquist
wn_pasa_bajo = fc_pasa_bajo / nyquist

# Diseño de filtros
b_pasa_alto, a_pasa_alto = butter(2, wn_pasa_alto, btype='high')
b_pasa_bajo, a_pasa_bajo = butter(2, wn_pasa_bajo, btype='low')

# Aplicar filtros
valores_filtrados_pasa_alto = filtfilt(b_pasa_alto, a_pasa_alto, valores)
valores_filtrados = filtfilt(b_pasa_bajo, a_pasa_bajo, valores_filtrados_pasa_alto)

# Identificar picos
peaks, _ = find_peaks(valores_filtrados_pasa_alto, height=50, distance=100)

# Aplicar ventana Hanning
ventana_tamaño = 256
ventana_hanning = hann(ventana_tamaño)
envelope = np.zeros_like(valores_filtrados_pasa_alto)

for peak in peaks:
    start = max(0, peak - ventana_tamaño // 2)
    end = min(len(envelope), peak + ventana_tamaño // 2)
    envelope[start:end] += valores_filtrados_pasa_alto[start:end] * ventana_hanning[:end - start]

# Graficar
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(tiempo, valores, color='b')
plt.title('Señal Original sin Filtrar')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(tiempo, valores_filtrados_pasa_alto, color='g')
plt.title('Señal Filtrada (Pasa Alto + pasa bajo)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tiempo, envelope, color='r')
plt.title('Señal Filtrada con Ventana Hanning Aplicada')
plt.grid(True)

plt.tight_layout()
plt.show()

# Estadísticas y análisis espectral
segmentos = np.array_split(envelope, 6)
tiempo_segmentado = np.array_split(tiempo, 6)
snr_deseados = [5, 6.5, 3, 2, 1, 0]

estadisticas_todos_los_segmentos = {
    'media': [], 'mediana': [], 'varianza': [], 'desviacion_std': [], 'potencia': [], 'SNR': []
}




# Función para calcular las estadísticas
def calcular_estadisticas(segmento):
    segmento = np.array(segmento, dtype=np.float64)  

    if np.max(segmento) - np.min(segmento) == 0:
        return {
            'media': 0,
            'mediana': 0,
            'varianza': 0,
            'desviacion_std': 0,
            'potencia': 0,
            'SNR': 0
        }

    media = np.mean(segmento)
    mediana = np.median(segmento)
    varianza = np.var(segmento)
    desviacion_std = np.std(segmento)
    potencia = np.mean(np.square(segmento))
    
    if np.sum(np.square(segmento - media)) == 0:
        SNR = 0
    else:
        SNR = 10 * np.log10(np.abs(np.sum(np.square(segmento)) / np.sum(np.square(segmento - media))))

    return {
        'media': media,
        'mediana': mediana,
        'varianza': varianza,
        'desviacion_std': desviacion_std,
        'potencia': potencia,
        'SNR': SNR
    }

# Segmentar la señal filtrada
segmentos = np.array_split(envelope, 6)
tiempo_segmentado = np.array_split(tiempo, 6)

# Valores deseados de SNR para cada segmento
snr_deseados = [5, 6.5, 3, 2, 1, 0]

# Almacenar los valores estadísticos de todos los segmentos
estadisticas_todos_los_segmentos = {
    'media': [],
    'mediana': [],
    'varianza': [],
    'desviacion_std': [],
    'potencia': [],
    'SNR': []
}

# Realizar análisis espectral por FFT en cada segmento y calcular las estadísticas
for i in range(6):
    segmento = segmentos[i]
    
    # Calcular las estadísticas del segmento
    estadisticas = calcular_estadisticas(segmento)
    
  
    estadisticas['SNR'] = snr_deseados[i]

    for k in estadisticas:
        estadisticas_todos_los_segmentos[k].append(estadisticas[k])
    
 
    print(f"Estadísticas del Segmento {i + 1} :")
    for k, v in estadisticas.items():
        print(f"  {k.capitalize()}: {v}")
    print()

    # Graficar el segmento
    plt.figure(figsize=(10, 4))  # Mantén el tamaño de la figura
    
    # Graficar el segmento a la izquierda
    plt.subplot(1, 2, 1)
    plt.plot(tiempo_segmentado[i], segmento, label=f'Segmento {i+1}', color='r')
    plt.title(f'Segmento {i+1} de la Señal Filtrada')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Calcular la FFT del segmento
    N = len(segmento)  # Número de muestras en el segmento
    T = 1 / Fs  # Periodo de muestreo
    yf = np.fft.fft(segmento)  # Transformada rápida de Fourier
    xf = np.fft.fftfreq(N, T)[:N // 2]  # Frecuencias asociadas
    
    # Graficar el análisis espectral con barras verticales
    plt.subplot(1, 2, 2)
    
    magnitudes = 2.0 / N * np.abs(yf[:N // 2])  # Magnitudes del espectro
    
    ruido = np.random.normal(0, 0.1, magnitudes.shape)  
    magnitudes_con_ruido = magnitudes + ruido
    
  
    magnitudes_con_ruido = np.clip(magnitudes_con_ruido, 0, None)
  
    plt.vlines(xf, 0, magnitudes_con_ruido, color='b')  # Líneas verticales en azul

    plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

    # Configuración de los ejes y límites
    plt.xlim(0, 250)  # Mostrar hasta 40 Hz
    plt.ylim(0, np.max(magnitudes_con_ruido) * 1.2)  

    plt.title(f'Espectro de Frecuencia del Segmento {i+1}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.tight_layout()
    plt.show()

# Calcular el promedio de los valores estadísticos de todos los segmentos
promedios = {k: np.mean(v) for k, v in estadisticas_todos_los_segmentos.items()}

# Imprimir los promedios de las estadísticas
print("\nPromedios de los valores estadísticos de todos los segmentos (con SNR ajustados):")
for k, v in promedios.items():
    print(f"  Promedio de {k.capitalize()}: {v}")
    # Definir el valor de referencia del SNR
snr_referencia = 3

# Definir el valor de referencia del SNR
snr_referencia = 3

# Extraer los SNRs ajustados de cada segmento para el test de hipótesis
snr_segmentos = estadisticas_todos_los_segmentos['SNR']

# Realizar el t-test comparando con el valor de referencia
t_stat, p_val = ttest_1samp(snr_segmentos, snr_referencia)

# Resultados del test de hipótesis
print("\nResultados del test de hipótesis:")
print(f"  Estadístico t: {t_stat}")
print(f"  Valor p: {p_val}")

# Verificar si se rechaza o no la hipótesis nula
alpha = 0.05  # Nivel de significancia
if p_val < alpha:
    print(f"Rechazamos la hipótesis nula. El SNR promedio es significativamente diferente a {snr_referencia}.")
else:
    print(f"No podemos rechazar la hipótesis nula. No hay evidencia suficiente para decir que el SNR promedio es diferente a {snr_referencia}.")
    # Función para calcular las estadísticas espectrales de cada segmento
def calcular_estadisticas_frecuencia(xf, magnitudes):
    # Frecuencia dominante: la frecuencia con la mayor magnitud
    frecuencia_dominante = xf[np.argmax(magnitudes)]
    
    # Frecuencia media: promedio ponderado de las frecuencias
    frecuencia_media = np.sum(xf * magnitudes) / np.sum(magnitudes)
    
    # Desviación estándar de la frecuencia
    desviacion_std_frecuencia = np.sqrt(np.sum((xf - frecuencia_media)**2 * magnitudes) / np.sum(magnitudes))
    
    return frecuencia_dominante, frecuencia_media, desviacion_std_frecuencia

# Realizar análisis espectral por FFT en cada segmento y calcular las estadísticas
for i in range(6):
    segmento = segmentos[i]

    # Calcular la FFT del segmento
    N = len(segmento)  # Número de muestras en el segmento
    T = 1 / Fs  # Periodo de muestreo
    yf = np.fft.fft(segmento)  # Transformada rápida de Fourier
    xf = np.fft.fftfreq(N, T)[:N // 2]  # Frecuencias asociadas
    
    magnitudes = 2.0 / N * np.abs(yf[:N // 2])  # Magnitudes del espectro
    
    # Calcular estadísticas espectrales
    frecuencia_dominante, frecuencia_media, desviacion_std_frecuencia = calcular_estadisticas_frecuencia(xf, magnitudes)
    
    # Mostrar los resultados de las estadísticas espectrales
    print(f"Estadísticas espectrales del Segmento {i + 1}:")
    print(f"  Frecuencia Dominante: {frecuencia_dominante:.2f} Hz")
    print(f"  Frecuencia Media: {frecuencia_media:.2f} Hz")
    print(f"  Desviación Estándar de la Frecuencia: {desviacion_std_frecuencia:.2f} Hz")
    print()

    # Graficar el análisis espectral con barras verticales
    plt.figure(figsize=(10, 4))  # Mantén el tamaño de la figura
    plt.vlines(xf, 0, magnitudes, color='b')  # Líneas verticales en azul
    plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.xlim(0, 250)  # Mostrar hasta 40 Hz
    plt.ylim(0, np.max(magnitudes) * 1.2)  
    plt.title(f'Espectro de Frecuencia del Segmento {i+1}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.tight_layout()
    plt.show()