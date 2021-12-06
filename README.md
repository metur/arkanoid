# arkanoid

Na pierwszym ekranie naciśnij "a" na klawiaturze spowoduje to odpalenie właściwego arkanoida i dodanie kilku bali. Gra polega na zbijaniu bloczków balami odbijając je od kijasa aby nie spadły. W grze nie ma jeszcze warunków wygranej ani przegranej.

Po wciśnięciu a i rozpoczęciu arkanoida działają następujące przyciski na klawiaturze:
q = wychodzi z arkanoida na pierwszy ekran (następne użycie zamyka program)
i = tworzy mapę z bloczków ustawioną w pliku level.txt (opisane później)
u = wypisuje matrycę bloczków

a = dodaje bale (max 100)
d = usuwa ostatnią bale (po spadnięciu odpowiednia bala jest usunięta)
x, strzalka do gory = dodaje pojedynczy bloczek, dodaje dużo pojedynczych bloczków
strzalka w dol = usuwa losowy bloczek
o = skrócenie kijasa
p = przedłużenie kijasa

Tworzenie mapy z bloczków polega na odpowiedniej interpretacji znaków w pliku tekstowym, w którym bloczki są podzielone przecinkiem. Coś jak CSV w zasadzie. Format bloczków jest następujący [Kod koloru][Kod wytrzymałości]. Przykładowo B2 wygeneruje bloczek o kolorze niebieskim o wytrzymałości 2. Wytrzymałość jest określona od liczby 1 do 4 włącznie. Dostępne są następujące kolory:
R - Czerwony
G - Zielony
B - Niebieski
Y - Szary/Biały
