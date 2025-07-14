# Clasificador de propinas de taxis en Nueva York

El proyecto aplica un modelo de clasificación Random Forest en datos de taxis de Nueva York durante el año 2020 para determinar aquellos viajes donde la propina dejada fue alta, o sea, mayor al 20% del costo total del viaje.


## 📖 Descripción

En este caso, el proyecto busca predecir si un viaje en taxi en Nueva York tuvo una propina alta, utilizando datos de viajes del año 2020, lo que puede ser útil para entender patrones de comportamiento de los pasajeros y mejorar la experiencia del servicio, así como entender mejor las dinámicas de propinas en el sector del transporte urbano.

En este proyecto se utilizan técnicas de procesamiento de datos, ingeniería de características y modelos de machine learning para lograr una clasificación efectiva.

---

## 🛠 Tecnologías

Lista de herramientas, librerías y versiones y lenguajes usados, por ejemplo:

- Python 3.9+
- pandas
- scikit-learn
- pyarrow
- fastparquet

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

Procesar datos:
```bash
python -m src.data.dataset
```

Generar características:
```bash
python -m src.features.build_features
```

Entrenar modelo:
```bash
python -m src.modeling.train
```

Realizar predicciones:
```bash
python -m src.modeling.predict
```
