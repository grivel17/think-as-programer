# plik zawiera rozwiązania zadań z podręcznika "Jak myśli programista"

# ZD.1.  

# wydrukuj dokładną połówkę kwadrata 
# pierwszy krok wydrukuj linię
# wydrukuj kwadrat 
# niech w kazdej linii ubywa 1 gwiazdka 

# def draw_half_square(n):
#         for x in range(n):
#                 print("* " * (n - x))

# ZD.2 
# wydrukuj dwa trójkąty i niech stykają się bokami 
# co mozna zrobić? - uzyc analogii do zd 1 
# dodać do analogii warunkowanie ze po połowie odwracamy 
# zadanie jest w wariancie uproszczonym przyjmujemy, ze n jest nieparzyste
# dla liczb parzystych wystarczy dodać jeszcze 1 warunek 


# def draw_two_triangles(n):
#         for x in range(n):
#                 if x <= n / 2: 
#                         print("* " * (x+1))
#                 else:
#                         print("* " * (n-x))
# draw_two_triangles(15)

# ZD.Algorytm luna sprawdź czy podany ciąg z liczbą dodaną jest prawidłowy 

# podsumuj to sobie w łózku - miałem plan rozbiłem problem na mniejsze, ze dopiero posiadanie zdefinowanych elementow pozwala przejsc dalej (zacznij od najprostszego najtrudniejszego najbardziej interesujacego )  

#  Jak to działa step by step?
# 1762483 numer ostatnia cyfra jest tą dodaną
# co druga cyfra *2 (od lewej)
# jeśli większe od 9 to dodaj do siebie cyfry liczby 
# suma wszystkich czy dzieli się bez reszty przez 10 
# warunek dowolny ciąg liczb musi przyjąć 
# ROZBIJ NA MAŁE ZADANIA 
# 1 + 5/ + 6 + 4/ + 4 + 7/ + 3
# 1. potrzebuję funkcję przyjmującą input 
# 2. zamień string na listę (potem mozna to zrefaktorować)
# 3. utnij ostatnią liczbę i zapisz ją do zmiennej 
# 4. pomnóz co drugą przez dwa 
# 5. sprawdz czy nie większa od 9 jeśli tak dodaj elementy 

# przetwarzam go na listę jest uporządkowana posiada indeksy mozna ją iterować - SPRÓBUJ KROKI W RANGE 
# MODUŁ INPUT: 
# to_control = int(input("Wprowadź liczbę do kontroli: "))
# print(to_control)

# L = [1,7,6,2,4,8,3]

# for i in range(1,len(L), 2):
#         print(L[i])

#! jeśli uzyje modulo 10 podwojonej liczby (to usune dziesiętność i zawsze zostanie druga wtedy wystarczy dodac )
#! sprawdź które rozwiązanie jest bardziej optymalne z punktuy widzenia czasu

# x = 1762484  

# def check_luhnas_algorythm(x):
#         x = str(x)

#         lx = [int(i) for i in x] 

#         for i in range(1, len(lx) - 1, 2):
#                 lx[i] = lx[i]*2
#                 if lx[i] > 9: 
#                         lx[i] = str(lx[i])
#                         lx[i] = int(lx[i][0]) + int(lx[i][1]) 

#         if sum(lx) % 10 == 0:
#                 print("Yupi podałeś dobry kod")

#         else: 
#                 print("Błąd. Sprobuj ponownie...") 

#ZD 3.  Śledzenie stanu - problem: dekodowanie wiadomości A. jakich umiejętności nam trzeba albo 
# B. albo jakich elementów potrzeba 
# 1. pobranie liczby (mozna uzyc listy )
# 2. dekodowanie po przez dzielenie i wybór odpowiedniej litery z alfabetu 
#       2a. uzyj dodatkowej listy z alfabetem oraz listy znaków interpunkcyjnych 
# 3. zbudowanie trzech trybów dekodowania - zbudować do obsługi trzy oddzielne funkcje 
# 4. jak w klasie js mozna wprowadzić zmienną która będzie przechowywała aktualny stan 
# 5. listę output 
# 6. i finalny output 
# 

lista_liczb = [313, 12312, 906, 3337, 2529, 568, 1994, 689, 14994, 221, 216, 11, 600, 18, 11684, 0, 136, 1496, 27, 10]

lista_liter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r", "s", "t","u","v" "x", "w", "y", "z"]

lista_znakow = ["!", "?", ",", "."," ",";", "'",'"']


litery = []

control = 0

def zwroc_wielka_litere(numer_litery):
        
        global control 
        pozycja_litery = numer_litery % 27
        if pozycja_litery > 0:
                litery.append(lista_liter[pozycja_litery - 1].upper())
        else: 
                control = 1 

def zwroc_mala_litere(numer_litery):
        
        global control 
        pozycja_litery = numer_litery % 27
        if pozycja_litery > 0:
                litery.append(lista_liter[pozycja_litery - 1].lower())
        else: 
                control = 2 


def zwroc_znak(numer_litery):
        
        global control 
        pozycja_litery = numer_litery % 9
        if pozycja_litery > 0:
                litery.append(lista_znakow[pozycja_litery - 1].lower())
        else: 
                control = 0 

for x in lista_liczb:
        if control == 0:
                zwroc_wielka_litere(x)
        elif control == 1:
                zwroc_mala_litere(x)
        elif control == 2:
                zwroc_znak(x)

final_output = "".join([str(e) for e in litery])

print(final_output)






















