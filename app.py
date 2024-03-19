import random

markusLoves = ["python", "Bread", "Cake", "Water", "Cats", "Dogs"]

def lovesMore(ele):
    print("Markus loves Java more than " + ele + ".")

for _ in range(len(markusLoves)):
    lovesMore(random.choice(markusLoves))
  
