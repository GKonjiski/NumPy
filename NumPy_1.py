import numpy as np

print(np.__version__)



#NUMPY ARRAY
#so bolša verzija python list
#odspodaj so primeri python lčista in numpay arraya, kaj ze zgodi, če ju množiš z 2
my_list=[1,2,3,4,]

my_list=my_list*2
print(my_list)

array=np.array([1,2,3,4])

array=array*2
print(array)

#MULTIDIMENZIONALNI ARRAYI

#0 DIMENZIJA ARRAY
multi_array_0=np.array("A")

#1 DIMENZIJA ARRAY
multi_array_1=np.array(["A","B","C"])

#2 DIMENZIJA ARRAY (MATRICA)
multi_array_2=np.array([["A","B","C"],
                        ["Č","D","E"],
                        ["F","G","H"]])

#3 DIMENZIJA ARRAY
#v dimenzijah arraya more bit znotraj seznamov(listov) vedno enako število elementov
multi_array_3=np.array([[["A","B","C"], ["Č","D","E"], ["F","G","H"]],
                        [["I","J","K"], ["L","M","N"], ["O","P","R"]],
                        [["S","Š","T"], ["U","V","Z"], ["Ž"," ","-"]]])


#OBLIKA ARRAYA
print(multi_array_3.shape) #(3, 3, 3)=>3 plasti, 3 vrste, 3 stolpci (ni treba da so tri plati, lohk sta sam 2)

#normalen python za izkanje elemta
print(multi_array_3 [1][1][1])

#numpy iskanje elemnta
print(multi_array_3[1,1,1]) #=>M

print(multi_array_3[2,0,1])


#SLICING

slicing_array=np.array([[1 ,2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16]])

#array[start:end:step]  (subscript operator[])
print(slicing_array[1]) #=> [5, 6, 7, 8]

print(slicing_array[0:3]) #=>[1 ,2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12] (3 ker se piše eno prej in ne vklučuje napisane) 
#[1:] pomeni od 1 do konca

print(slicing_array[0:4:2]) #=>[1 ,2, 3, 4], [9, 10, 11, 12] (vsaka druga začebjši z prvo)

#da zbiraš po naslednji ravni(vrstice, stolpci(elemnti).. ločiš v[] z ,  To pomeni prvo zbereš vrstico (list) in nato elemnt v nejm)
print(slicing_array[:, 2]) #=>to pomeni vse vrstice tretji stolpec (elenet) torej [ 3  7 11 15]

print(slicing_array[:, 0:3]) #=>od prvega do 3jega stolpca

print(slicing_array[0:2, 0:2]) #=> [[1 2]
                                   #[5 6]]


# SCALAR ARITHMETIC (ena številka)

scalar_array=np.array([1, 2, 3])

print(scalar_array+1) #=>[2 3 4] isto za vse ostale matematične operacije

#VEKTORIZIRANE MATEMATIČNE FUNKCIJE 

print(np.sqrt(scalar_array)) #=>[1.         1.41421356 1.73205081]


#ELEMENT-WISE ARITHMETICS

scalar_array1=np.array([4, 5, 6])

print(scalar_array + scalar_array1) #=>[5 7 9] isto za vse ostale matematične operacije


#OPERATORJI ZA PRIMERJANEJ

com_array= np.array([91, 55, 100, 73, 82, 64])

print(com_array == 100) #=>[False False  True False False False]
print(com_array >= 70)  #=>[ True False  True  True  True False]

com_array[com_array < 60] =0 
print(com_array)    #=>[ 91   0 100  73  82  64]


#BROADCASTING
#Z bradcatingom lahko operiaraš na arrayih z različnimi oblikami (shapes), 
# numpy bo virtualno razširu dimenzije da se manjši shape jumejo z velikostjo večjega arraya.

#PRAVILA za primerjanje
#Dimenzije se ujemajo ali pa je ena dimenzija velika 1 (JE LOGIČNO SAM MAL RABŠ POMISLT :)  )

brod_array1= np.array([[1, 2, 3, 4]])

brod_array2= np.array([[1], [2], [3], [4]])

print(brod_array1.shape) #=>(1, 4)    STA PRIMERLJIVA KER IMA VSAJ EN DIMENZIJO 1
print(brod_array2.shape) #=>(4, 1)    če bi bilo pa (2, 4) ali (1,4) pa primarjava ne bi mogoča
                                          #         (4, 1) ali (4,2)


print((brod_array1 * brod_array2)) #=>[[ 1  2  3  4]
                                   #   [ 2  4  6  8]
                                   #   [ 3  6  9 12]
                                   #   [ 4  8 12 16]]


#AGREGATNE FUNKCIJE
#Povzemajo podatke in vrnejo samo vrednost

agr_array=np.array([[1, 2, 3, 4],
                    [6, 7, 8, 9]])

print(np.sum(agr_array))     #=> 40 (seštevek)
print(np.mean(agr_array))    #=> 5.0 (povprečna vrednost)
print(np.std(agr_array))     #=> 2.7386  (standardna divijacija) (lahk tudi varijacije(var))
print(np.max(agr_array))     #=> 9  isto tudi za min
print(np.argmax(agr_array))  #=> 7   pozicija (index) max vrednosti

print(np.sum(agr_array, axis=0)) #=> [ 7  9 11 13] axis pomeni da se v tem primeru seštejejo vsi stolpci (elemti z istim indexom v listih znotraj glavnega arraya )
print(np.sum(agr_array, axis=1)) #=> [10 30] v tem primeru se seštejejo elemnti v listih
# axis=0 sešteva verticalno. axis=1 sešteva horizontalno. Tle rabš gledat kot matrico. axis=2 če maš še layerje


#FILTRIRANJE
filter_array = np.array([[15, 14, 16, 17, 34, 23, 60],
                        [14, 15, 17, 11, 26, 27, 80]])

filter_array1 = filter_array[filter_array<20]

print(filter_array1) #=> [15 14 16 17 14 15 17 11]   ( operator "and" je v numpy &, "or" je pa |,  ker je numpy napisan v C)

filter_array3=np.where(filter_array >= 18, filter_array, 0) #če hočeš določene vrednosti zamenjati (pogoj, target, nova vrednost)

print(filter_array3) #=> [[ 0  0  0  0 34 23 60]
                     #    [ 0  0  0  0 26 27 80]]


#da se tut generirat random numbers