import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter


class PDFUnlocker(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Unlocker")
        self.geometry("520x430")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.pdf_path = None

        # -------------------------
        # Título
        # -------------------------
        self.title_label = ctk.CTkLabel(
            self,
            text="🔓 PDF Unlocker",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Genera una copia de tu PDF sin contraseña",
            font=ctk.CTkFont(size=14)
        )
        self.subtitle_label.pack(pady=(0, 25))

        # -------------------------
        # Selector de archivo
        # -------------------------
        self.file_button = ctk.CTkButton(
            self,
            text="📄  Seleccionar PDF",
            width=300,
            height=45,
            command=self.select_pdf
        )
        self.file_button.pack(pady=10)

        self.file_label = ctk.CTkLabel(
            self,
            text="Ningún archivo seleccionado",
            wraplength=430
        )
        self.file_label.pack(pady=(0, 20))

        # -------------------------
        # Contraseña
        # -------------------------
        self.password_label = ctk.CTkLabel(
            self,
            text="Contraseña"
        )
        self.password_label.pack(anchor="w", padx=110)

        self.password_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            show="•",
            placeholder_text="Introduce la contraseña"
        )
        self.password_entry.pack(pady=(5, 20))

        # -------------------------
        # Botón desbloquear
        # -------------------------
        self.unlock_button = ctk.CTkButton(
            self,
            text="🔓  Quitar contraseña",
            width=300,
            height=45,
            command=self.unlock_pdf
        )
        self.unlock_button.pack(pady=5)

        # -------------------------
        # Estado
        # -------------------------
        self.status_label = ctk.CTkLabel(
            self,
            text="",
            wraplength=430
        )
        self.status_label.pack(pady=20)

    # ==========================================
    # Seleccionar PDF
    # ==========================================

    def select_pdf(self):

        path = filedialog.askopenfilename(
            title="Seleccionar PDF",
            filetypes=[
                ("Archivos PDF", "*.pdf"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not path:
            return

        self.pdf_path = path

        filename = os.path.basename(path)

        self.file_label.configure(
            text=f"Archivo seleccionado:\n{filename}"
        )

        self.status_label.configure(text="")

    # ==========================================
    # Desbloquear PDF
    # ==========================================

    def unlock_pdf(self):

        if not self.pdf_path:
            messagebox.showwarning(
                "Falta el archivo",
                "Selecciona primero un archivo PDF."
            )
            return

        password = self.password_entry.get()

        if not password:
            messagebox.showwarning(
                "Falta la contraseña",
                "Introduce la contraseña del PDF."
            )
            return

        try:

            self.status_label.configure(
                text="Procesando PDF..."
            )

            self.update()

            # -------------------------
            # Abrir PDF
            # -------------------------

            reader = PdfReader(self.pdf_path)

            # Si está cifrado, lo desbloqueamos
            if reader.is_encrypted:

                result = reader.decrypt(password)

                if result == 0:
                    raise ValueError(
                        "La contraseña no es correcta."
                    )

            # -------------------------
            # Crear nuevo PDF
            # -------------------------

            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # -------------------------
            # Nombre de salida
            # -------------------------

            directory = os.path.dirname(self.pdf_path)

            filename = os.path.basename(self.pdf_path)

            name, extension = os.path.splitext(filename)

            output_path = os.path.join(
                directory,
                f"{name}_sin_clave{extension}"
            )

            # Evitar sobrescribir archivos existentes
            counter = 1

            while os.path.exists(output_path):

                output_path = os.path.join(
                    directory,
                    f"{name}_sin_clave_{counter}{extension}"
                )

                counter += 1

            # -------------------------
            # Guardar
            # -------------------------

            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            self.status_label.configure(
                text="✓ PDF desbloqueado correctamente"
            )

            messagebox.showinfo(
                "Proceso terminado",
                f"Se creó el archivo:\n\n"
                f"{output_path}"
            )

        except ValueError as error:

            self.status_label.configure(
                text="❌ No se pudo desbloquear el PDF."
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            self.status_label.configure(
                text="❌ Ocurrió un error."
            )

            messagebox.showerror(
                "Error",
                f"No fue posible procesar el PDF.\n\n"
                f"{error}"
            )


# ==========================================
# Ejecutar aplicación
# ==========================================

if __name__ == "__main__":

    app = PDFUnlocker()

    app.mainloop()