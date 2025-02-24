import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar, OptionMenu
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import osmnx as ox

ox.settings.log_console=True
ox.settings.use_cache=True

root = tk.Tk()
root.geometry("1600x950")
root.title('ANTSZON Application')

# Obtention du chemin du dossier actuel pour l'insertion des images
current_directory = os.path.dirname(__file__)

# Construction du chemin de l'image
image_path = os.path.join(current_directory, "Images", "Ants.png")
image_path1 = os.path.join(current_directory, "Images", "AntsColony.png")
image_path2 = os.path.join(current_directory, "Images", "MessageBox.png")

#Liste ID_Trajets
Id_trajets = ["Option 1", "Option 2", "Option 3"]

# Insertion de l'image
image = Image.open(image_path)
image = image.resize((550, 375))  # Redimensionnez l'image selon vos besoins
image_tk = ImageTk.PhotoImage(image)

image1 = Image.open(image_path1)
image1 = image1.resize((550, 375))  # Redimensionnez l'image selon vos besoins
image_tk1 = ImageTk.PhotoImage(image1)

image2 = Image.open(image_path2)
image2 = image2.resize((250, 250))  # Redimensionnez l'image selon vos besoins
image_tk2 = ImageTk.PhotoImage(image2)


# Home Page
def home_page():
    home_frame = tk.Frame(main_frame)


    # Ajouter du contenu au cadre
    btn = tk.Button(home_frame, text="Generer", font=(15), fg="White", bd=0, bg="green", width=50, height=3)
    btn.pack(pady=20, padx=20)

    Graph2 = tk.Frame(home_frame,)
    Graph2.pack(fill=tk.BOTH, padx=20, pady=20)

    # Graphs
    # Graphs_path = os.path.join(current_directory, "Images","Data")

    home_frame.pack(fill=tk.BOTH, expand=True)

# Delyvery Page
def Graphs_page():
    Graphs_frame = tk.Frame(main_frame)

    lb = tk.Label(Graphs_frame, text="Graphs Page", font=('Bold', 15))
    lb.pack()

    dropdown = ttk.Combobox(Graphs_frame, values=Id_trajets)
    dropdown.place(x=100, y=100)

    button = tk.Button(Graphs_frame, text="Generate", command=lambda: generate_graph(dropdown.get()))
    button.place(x=250, y=100)

    Cartetitle = tk.Label(Graphs_frame, text="Graph :", font=('Roman', 15))
    Cartetitle.place(x=100, y=200)

    def generate_graph(selected_trajet):
        Trajet_path = os.path.join(current_directory, "Images", "Data", selected_trajet)

        image_label = tk.Label(Graphs_frame, image=image_tk, bg="darkgray")
        image_label.place(x=750, y=550)
        return (Trajet_path)

    # Le reste du code pour générer le graphique en utilisant Trajet_path

    Graphs_frame.pack(fill=tk.BOTH, expand=True)



#Journey Page
def Journey_page():
    Journey_frame = tk.Frame(main_frame)

    lb =tk.Label(Journey_frame, text="Journey Page", font=('Bold',15))
    lb.pack()



    Journey_frame.pack(fill=tk.BOTH, expand=True)

#About Us Page
def About_page():
    About_frame = tk.Frame(main_frame, bg="darkgray",)

    # Titre
    title_label = tk.Label(About_frame, text="The ANTSZON CORP", font=("Roman", 26, "bold"), foreground="red",bg="darkgray")
    title_label.pack(pady=50)

    # Présentation de l'équipe
    team_label = tk.Label(About_frame, text="Notre equipe :", font=("Roman", 20),foreground="red", bg="darkgray")
    team_label.pack()

    team_description = tk.Label(About_frame, text="""Nous sommes une équipe passionnée composée d'experts en développement, en design et en gestion de projet.
    Notre équipe diversifiée allie créativité, expertise technique et dévouement pour offrir des solutions innovantes à nos clients.""",
                                height = 5 ,width=100, font=("Roman", 18), bg="darkgray")
    team_description.pack(pady=10 ,padx=10)

    # Objectif principal
    objective_label = tk.Label(About_frame, text="Notre objectif principal :", font=("Roman", 18),foreground="red", bg="darkgray")
    objective_label.pack()

    objective_description = tk.Label(About_frame,text="""Notre objectif principal est de fournir des produits et services de haute qualité
    qui répondent aux besoins de nos clients. Nous nous engageons à être à l'avant-garde de la technologie et à créer des solutions sur mesure
    qui ajoutent de la valeur à nos clients et à leurs utilisateurs."""
                                    , height = 5 , width=100, font=("Roman", 18), bg="darkgray")
    objective_description.pack(pady=10)


    image_label = tk.Label(About_frame, image=image_tk, bg="darkgray")
    image_label.place(x=750, y=550)

    image_label1 = tk.Label(About_frame, image=image_tk2, bg="darkgray")
    image_label1.place(x=560, y=(500))


    About_frame.pack(fill=tk.BOTH, expand=True)

