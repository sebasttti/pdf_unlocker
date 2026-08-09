# 🔓 PDF Unlocker

Aplicación de escritorio para **eliminar la contraseña de archivos PDF cuando se conoce la contraseña original**.

El procesamiento se realiza completamente de forma local, por lo que los documentos no necesitan ser enviados a ningún servidor.

## ✨ Características

* 🔐 Permite abrir PDFs protegidos con contraseña.
* 🔓 Genera una copia sin contraseña.
* 📄 Conserva el archivo original intacto.
* 💻 Aplicación de escritorio para Windows.
* 🔒 Procesamiento 100% local.
* 🎨 Interfaz gráfica sencilla y moderna.
* 📦 Puede convertirse en un ejecutable `.exe` independiente.

## 🛠️ Tecnologías

* **Python**
* **CustomTkinter** — interfaz gráfica
* **pypdf** — procesamiento de archivos PDF
* **PyInstaller** — generación del ejecutable para Windows

## 📋 Requisitos

Para ejecutar el proyecto desde código fuente necesitas:

* Python 3.10 o superior
* pip

## 🚀 Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd pdf-unlocker
```

Instala las dependencias:

```bash
pip install customtkinter pypdf
```

## ▶️ Ejecutar la aplicación

```bash
python pdf_unlocker.py
```

La aplicación permite:

1. Seleccionar un archivo PDF.
2. Introducir la contraseña conocida.
3. Generar una copia del documento sin contraseña.

Por ejemplo:

```text
Declaracion_Renta_2025.pdf
        ↓
Declaracion_Renta_2025_sin_clave.pdf
```

El archivo original no se modifica.

## 📦 Generar ejecutable para Windows

Instala PyInstaller:

```bash
pip install pyinstaller
```

Comprueba la instalación:

```bash
python -m PyInstaller --version
```

Genera el ejecutable:

```bash
pyinstaller --onefile --windowed pdf_unlocker.py
```

El resultado estará en:

```text
dist/pdf_unlocker.exe
```

El ejecutable puede utilizarse en equipos Windows sin necesidad de instalar Python.

### Ejecutable con icono

Si el proyecto incluye un archivo `icon.ico`:

```bash
pyinstaller --onefile --windowed --icon=icon.ico pdf_unlocker.py
```

## 📁 Estructura del proyecto

```text
pdf-unlocker/
│
├── pdf_unlocker.py
├── README.md
├── .gitignore
│
├── build/
├── dist/
└── pdf_unlocker.spec
```

Los directorios y archivos generados por PyInstaller están incluidos en `.gitignore`.

## 🔐 Seguridad y privacidad

El aplicativo **no intenta descubrir, romper ni adivinar contraseñas**.

La contraseña debe ser conocida por el usuario y proporcionada durante el proceso.

Los archivos PDF se procesan localmente en el equipo del usuario. No se requiere conexión a un servicio externo ni se cargan documentos a Internet.

## ⚠️ Limitaciones

La aplicación está diseñada para PDFs protegidos mediante contraseña que el usuario conoce.

Algunos documentos pueden utilizar mecanismos de protección o características de PDF que no sean completamente compatibles con la biblioteca utilizada.

## 📄 Licencia

Este proyecto puede distribuirse y modificarse según los términos de la licencia que se defina para el repositorio.

```
```
