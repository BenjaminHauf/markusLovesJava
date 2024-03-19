import random

markusLoves = ["python", "Bread", "Cake", "Water", "Cats", "Dogs"]

def lovesMore(ele):
    #print("Markus loves Java more than " + ele + ".")
    with open("README.md", "a") as file:
        file.write("Markus loves Java more than " + ele + ".\n")

for _ in range(len(markusLoves)):
    lovesMore(random.choice(markusLoves))
  
