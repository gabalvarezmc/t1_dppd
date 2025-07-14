# Clasificador de propinas de taxis en Nueva York

El proyecto aplica un modelo de clasificación Random Forest en datos de taxis de Nueva York durante el año 2020 para determinar aquellos viajes donde la propina dejada fue alta, o sea, mayor al 20% del costo total del viaje.


## 📖 Descripción

En este caso, el proyecto busca predecir si un viaje en taxi en Nueva York tuvo una propina alta, utilizando datos de viajes del año 2020, lo que puede ser útil para entender patrones de comportamiento de los pasajeros y mejorar la experiencia del servicio, así como entender mejor las dinámicas de propinas en el sector del transporte urbano.

En este proyecto se utilizan técnicas de procesamiento de datos, ingeniería de características y modelos de machine learning para lograr una clasificación efectiva.

Por su parte, se incluye el archivo respuestas.ipynb con respuestas a las preguntas propuestas en la formulación de la tarea.

---

## 🛠 Tecnologías

Lista de herramientas, librerías y versiones y lenguajes usados, por ejemplo:

- Python 3.9+
- pandas==2.3.1
- scikit-learn==1.7.0
- pyarrow==20.0.0
- fastparquet==2024.11.0
- matplotlib==3.10.3

---


## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/gabalvarezmc/t1_dppd.git
   cd t1_dppd
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejemplo de ejecución de los scripts principales:

Se utiliza el código pipeline_evaluate_months con tres argumentos de entrada: Año de comienzo, mes y cantidad de meses a evaluar. En base a estos parámetros se descarga la información de su respectiva URL.
```bash
python -m src.pipeline_evaluate_months 2020 2 10
```

IMPORTANTE: El funcionamiento del código está sujeto a congruencia en la url y disponibilidad de información del año y meses solicitados.