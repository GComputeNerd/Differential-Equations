import subprocess

# Program to test rendering of LaTeX equation into a .svg file

# Rendering equation

test = r"$\dfrac{dy}{dx} = \dfrac{x^2}{30}$"
n = "test-eq" + ".tex"

template = open("template.tex")
f = open(n, "w")
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

# Render .tex into .dvi

subprocess.run(['latex', n])

# Render .dvi into .svg

subprocess.run(['dvisvgm', '-n', n])
