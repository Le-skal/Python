import tkinter as tk
from tkinter import filedialog, messagebox
import os
import requests

# On importe les fonctions de main.py
import main


def run():
    def action_charger_fichier():
        filepath = filedialog.askopenfilename(
            title="Sélectionner le fichier bankaccount.txt",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
        )

        if filepath:
            try:
                banque, agence, compte, idNational, iban = main.charger_fichier(
                    filepath
                )

                # Mise à jour des variables Tkinter
                banque_var.set(banque)
                agence_var.set(agence)
                compte_var.set(compte)
                id_national_var.set(idNational)
                iban_var.set(iban)

                fichier_label.config(text=f"Fichier: {os.path.basename(filepath)}")

            except Exception as e:
                messagebox.showerror(
                    "Erreur", f"Erreur lors de la lecture du fichier:\n{str(e)}"
                )

    def action_valider_iban():
        iban = iban_var.get()
        if not iban:
            messagebox.showwarning(
                "Avertissement", "Veuillez charger ou saisir un IBAN"
            )
            return

        api_key = "261f79768b16828f01ba93b650631c6d2d17b550"
        url = f"https://api.ibanapi.com/v1/validate/{iban}?api_key={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            # Check all validations
            validations = data.get("validations", [])
            failed_validations = [
                v["message"] for v in validations if v.get("result") != 200
            ]

            if not failed_validations:
                messagebox.showinfo("Résultat", f"Valid IBAN:\n{data.get('message')}")
            else:
                messagebox.showerror(
                    "Résultat", "Invalid IBAN:\n" + "\n".join(failed_validations)
                )

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue:\n{str(e)}")

    # -------------------------
    # Interface Tkinter
    # -------------------------
    root = tk.Tk()
    root.title("Générateur d'IBAN")
    root.geometry("500x500")
    root.resizable(False, False)

    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(
        main_frame, text="Générateur d'IBAN Français", font=("Arial", 16, "bold")
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    load_button = tk.Button(
        main_frame,
        text="Charger le fichier bankaccount.txt",
        command=action_charger_fichier,
        width=30,
        height=2,
    )
    load_button.grid(row=1, column=0, columnspan=2, pady=(0, 20))

    fichier_label = tk.Label(
        main_frame, text="Aucun fichier chargé", font=("Arial", 10)
    )
    fichier_label.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    validate_button = tk.Button(
        main_frame,
        text="Valider l'IBAN",
        command=action_valider_iban,
        width=30,
        height=2,
        bg="#4CAF50",
        fg="white",
    )
    validate_button.grid(row=9, column=0, columnspan=2, pady=(20, 10))

    # Variables
    global banque_var, agence_var, compte_var, id_national_var, iban_var
    banque_var = tk.StringVar()
    agence_var = tk.StringVar()
    compte_var = tk.StringVar()
    id_national_var = tk.StringVar()
    iban_var = tk.StringVar()

    # Labels
    tk.Label(main_frame, text="Code banque:", font=("Arial", 10)).grid(
        row=3, column=0, sticky="w", pady=5
    )
    tk.Label(main_frame, textvariable=banque_var, font=("Arial", 10, "bold")).grid(
        row=3, column=1, sticky="w", pady=5
    )

    tk.Label(main_frame, text="Code agence:", font=("Arial", 10)).grid(
        row=4, column=0, sticky="w", pady=5
    )
    tk.Label(main_frame, textvariable=agence_var, font=("Arial", 10, "bold")).grid(
        row=4, column=1, sticky="w", pady=5
    )

    tk.Label(main_frame, text="Numéro de compte:", font=("Arial", 10)).grid(
        row=5, column=0, sticky="w", pady=5
    )
    tk.Label(main_frame, textvariable=compte_var, font=("Arial", 10, "bold")).grid(
        row=5, column=1, sticky="w", pady=5
    )

    tk.Label(main_frame, text="Identifiant national:", font=("Arial", 10)).grid(
        row=6, column=0, sticky="w", pady=5
    )
    tk.Label(main_frame, textvariable=id_national_var, font=("Arial", 10, "bold")).grid(
        row=6, column=1, sticky="w", pady=5
    )

    tk.Label(main_frame, text="IBAN généré:", font=("Arial", 12, "bold")).grid(
        row=7, column=0, sticky="w", pady=(20, 5)
    )
    tk.Label(
        main_frame, textvariable=iban_var, font=("Arial", 12, "bold"), fg="blue"
    ).grid(row=7, column=1, sticky="w", pady=(20, 5))

    root.mainloop()
