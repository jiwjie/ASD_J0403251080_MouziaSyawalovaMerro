#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 12 - Graph II : Shortest Path
#================================================

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 

# Representasi weighted graph menggunakan dictionary bersarang 

graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] 
jalur_2 = graph['A']['C'] + graph['C']['D'] 

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 
  # A -> B -> D 
  # A -> C -> D 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")


# Pertanyaan analisis
'''
1. Berapa total bobot jalur A -> B -> D?
    > A -> B = 4
      B -> D = 5
    Total = 4 + 5 = 9

2. Berapa total bobot jalur A -> C -> D? 
    > A -> C = 2
      C -> D = 1
      Total = 2 + 1 = 3
      
3. Jalur mana yang dipilih sebagai jalur terpendek? 
    > A -> C -> D
    
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang 
paling sedikit? 
    > Pada Weighted Graph, tiap edge memiliki nilai masing-masing. Walaupun 
    kedua jalur memiliki jumlah edge sama-sama 2, namun akumulasi dari tiap jalur
    itu yang membedakan dan menentukan jalur terpendek.
'''
