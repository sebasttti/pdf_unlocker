# PDF Unlocker — Comandos

## 1. Instalar las dependencias del proyecto

```bash
pip install customtkinter pypdf
```

## 2. Instalar PyInstaller

```bash
pip install pyinstaller
```

## 3. Verificar que PyInstaller quedó instalado

```bash
pyinstaller --version
```

O usando Python directamente:

```bash
python -m PyInstaller --version
```

## 4. Generar el ejecutable

Desde la carpeta donde está `pdf_unlocker.py`:

```bash
pyinstaller --onefile --windowed pdf_unlocker.py
```
```bash
python -m PyInstaller --onefile --windowed pdf_unlocker.py
```

## 5. Generar el ejecutable con icono (opcional)

```bash
pyinstaller --onefile --windowed --icon=icon.ico pdf_unlocker.py
```
```bash
python -m PyInstaller --onefile --windowed pdf_unlocker.py
```

## Resultado

Después de ejecutar PyInstaller encontrarás algo parecido a:

```text
Proyecto/
├── pdf_unlocker.py
├── build/
├── dist/
│   └── pdf_unlocker.exe
└── pdf_unlocker.spec
```

El archivo que distribuirías es:

```text
dist/pdf_unlocker.exe
```

El `.exe` puede ejecutarse en otros equipos Windows sin necesidad de instalar Python, porque PyInstaller empaqueta el intérprete y las dependencias necesarias.
