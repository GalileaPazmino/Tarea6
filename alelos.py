#! /bin/bash
import scipy # for random numbers

def build_population(N, p):
    """ cada cromosoma tiene un alelo y N es el numero de individuos
    """
   #En esta funcion se estan creando tuplas con la lista de los alelos A y a segun el numero de individuos
    population = []
    for i in range(N):   #se crea un bucle for aleatorio con las variables a y A, para ir agregando alelos aleatorios 
                         #al final de cada alelo a o A en build population
        allele1 = "A"    
        if scipy.random.rand() > p: #la probabilidad de tener alelos a y A debe ser mayor a 0.43
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

build_population(N = 25, p = 0.43) #para 25 indiviuos con probalidad de 0.43, devolver la poblacion con alelos Aay aA al azar

# FUNCIÓN 2. Conteo de pares de alelos
def compute_frequencies(population):
    #Cuenta los genotipos y devuelve un diccionario de frecuencias genotípicas segun los alelos que haya
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA}) # forma el diccionario
my_pop = build_population(500, 0.21)
fmy_pop = compute_frequencies(my_pop) #ver las frecuencias de los alelos aleatorios creados en la funcion 1
print(fmy_pop)
print((500-fmy_pop["aa"])/500) #ver la cantidad de aa en una poblacion de 500

# FUNCIÓN 3. Creación de nueva población

def reproduce_population(population):
    #Para cada N producir una nueva generacion al azar
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N) #recibe cromosoma de papa
        mom = scipy.random.randint(N) #recibe cromosa de mama
        #ver que cromosoma viene de mama
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom]) #ver la descendencia entre mama y papa
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring) #ir creando las nuevas generaciones al final de cada cromosoma
    return new_generation
print(compute_frequencies(my_pop))
new_pop = reproduce_population(my_pop) #ver la nueva reproduccion en cada indiviudo, segun los alelos generados de mama y papa
new_pop2 = reproduce_population(new_pop)
print(compute_frequencies(new_pop))
print(compute_frequencies(new_pop2))
