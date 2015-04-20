# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:32:39 2015

@author: Carlos
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from dados_do_usuario import UserDayCaloriesWeek
from dados_do_usuario import UserDayProteinsWeek
from dados_do_usuario import UserDayCarboidratesWeek
from dados_do_usuario import UserDayFatWeek
from Funcoes import CalculaTMBmultAF
from Funcoes import CalculaSumUserDayCaloriesWeek


categoria = ('Calorias consumidas','calorias recomendadas',)
y_pos = np.arange(len(categoria))
quantidade = [CalculaSumUserDayCaloriesWeek(),CalculaTMBmultAF()]
plt.barh(y_pos, quantidade, align='center', alpha=0.4)
plt.yticks(y_pos, categoria)
plt.xlabel('Quantidade (calorias)')
plt.title('Quantidade diaria recomendada vs consumida')
plt.show()

'''
print("Lista de keys UserDayCaloriesWeek: ",list(UserDayCaloriesWeek.keys()))
print("UserDayCaloriesWeek: ",UserDayCaloriesWeek.values())
print("Lista de keys UserDayProteinWeek: ",list(UserDayProteinsWeek.keys()))
print("UserDayProteinWeek: ",UserDayProteinsWeek.values())
'''

num_days_cal = len(list(UserDayCaloriesWeek.keys()))
num_days_protein = len(list(UserDayProteinsWeek.keys()))
num_days_carboidrates = len(list(UserDayCarboidratesWeek.values()))
num_days_fat=len(list(UserDayFatWeek.values()))


days=list(UserDayCaloriesWeek.keys())
days.sort()

calories_values=[]
for d in days:
    calories_values.append(UserDayCaloriesWeek[d])
print(UserDayCaloriesWeek)
print("UserDayCaloriesWeek",days)
print("UserDayCaloriesWeek",calories_values)

plt.plot(list(range(num_days_cal)),calories_values)
plt.xlabel("Dias da semana")
plt.ylabel("Calories")
plt.title("Quantidade de Calorias ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()


proteins_values=[]
for d in days:
    proteins_values.append(UserDayProteinsWeek[d])
print("UserDayProteinsWeek",UserDayProteinsWeek)
print("UserDayProteinsWeek",days)
print("UserDayProteinsWeek",proteins_values)

plt.plot(list(range(num_days_protein)),proteins_values)
plt.xlabel("Dias da semana")
plt.ylabel("Proteinas")
plt.title("Quantidade de proteinas ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()


carboidrates_values=[]
for d in days:
    carboidrates_values.append(UserDayCarboidratesWeek[d])
print("UserDayCarboidratesWeek",UserDayCarboidratesWeek)
print("UserDayCarboidratesWeek",days)
print("UserDayCarboidratesWeek",carboidrates_values)


plt.plot(list(range(num_days_carboidrates)),carboidrates_values)
plt.xlabel("Dias da semana")
plt.ylabel("Carboidratos")
plt.title("Quantidade de carboidratos ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()


fat_values=[]
for d in days:
    fat_values.append(UserDayFatWeek[d])
print("UserDayFatWeek",UserDayFatWeek)
print("UserDayFatWeek",days)
print("UserDayFatWeek",fat_values)

plt.plot(list(range(num_days_fat)),fat_values)
plt.xlabel("Dias da semana")
plt.ylabel("Gordura")
plt.title("Quantidade de gordura ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()

#label=["Segunda","Terca","Quarta","Quinta","Sexta","Sabado","Domingo"]
plt.plot(list(range(num_days_cal)),calories_values,list(range(num_days_protein)),proteins_values,list(range(num_days_carboidrates)),carboidrates_values,list(range(num_days_fat)),fat_values)
plt.xlabel("Dias da semana")
plt.ylabel("Calories, Proteinas, Carboidratos e Gordura")
plt.title("Quantidade ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()