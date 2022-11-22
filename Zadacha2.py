# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

coynt = 0

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not(x or y or z) == (not x and not y and not z):
                coynt = coynt + 1
                print('{3} !({0} or {1} or {2}) = !{0} and !{1} and !{2} '.format(x, y, z, coynt))
                if coynt == 8:
                    print('Утверждение истинно')
                


