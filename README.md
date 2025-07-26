# Análisis Exploratorio de Datos de Producción Industrial

Este proyecto contiene un análisis exploratorio de datos (EDA) aplicado a un dataset de una empresa industrial colombiana que opera 24/7, produciendo alrededor de 100 productos por hora con un promedio de 2 unidades defectuosas por ciclo.

## 📊 Objetivo

Investigar la posible relación entre las unidades defectuosas y distintas variables del proceso productivo como:
- Máquina utilizada
- Operador responsable
- Turno de trabajo
- Variables ambientales (temperatura, humedad, vibración)
- Tiempo de ciclo

## 🔍 Contenido

El análisis se estructura en las siguientes secciones:

1. **Preparación del Dataset**  
   Estandarización de codificación, limpieza de caracteres especiales y formato de fechas.

2. **Análisis Inicial de Fallos**  
   Revisión de la variable `fallo_detectado` y cambio de enfoque a `unidades_defectuosas`.

3. **Evaluación por Máquina**  
   Comparación entre producción total, unidades defectuosas y cálculo de porcentajes por máquina.

4. **Análisis por Operador**  
   Estudio del desempeño de los operadores en relación a errores.

5. **Análisis por Turno**  
   Exploración de la influencia del turno de trabajo sobre los defectos.

6. **Estudio de Correlaciones**  
   Mapa de calor de correlaciones entre variables numéricas.

7. **Series de Tiempo**  
   Análisis mensual y diario de la cantidad de unidades defectuosas.

7.1 **Estadísticas Descriptivas**  
   Medidas como promedio, mediana, varianza y desviación estándar para cuantificar la estabilidad del sistema.

8. **Conclusiones**  
   El número de unidades defectuosas es estable y no parece depender significativamente de otras variables registradas.

## 🛠️ Tecnologías Utilizadas

- Python 3
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook


## 📌 Notas

- El dataset analizado se asumió proveniente de una empresa industrial en Colombia.
- No se identificaron patrones anormales ni relaciones claras con otras variables.
- Se sugiere explorar modelos de series de tiempo o detección de anomalías para futuros análisis.

## Creditos

- Jhon Steven Velasquez
- Luis Miguel Lopez
- Michael Moreno
