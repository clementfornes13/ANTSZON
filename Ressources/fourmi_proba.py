import multiprocessing as mp
import sys

# Création de la queue pour stocker les résultats
resultat_queue = mp.Queue()

if __name__ == "__main__":
    var1 = int(sys.argv[1])
    var2 = sys.argv[2]
    def distance_euclidienne(A,B):
        # On calcule la distance euclidienne entre deux points
        return ((A[0]-B[0])**2+(A[1]-B[1])**2)**(1/2)

    def fourmi_proba_process(i,resultat_queue,Graph,Pheromone,PositionFourmis,SeenFourmis,alpha=1,beta=1) :
        # On filtre le cas ou la fourmi doit rejoindre son noeud d'origine
        Last = True
        for value in SeenFourmis[i] :
            if value is False :
                Last = False
        if Last :
            # On renvoie le signal qu'une fourmi doit revenir à son point de départ
            return ["F"]*len(PositionFourmis)
        Result_temp = []
        Distances_temp = []
        # On la calculer pour chaque fourmis les probabilités d'aller à chaque noeud
        # Coordonnées de la fourmis
        CoordsFourmis = Graph[PositionFourmis[i]]
        for j in range(len(Graph)) :
            # j est le noeud de destination
            # On veux pas que la fourmis reste sur place ni qu'elle aille sur un noeud qu'elle a déjà vu
            if j is not PositionFourmis[i] and SeenFourmis[i][j] is False:
                Result_temp.append([PositionFourmis[i],j,(Pheromone[PositionFourmis[i]][j])**(beta)/(distance_euclidienne(CoordsFourmis,Graph[j]))**(alpha)])
                Distances_temp.append((Pheromone[PositionFourmis[i]][j])**(beta)/(distance_euclidienne(CoordsFourmis,Graph[j]))**(alpha))
            else :
                Result_temp.append((PositionFourmis[i], j, None))
                Distances_temp.append(None)
        # On return tout au thread principal
        resultat_queue.put(Result_temp,Distances_temp)

    def fourmis_proba_main(Graph,Pheromone,PositionFourmis,SeenFourmis,alpha=1,beta=1) : #Trustable
        Result = []
        # /!\ On met dans Distances et Distances_temps les distances inverses multiplié par les phéromones
        Distances = []
        processes = []
        for i in range(len(PositionFourmis)):
            process = mp.Process(target=fourmi_proba_process, args=(i,resultat_queue,Graph,Pheromone,PositionFourmis,SeenFourmis,alpha,beta))
            process.start()
            processes.append(process)
        for process in processes:
            process.join()
        # On récupère les résultats
        for i in range(len(PositionFourmis)) :
            Result_temp,Distances_temp = resultat_queue.get()
            Result.append(Result_temp)
            # On calcul la distance totale pour normaliser les probabilités (on prend pas en compte les None)
            Distances.append(sum([element for element in Distances_temp if element is not None]))

        # On normalise les probabilités
        for i in range(len(Result)) :
            for j in range(len(Result[i])) :
                if Result[i][j][2] is not None :
                    # On normalise les probabilités
                    Result[i][j][2] = (Result[i][j][2]/Distances[i])
        return Result
