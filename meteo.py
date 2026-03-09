import requests
import matplotlib.pyplot as plt


villes = ["Paris", "Tokyo", "New York", "Dakar"]

temperatures = []
humidites = []


for ville in villes:
    url = f"https://wttr.in/{ville}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = int(data["current_condition"][0]["temp_C"])
        humidite = int(data["current_condition"][0]["humidity"])

        temperatures.append(temp)
        humidites.append(humidite)


plt.subplot(1,2,1)
plt.bar(villes, temperatures)
plt.title("Comparaison des températures")
plt.xlabel("Villes")
plt.ylabel("Température °C")



plt.subplot(1,2,2)
plt.pie(humidites, labels=villes, autopct="%1.1f%%")
plt.title("Répartition de l'humidité")
plt.show()



import csv

with open("meteo_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

   
    writer.writerow(["Ville", "Température (°C)", "Humidité (%)"])

  
    for i in range(len(villes)):
        writer.writerow([villes[i], temperatures[i], humidites[i]])

print("Rapport météo enregistré dans meteo_report.csv")