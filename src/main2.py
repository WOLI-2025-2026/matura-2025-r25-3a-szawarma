import math

plik_wejscia="/workspaces/matura-2025-r25-3a-szawarma/zalaczniki-2025/dron.txt"
plik_wyjscia="/workspaces/matura-2025-r25-3a-szawarma/src/wyniki3.txt"

def nwd(a,b):
    return math.gcd(abs(a), abs(b))

def zad3_1(plik_wejscia, plik_wyjscia):
    licznik_par = 0
    with open(plik_wejscia, 'r') as wejscie:
        for linia in wejscie:
            A, B = map(int, linia.split())
            if nwd(A,B) > 1:
                licznik_par += 1

    with open(plik_wyjscia, 'w') as f:
        f.write(f"3.1 {licznik_par}\n")

def zad3_2():
    P = [(0, 0)]
    x, y = 0, 0
    
    with open(plik_wejscia, 'r') as w:
        for l in w:
            try:
                A, B = map(int, l.split())
                x += A
                y += B
                P.append((x, y))
            except: pass
    licznik = 0
    for px, py in P:
        if 0 < px < 5000 and 0 < py < 5000:
            licznik += 1
            
    T = ""
    N = len(P)
    
    for k in range(N):
        for i in range(N):
            if i == k: continue
            for j in range(i + 1, N): 
                if j == k: continue
                
                xk, yk = P[k]
                xi, yi = P[i]
                xj, yj = P[j]
                
                if 2 * xk == xi + xj and 2 * yk == yi + yj:
                    T = (P[k], P[i], P[j])
                    break
            if T: break
        if T: break
        
    with open(plik_wyjscia, 'w') as z:
        z.write(f"3.2a {licznik}\n")
        
        if T:
            S, A, B = T
            z.write(f"3.2b ({S[0]}, {S[1]}), ({A[0]}, {A[1]}), ({B[0]}, {B[1]})\n")
        else:
            z.write("3.2b Nie istnieje\n")


if __name__ == "__main__":
    zad3_2()