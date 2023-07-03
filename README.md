# Projet : ADEME

Le projet à pour but l'optimisation de tournées de livraison, l'idée étant d'avoir le minimum de camions et de temps/distance de trajet.

Le projet à pour portée la france métropolitaine.

## Contraintes

### Version de base 

- Le choix du modèle et le code en Python capable de résoudre des instances de taille importante (plusieurs milliers de villes)
- Une étude statistique du comportement expérimental de l'algorithme

 

### Contraintes supplémentaires

Voici une liste (non exhaustive) de contraintes qui pourraient être intégrées au périmètre de votre étude. Pour certaines, des versions avancées sont aussi proposées. L’implémentation d’une contrainte et de l’une de ses versions avancées vaut l’implémentation de deux contraintes.

- Fenêtre de temps de livraison pour chaque objet

- Interdiction de livrer hors de la fenêtre

- Possibilité d'attendre sur place l'ouverture de la fenêtre temporelle

- k camions disponibles simultanément pour effectuer les livraisons. Le calcul de la tournée devra inclure l’affectation des objets (et donc des points de livraison) aux différents camions disponibles, et minimiser non plus le temps total, mais la date de retour du dernier camion à la base.

- Capacité des camions (2 ou 3 dimensions) et encombrement des objets

- Certains objets ne peuvent être livrés que par certains camions

- Chaque objet a un point de collecte spécifique // Probablement pas faite dans notre version

- Le temps de parcours d’une arête varie au cours du temps (ce qui revient à faire varier sa longueur), pour représenter la variation du trafic

 
### Types de contraintes
Ces contraintes peuvent être réparties en deux catégories :

Les contraintes ne modifiant pas l’espace des solutions, uniquement leurs valeurs. Par exemple, la prise en compte de fenêtres de temps avec attente (si le camion est en avance). Dans le cas d’une méthode à voisinage, les voisins d’une solution ne seront pas modifiés par l’intégration de cette contrainte, seuls les coûts seront différents

Les contraintes modifiant l’espace des solutions. Par exemple, certains objets nécessitant un camion d’un type précis pour être livrés. Ajouter cette contrainte va rendre certaines solutions invalides, et donc restreindre l’espace de solutions.

D'autres contraintes peuvent être traitées, si c'est justifié par une application industrielle (pas forcément issu du contexte actuel).

## Phases

### Phase 0 : Données à obtenir/générer

Le graphe de la france, c'est à dire les routes et intersections, est disponible via OSMNX .

On fixe 1 warehouse par region.
On simule les livraisons et leur fenetres de temps de manière réaliste, on prend donc en compte la densité de population.
/!\ Une warehouse ne peut livrer que dans sa region.

### Phase 1 : TSP (Fourmi) + (Dijkstra)

#### Partie algorimique

L'algothrime des fourmi va repondre aux problématique de fenetre de temps et d'optimisation de la route à prendre.

Dijkstra va lui permettre d'obtenir la plus courte distance pour effectuer le trajet d'un noeux à un autre

Note : on souhaite que les véhicule spéciaux, réfrigéré par exemple, ne puisse que livrer uniquement les livraisons où un véhicule spécial est nécéssaire.

#### Partie pratique
On cherche à optimiser le nombre de livraisons faite par un véhicule avant qu'il rentre à la warehouse.

L'algorithme va donc, pour chaque warehouse et types de colis, utiliser TSP (Fourmi) afin de trouver les meilleurs chemins qui respectent nos contraintes.

On obtiendra donc en `output`, une liste des meilleurs circuits pour chaque warehouse.

### Phase 2 : Attribution des véhicules

On considère que CesiCDP possède suffisament de véhicules pour toutes les situations.

On cherche donc à attribuer des véhicule pertinent pour chaque circuit de livraison, il existe plusieurs critères pertinent comme :

- L'empreinte carbone
- Le stockage
- Le cout

// A completer après nos recherches.



















