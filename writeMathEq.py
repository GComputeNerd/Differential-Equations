# Program to test rendering of LaTeX equation into a .png file

# Rendering equation

test = r"$\dfrac{dy}{dx} = \dfrac{x^2}{30}$"
n = "test-eq"

template = open("template.tex")
f = open(n + ".tex", "w")
line = ""

while (not (r"\begin{document}" in line)):
    line = template.readline()
    print(line)
    f.write(line)

f.write(test)

for line in template:
    f.write(line)

template.close()
f.close()