#Settings Page
def Settings_page():
    Settings_frame = tk.Frame(main_frame)

    lb =tk.Label(Settings_frame, text="Settings Page", font=('Roman',35), foreground="red")
    lb.pack(pady=25)

#Function Save Settings
    def save_settings():
        new_settings = {
            "COLIS_PETIT_POIDS": petit_poids_entry.get(),
            "COLIS_MOYEN_POIDS": moyen_poids_entry.get(),
            "COLIS_GRAND_POIDS": grand_poids_entry.get(),
            "COLIS_EXCEPT_POIDS": except_poids_entry.get(),
            "COLIS_PETIT_VOLUME": petit_volume_entry.get(),
            "COLIS_MOYEN_VOLUME": moyen_volume_entry.get(),
            "COLIS_GRAND_VOLUME": grand_volume_entry.get(),
            "COLIS_EXCEPT_VOLUME": except_volume_entry.get(),
            "PROBA_TAILLE": proba_taille_entry.get(),
            "PROBA_TYPE": proba_type_entry.get(),
            "RANGE_MIN_TIME": range_min_time_entry.get(),
            "RANGE_MAX_TIME": range_max_time_entry.get(),
            "PROBA_NO_RANGE": proba_no_range_entry.get(),
            "RANGE_MARGE": range_marge_entry.get(),
            "N_POINTS": n_points_entry.get(),
            "NOMBRE_ENTREPOTS": nombre_entrepots_entry.get(),
            "MARGEVITESSEVEHICULE": marge_vitesse_vehicule_entry.get(),
            "MARGETEMPSRETOUR": marge_temps_retour_entry.get(),
            "NOMBRE_ITERATION": nombre_iteration_entry.get(),
            "ALPHA": alpha_entry.get(),
            "BETA": beta_entry.get(),
            "GAMMA": gamma_entry.get(),
            "REGION": region_var.get()
        }

        with open(".\\Projet\\settings.txt", "w", encoding="utf-8") as file:
            for key, value in new_settings.items():
                file.write(f"{key} = {value}\n")
        messagebox.showinfo("Sauvegarde", "Sauvegarde réussie !")

    def load_settings():
        with open(".\\Projet\\settings.txt", "r") as file:
            settings = file.readlines()
            for setting in settings:
                key, value = setting.strip().split(" = ")
                if key in entry_fields:
                    entry_fields[key].delete(0, tk.END)
                    entry_fields[key].insert(tk.END, value)


    # Create a button to save the settings
    save_button = tk.Button(Settings_frame, text="Save", command=save_settings, width=20, height=2, font=(300))
    save_button.place(x=400, y=800)

    # Create a button to load the settings
    load_button = tk.Button(Settings_frame, text="Load", command=load_settings, width=20, height=2, font=(300))
    load_button.place(x=700, y=800)


    # Create entry fields for each setting
    entry_fields = {}

    petit_poids_label = tk.Label(Settings_frame, text="Poids Colis :", font=("Roman", 20) ,foreground="red")
    petit_poids_label.place(x=120, y=100)

    petit_poids_label1 = tk.Label(Settings_frame, text="Petit :", font=(18))
    petit_poids_label1.place(x=120, y=160)
    petit_poids_entry = tk.Entry(Settings_frame, font=(18), width=15)
    petit_poids_entry.place(x=120, y=200)
    entry_fields["COLIS_PETIT_POIDS"] = petit_poids_entry

    moyen_poids_label = tk.Label(Settings_frame, text="Moyen :", font=(18))
    moyen_poids_label.place(x=120, y=240)
    moyen_poids_entry = tk.Entry(Settings_frame, font=(18), width=15)
    moyen_poids_entry.place(x=120, y=280)
    entry_fields["COLIS_MOYEN_POIDS"] = moyen_poids_entry

    grand_poids_label = tk.Label(Settings_frame, text="Grand:" , font=(18))
    grand_poids_label.place(x=120, y=320)
    grand_poids_entry = tk.Entry(Settings_frame, font=(18), width=15)
    grand_poids_entry.place(x=120, y=360)
    entry_fields["COLIS_GRAND_POIDS"] = grand_poids_entry

    except_poids_label = tk.Label(Settings_frame, text="Except :", font=(18))
    except_poids_label.place(x=120, y=400)
    except_poids_entry = tk.Entry(Settings_frame , font=(18), width=15)
    except_poids_entry.place(x=120, y=440)
    entry_fields["COLIS_EXCEPT_POIDS"] = except_poids_entry

    petit_poids_label = tk.Label(Settings_frame, text="Volume Colis :", font=("Roman", 20) ,foreground="red")
    petit_poids_label.place(x=550, y=100)

    petit_volume_label = tk.Label(Settings_frame, text="Petit :", font=(18))
    petit_volume_label.place(x=550, y=160)
    petit_volume_entry = tk.Entry(Settings_frame, font=(18), width=15)
    petit_volume_entry.place(x=550, y=200)
    entry_fields["COLIS_PETIT_VOLUME"] = petit_volume_entry

    moyen_volume_label = tk.Label(Settings_frame, text="Moyen :", font=(18))
    moyen_volume_label.place(x=550, y=240)
    moyen_volume_entry = tk.Entry(Settings_frame, font=(18), width=15)
    moyen_volume_entry.place(x=550, y=280)
    entry_fields["COLIS_MOYEN_VOLUME"] = moyen_volume_entry

    grand_volume_label = tk.Label(Settings_frame, text="Grand :", font=(18))
    grand_volume_label.place(x=550, y=320)
    grand_volume_entry = tk.Entry(Settings_frame, font=(18), width=15)
    grand_volume_entry.place(x=550, y=360)
    entry_fields["COLIS_GRAND_VOLUME"] = grand_volume_entry

    except_volume_label = tk.Label(Settings_frame, text="Except :", font=(18))
    except_volume_label.place(x=550, y=400)
    except_volume_entry = tk.Entry(Settings_frame, font=(18), width=15)
    except_volume_entry.place(x=550, y=440)
    entry_fields["COLIS_EXCEPT_VOLUME"] = except_volume_entry

    petit_poids_label = tk.Label(Settings_frame, text="Probabilites :", font=("Roman", 20) ,foreground="red")
    petit_poids_label.place(x=980, y=100)

    proba_taille_label = tk.Label(Settings_frame, text="Taille :", font=(18))
    proba_taille_label.place(x=980, y=160)
    proba_taille_entry = tk.Entry(Settings_frame, font=(18), width=15)
    proba_taille_entry.place(x=980, y=200)
    entry_fields["PROBA_TAILLE"] = proba_taille_entry

    proba_type_label = tk.Label(Settings_frame, text= "Type :" , font=(18))
    proba_type_label.place(x=980, y=240)
    proba_type_entry = tk.Entry(Settings_frame, font=(18), width=15)
    proba_type_entry.place(x=980, y=280)
    entry_fields["PROBA_TYPE"] = proba_type_entry

    proba_no_range_label = tk.Label(Settings_frame, text="No Range :" , font=(18))
    proba_no_range_label.place(x=980, y=320)
    proba_no_range_entry = tk.Entry(Settings_frame, font=(18), width=15)
    proba_no_range_entry.place(x=980, y=360)
    entry_fields["PROBA_NO_RANGE"] = proba_no_range_entry

    petit_poids_label = tk.Label(Settings_frame, text="Range :", font=("Roman", 20) ,foreground="red")
    petit_poids_label.place(x=120, y=500)

    range_min_time_label = tk.Label(Settings_frame, text="Time Min:" , font=(18))
    range_min_time_label.place(x=120, y=560)
    range_min_time_entry = tk.Entry(Settings_frame, font=(18), width=15)
    range_min_time_entry.place(x=120, y=600)
    entry_fields["RANGE_MIN_TIME"] = range_min_time_entry

    range_max_time_label = tk.Label(Settings_frame, text="Time Max :", font=(18))
    range_max_time_label.place(x=120, y=640)
    range_max_time_entry = tk.Entry(Settings_frame , font=(18), width=15)
    range_max_time_entry.place(x=120, y=680)
    entry_fields["RANGE_MAX_TIME"] = range_max_time_entry

    range_marge_label = tk.Label(Settings_frame, text="Marge :" , font=(18))
    range_marge_label.place(x=120, y=720)
    range_marge_entry = tk.Entry(Settings_frame , font=(18), width=15)
    range_marge_entry.place(x=120, y=760)
    entry_fields["RANGE_MARGE"] = range_marge_entry

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    n_points_label = tk.Label(Settings_frame, text="N Points:", font=(18))
    n_points_label.place(x=400, y=560)
    n_points_entry = tk.Entry(Settings_frame, font=(18), width=15)
    n_points_entry.place(x=400, y=600)
    entry_fields["N_POINTS"] = n_points_entry

    nombre_entrepots_label = tk.Label(Settings_frame, text="Nombre d'entrepots:", font=(18))
    nombre_entrepots_label.place(x=400, y=640)
    nombre_entrepots_entry = tk.Entry(Settings_frame, font=(18), width=15)
    nombre_entrepots_entry.place(x=400, y=680)
    entry_fields["NOMBRE_ENTREPOTS"] = nombre_entrepots_entry

    marge_vitesse_vehicule_label = tk.Label(Settings_frame, text="Marge Vitesse Vehicule:" , font=(18))
    marge_vitesse_vehicule_label.place(x=400, y=720)
    marge_vitesse_vehicule_entry = tk.Entry(Settings_frame, font=(18), width=15)
    marge_vitesse_vehicule_entry.place(x=400, y=760)
    entry_fields["MARGEVITESSEVEHICULE"] = marge_vitesse_vehicule_entry

    marge_temps_retour_label = tk.Label(Settings_frame, text="Marge temps Retour:", font=(18))
    marge_temps_retour_label.place(x=680, y=560)
    marge_temps_retour_entry = tk.Entry(Settings_frame, font=(18), width=15)
    marge_temps_retour_entry.place(x=680, y=600)
    entry_fields["MARGETEMPSRETOUR"] = marge_temps_retour_entry

    nombre_iteration_label = tk.Label(Settings_frame, text="Nombre d'Iterations:", font=(18))
    nombre_iteration_label.place(x=680, y=640)
    nombre_iteration_entry = tk.Entry(Settings_frame, font=(18), width=15)
    nombre_iteration_entry.place(x=680, y=680)
    entry_fields["NOMBRE_ITERATION"] = nombre_iteration_entry

    alpha_label = tk.Label(Settings_frame, text="Alpha :", font=(18))
    alpha_label.place(x=680, y=720)
    alpha_entry = tk.Entry(Settings_frame, font=(18), width=15)
    alpha_entry.place(x=680, y=760)
    entry_fields["ALPHA"] = alpha_entry

    beta_label = tk.Label(Settings_frame, text="Beta:", font=(18))
    beta_label.place(x=960, y=560)
    beta_entry = tk.Entry(Settings_frame, font=(18), width=15)
    beta_entry.place(x=960, y=600)
    entry_fields["BETA"] = beta_entry

    gamma_label = tk.Label(Settings_frame, text="Gamma:", font=(18))
    gamma_label.place(x=960, y=640)
    gamma_entry = tk.Entry(Settings_frame, font=(18), width=15)
    gamma_entry.place(x=960, y=680)
    entry_fields["GAMMA"] = gamma_entry


    # Create a list of departments for the REGION label
    departments = ['Ain', 'Aisne', 'Allier', 'Alpes-de-Haute-Provence', 'Hautes-Alpes', 'Alpes-Maritimes',
                   'Ardèche', 'Ardennes','Ariège', 'Aube', 'Aude', 'Aveyron', 'Bouches-du-Rhône', 'Calvados',
                   'Cantal', 'Charente', 'Charente-Maritime','Cher', 'Corrèze', 'Corse-du-Sud', 'Haute-Corse',
                   "Côte-d'Or", "Côtes-d'Armor", 'Creuse', 'Dordogne','Doubs', 'Drôme', 'Eure', 'Eure-et-Loir',
                   'Finistère', 'Gard', 'Haute-Garonne', 'Gers', 'Gironde', 'Hérault','Ille-et-Vilaine', 'Indre',
                   'Indre-et-Loire', 'Isère', 'Jura', 'Landes', 'Loir-et-Cher', 'Loire', 'Haute-Loire',
                   'Loire-Atlantique', 'Loiret', 'Lot', 'Lot-et-Garonne', 'Lozère', 'Maine-et-Loire',
                   'Manche', 'Marne', 'Haute-Marne','Mayenne', 'Meurthe-et-Moselle', 'Meuse', 'Morbihan',
                   'Moselle', 'Nièvre', 'Nord', 'Oise', 'Orne', 'Pas-de-Calais','Puy-de-Dôme',
                   'Pyrénées-Atlantiques', 'Hautes-Pyrénées', 'Pyrénées-Orientales', 'Bas-Rhin',
                   'Haut-Rhin','Rhône', 'Haute-Saône', 'Saône-et-Loire', 'Sarthe', 'Savoie',
                   'Haute-Savoie', 'Paris', 'Seine-Maritime','Seine-et-Marne', 'Yvelines', 'Deux-Sèvres',
                   'Somme', 'Tarn', 'Tarn-et-Garonne', 'Var', 'Vaucluse', 'Vendée','Vienne', 'Haute-Vienne',
                   'Vosges', 'Yonne', 'Territoire de Belfort', 'Essonne', 'Hauts-de-Seine',
                   'Seine-Saint-Denis', 'Val-de-Marne', "Val-d'Oise"]

    # Create a StringVar to store the selected department
    region_var = StringVar(Settings_frame)
    region_var.set(departments[0])  # Set the default department

    # Create the label and dropdown menu for the REGION setting
    region_label = tk.Label(Settings_frame, text="Region:", font=(18))
    region_label.place(x=960, y=720)
    region_option_menu = OptionMenu(Settings_frame, region_var, *departments)
    region_option_menu.config(width=12, font=(18))
    region_option_menu.place(x=960, y=760)

    entry_fields["REGION"] = region_option_menu

    Settings_frame.pack(fill=tk.BOTH, expand=True)

