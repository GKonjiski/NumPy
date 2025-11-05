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



