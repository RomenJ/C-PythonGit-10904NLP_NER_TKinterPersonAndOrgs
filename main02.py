import tkinter as tk
from tkinter import filedialog, messagebox
import spacy

# Función para cargar el archivo .txt
def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        try:
            with open(filepath, encoding='utf-8') as file:
                text = file.read()
                # Mostrar el texto cargado en el área de texto
                loaded_text.delete("1.0", "end")
                loaded_text.insert("1.0", text)
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {e}")

# Función para analizar el texto y encontrar coincidencias
def analyze_text():
    text = loaded_text.get("1.0", "end-1c")  # Obtener el texto de la entrada
    if not text.strip():
        messagebox.showwarning("Advertencia", "Por favor, carga un archivo o introduce texto para analizar.")
        return

    nlp = spacy.load('en_core_web_md')
    document = nlp(text)

    target = target_entry.get().lower()
    person_count = 0
    org_count = 0

    for named_entity in document.ents:
        if named_entity.label_ == "PERSON" and target.lower() in named_entity.text.lower():
            person_count += 1
            start = max(named_entity.start - 20, 0)
            end = min(named_entity.end + 20, len(document))
            surrounding_text = document[start:end].text
            messagebox.showinfo("Coincidencia encontrada", f"Contexto del target: {target}\n20 palabras antes del target: {document[start:named_entity.start].text}\n20 palabras después del target: {document[named_entity.end:end].text}")
        elif named_entity.label_ == "ORG" and target.lower() in named_entity.text.lower():
            org_count += 1
            start = max(named_entity.start - 20, 0)
            end = min(named_entity.end + 20, len(document))
            surrounding_text = document[start:end].text
            messagebox.showinfo("Coincidencia encontrada", f"Contexto del target: {target}\n20 palabras antes del target: {document[start:named_entity.start].text}\n20 palabras después del target: {document[named_entity.end:end].text}")

    messagebox.showinfo("Resultados", f"Conclusión del NER:\n. Target: {target}\n. Coincidencias con personas (PERSON): {person_count}\n. Coincidencias con organizaciones (ORG): {org_count}")

# Crear ventana principal
root = tk.Tk()
root.title("NER ORG & PERS App")
root.configure(bg='light blue')
target_label0 = tk.Label(root, text="PERSON & ORG FINDER")
target_label0.pack(pady=5)
target_label0.configure(bg='light blue')
target_label01 = tk.Label(root, text="English version for spanish user")
target_label01.pack(pady=5)
target_label01.configure(bg='light blue')

# Crear widgets
load_button = tk.Button(root, text="\u21BA Cargar archivo en inglés", command=load_file)  # Unicode para flecha circular ↺
load_button.pack(pady=5)

file_frame = tk.Frame(root)
file_frame.pack(pady=5)
file_frame.configure(bg='light blue')
file_label = tk.Label(file_frame, text="Texto cargado:")
file_label.pack(side="left", padx=5)
file_label.configure(bg='light blue')

loaded_text = tk.Text(file_frame, width=40, height=10)
loaded_text.pack(side="left", padx=5)

target_label = tk.Label(root, text="Persona u Organización a buscar:")
target_label.pack(pady=5)
target_label.configure(bg='light blue')

target_entry = tk.Entry(root)
target_entry.pack()

# Añadir etiquetas para guiar a los usuarios
instructions_label = tk.Label(root, text="Pasos:\n  1. Haz clic en 'Cargar archivo' para seleccionar un archivo .txt.\n  2. Introduce un objetivo en el campo 'Objetivo'.\n  3. Haz clic en 'Analizar texto' para encontrar coincidencias de entidades PERSON y ORG.", justify="left")
instructions_label.pack(pady=5)
instructions_label.configure(bg='light blue')

analyze_button = tk.Button(root, text="Analizar texto \u27A4", command=analyze_text)  # Unicode para flecha hacia la derecha ➤
analyze_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