def hide_frames():
    for widget in main_frame.winfo_children():
        widget.destroy()





#Indicate fonction
def hide_indicators():
    home_indicate.config(bg="gray")
    Graphs_indicate.config(bg="gray")
    About_indicate.config(bg="gray")
    Settings_indicate.config(bg="gray")
    Journey_indicate.config(bg="gray")


def indicate(lb, page):
    hide_indicators()
    lb.config(bg="black")
    hide_frames()
    page()





options_frame = tk.Frame(root, bg="gray")

#Home Button
home_btn = tk.Button(options_frame, text="Home",font=('Bold',15) , fg="White", bd=0 ,bg="gray",
                    command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=70, width=130, height=50)

#Home Indicator
home_indicate = tk.Label(options_frame, text="",bg="gray")
home_indicate.place(x=3, y=70, width=5, height=50)

#Delivery Button
Graphs_btn = tk.Button(options_frame, text="Delivery",font=('Bold',15) , fg="White", bd=0 ,bg="gray",
                    command=lambda: indicate(Graphs_indicate, Graphs_page))
Graphs_btn.place(x=10, y=170, width=130, height=50)

#Delivery Indicator
Graphs_indicate = tk.Label(options_frame, text="",bg="gray")
Graphs_indicate.place(x=3, y=170, width=5, height=50)

