# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z) == not x and not y and not z:
                print('!({0} or {1} or {2}) = !{0} and !{1} and !{2} '.format(x, y, z))