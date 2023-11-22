
# Pruebas con Streamlit

Las credenciales de administrador por defecto son ```admin / admin```.

## Aclaraciones

La inicialización de la base de datos es temporal y solo para mostrar datos de prueba, el almacenamiento de contraseñas en texto plano también.

## Howto
Probado con Python 3.11

### Desde consola

```
pip install -r requirements.txt
```

```
streamlit run app.py
```

### Por contenedor Docker

```
docker build -t app-prueba-streamlit .
```

```
docker run -dp 8501:8501 app-prueba-streamlit
```

---

Acceso desde ```http://localhost:8501/```