#journey Button
Graphs_btn = tk.Button(options_frame, text="Journey",font=('Bold',15) , fg="White", bd=0 ,bg="gray",
                    command=lambda: indicate(Journey_indicate, Journey_page))
Graphs_btn.place(x=10, y=270, width=130, height=50)

#Journey Indicator
Journey_indicate = tk.Label(options_frame, text="",bg="gray")
Journey_indicate.place(x=3, y=270, width=5, height=50)

#About Us Button
About_btn = tk.Button(options_frame, text="About Us",font=('Bold',15) , fg="White", bd=0 ,bg="gray",
                    command=lambda: indicate(About_indicate, About_page))
About_btn.place(x=10, y=370, width=130, height=50)

#About Indicator
About_indicate = tk.Label(options_frame, text="",bg="gray")
About_indicate.place(x=3, y=370, width=5, height=50)

#Settings Button
Settings_btn = tk.Button(options_frame, text="Settings",font=('Bold',15) , fg="White", bd=0 ,bg="gray",
                        command=lambda: indicate(Settings_indicate, Settings_page))
Settings_btn.place(x=10, y=470, width=130, height=50)

#Settings Indicator
Settings_indicate = tk.Label(options_frame, text="",bg="gray")
Settings_indicate.place(x=3, y=470, width=5, height=50)


options_frame.pack(side=tk.LEFT, fill=tk.Y)
options_frame.pack_propagate(False)
options_frame.configure(width =150, height=550)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width =1600, height=950)


home_page()
root.mainloop()
