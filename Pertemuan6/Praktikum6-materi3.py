#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Merge Sort  (Ascending)
#================================================================

def merge_sort(data):
    
    if len(data) <= 1:
        return data

    # Divide : membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid]   # slicing bagian kiri
    right = data[mid:]  # slicing bagian kanan
    
    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
        
    return merge(left_sorted, right_sorted)

def merge(left,right):
        
    result = []
    i = 0
    j = 0 
    
    # Membandingkan elemen kiri dan kanan 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
            
    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[:i])
    
    return result

angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting : ", merge_sort(angka))
        
        
    
    
''' # 8 ==> left 4   right 4
        # left 4 ==> mergesort ==>
        #       left 2 ==> mergesort ==>
        # dan right 2 ==> mergesort '''