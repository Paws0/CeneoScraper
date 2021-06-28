from matplotlib import pyplot as plt
from os import listdir 
import pandas as pd 
import numpy as np 
from pandas._config.config import options

pd.set_option("display.max_columns", None)

def transform_stars(stars):
    return float(stars.split("/")[0].replace(","),".") 

print(*[file_name.split(".")[0] for file_name in listdir("opinions")], sep='\n')

product_id = input("Podaj kod produktu: ")  

opinions = pd.read_json("opinions/{}.json".format(product_id))

opinions_count = opinions.opinion_id.count()    
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()
average_score = opinions.stars.mean().round(2)

stars = opinions.stars.value_counts().reindex(np.arange(0,5.001,0.5), fill_value=0)

stars.plot.bar(color="lightsteelblue")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiaztek")
plt.ylabel("Liczba opinii")
plt.savefig("plots/{}.bar.png".format(product_id))
plt.close()

recomm = opinions.recomm.value_counts(dropna=False).reindex([False,True,float("Nan")], fill_value=0)
print(recomm)
plt.title('Opinie w procentach')
plt.labels=recomm
plt.gcf()
#explode=(0,0,0.03)
mylabels = [ "Nie Polecam", "Polecam", "Brak Opinii" ]
#labels = 
recomm.plot.pie( 
                 autopct=lambda p: '{:1.0f}%'.format(round(p)) if p > 0 else '',

                 pctdistance=1.1, labeldistance=1.2,
                 startangle = 315, #explode=explode,
                 labels=mylabels,
                 rotatelabels=True,
                 colors=['coral','powderblue','black'],
)

 
Circle=plt.Circle(xy=(0,0), radius=0.75, facecolor='white')
plt.gca().add_artist(Circle)
plt.ylabel('')
plt.savefig("plots/{}.pie.png".format(product_id)) 
plt.close()