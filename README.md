# ConversaCutAI 🎙️

![ConversaCutAI Logo](assets/logo.png)

## 📌 Descripción

**ConversaCutAI** es una aplicación de escritorio que permite analizar archivos de audio y detectar automáticamente los fragmentos donde existe voz humana.

Su objetivo es facilitar la edición de grabaciones largas, eliminando silencios innecesarios y generando archivos de audio recortados con las partes importantes de una conversación.

---

## ✨ Características principales

✅ Detección automática de voz mediante inteligencia artificial  
✅ Eliminación de silencios prolongados  
✅ Procesamiento de archivos de audio WAV  
✅ Interfaz gráfica sencilla y moderna  
✅ Configuración personalizable mediante `config.json`  
✅ Generación automática de reportes de procesamiento  
✅ Exportación del audio procesado

---

## 🖥️ Capturas

*(Próximamente)*

---

## 🛠️ Tecnologías utilizadas

- Python 3.12
- CustomTkinter (interfaz gráfica)
- Silero VAD (detección de voz con IA)
- PyTorch
- Torchaudio
- PyDub
- SoundFile

---

## 📂 Estructura del proyecto

```text
ConversaCutAI/
│
├── app.py                 # Inicio de la aplicación
├── interfaz.py            # Interfaz gráfica
├── main.py                # Punto de entrada
├── config.json            # Configuración del programa
│
├── core/
│   └── procesador.py      # Motor de procesamiento de audio
│
├── utils/
│   └── rutas.py           # Gestión de rutas
│
├── assets/
│   └── logo.png           # Recursos gráficos
│
└── ConversaCutAI.spec     # Configuración de PyInstaller
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/alonshom/ConversaCutAI.git
```

### 2. Entrar en la carpeta

```bash
cd ConversaCutAI
```

### 3. Crear entorno virtual

```bash
python -m venv .venv
```

### 4. Activar entorno virtual

Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

Ejecutar la aplicación:

```bash
python main.py
```

Flujo de uso:

1. Seleccionar un archivo de audio.
2. Iniciar el procesamiento.
3. Esperar el análisis de voz.
4. Obtener el archivo procesado.

---

## ⚙️ Configuración

La configuración del programa se encuentra en:

```text
config.json
```

Permite modificar parámetros como:

- Sensibilidad de detección.
- Duración mínima de voz.
- Duración mínima de silencio.
- Espaciado antes y después de fragmentos detectados.

---

## 📦 Compilación

Para crear el ejecutable:

```bash
pyinstaller ConversaCutAI.spec
```

El archivo generado aparecerá en:

```text
dist/
```

---

## 📄 Licencia

Este proyecto actualmente no posee una licencia definida.

---

## 👤 Autor

**Alonshom**

Proyecto desarrollado con Python e inteligencia artificial para procesamiento automático de audio.