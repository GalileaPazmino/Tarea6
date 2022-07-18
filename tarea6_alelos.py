#!/usr/bin/env python
# coding: utf-8

# <img src="https://www.ikiam.edu.ec/img/logo-ikiam-grey.png" width=400 height=300 />

# ### <center><h2> INGENIERÍA EN BIOTECNOLOGÍA</h2></center>

# # <center><h1 style="color:purple">GBI6 - BIOINFORMÁTICA</h1></center>

# - **Estudiante:** Galilea Pazmiño
# - **Edad:** 22
# - **Domicilio:** Napo-Tena
# - **Nacionalidad:** Ecuatoriana
# - **Correo:** galilea.pazmino@est.ikiam.edu.ec
# - **Fecha:** 15/07/2022

# En este trabajo, se produciran nuevas generaciones a partir de la formacion aleatoria de alelos provenientes de mama y papa, codificadas a travez de funciones que han sido importadas desde modulos creados externamente para clasificar de forma ordenada y dinamica el proceso de informacion.

# In[344]:


import alelos


# In[368]:


alelos.build_population(25, 0.43)


# In[369]:


nuevo=alelos.build_population(10, 0.35)
print(nuevo)


# In[560]:


conteoalelo = alelos.compute_frequencies(nuevo)
print(conteoalelo)


# In[561]:


crecimiento = alelos.reproduce_population(nuevo)
print(crecimiento)


# In[566]:


conteoalelo2 = alelos.compute_frequencies(crecimiento)
print(conteoalelo2)


# In[590]:


def simulate_drift(N, p):
    # initialize the population
    my_pop = alelos.build_population(N, p)
    fixation = False # condiciòn incial de fijacion
    num_generations = 0 # población parental
    while fixation == False:
        # compute genotype counts
        genotype_counts = alelos.compute_frequencies(my_pop)
        # if one allele went to fixation, end
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N):
            print("An allele reached fixation at generation", num_generations)
            print("The genotype counts are")
            print(genotype_counts)
            fixation == True
            break
        # if not, reproduce
        my_pop = alelos.reproduce_population(my_pop)
        num_generations += 1
    return num_generations, genotype_counts


# In[603]:


sim1 = simulate_drift(100, 0.5 ) #simulacion de generacion
sim1


# In[551]:


Generacion100= alelos.build_population(100,0.5) #genero 100 individuos con una probabilidad de 50% 
print(Generacion100) # ver generacion 100
Conteo= alelos.compute_frequencies(Generacion100) # contar el numero de alelos en generacion 100
print(Conteo) #imprimo este conteo
len(Generacion100) # para saber el numero de individuos que tengo en la generacion


# En la generacion 100, se obtuviero diferentes resultados en el conteo de alelos, siendo AA el mas bajo y  Aa el mas alto, en la cual existen 100 individuos.
