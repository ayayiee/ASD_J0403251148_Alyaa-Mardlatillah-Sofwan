# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Materi 1 Rekursif: Faktorial
# Recursive case => 3! = 3 x 2 x 1
# Base case => 0 berhenti
# ===================================================================

def faktorial(n):              # Fungsi rekursif untuk menghitung nilai faktorial 

    # Base case
    if n == 0:                 # Jika n = 0, maka hasil faktorial 1
        return 1
    
    # Recursive case
    return n * faktorial(n-1)  # n-1 * n-2 * n-3 * ...... n-?

print("===== Program Faktorial =====")
print("Hasil Faktorial: ", faktorial(3))    #Menghitung 3! = 3x2x1 = 6








































































