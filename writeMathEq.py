import subprocess

# Program to test rendering of LaTeX equation into a .svg file

def renderMath(eqn, name):
    # Rendering equation
    
    template = open("template.tex")
    f = open(name + ".tex", "w")
    line = ""
    
    while (not (r"\begin{document}" in line)):
        line = template.readline()
        f.write(line)
    
    f.write(eqn)
    
    for line in template:
        f.write(line)
    
    template.close()
    f.close()
    
    # Render .tex into .dvi
    
    subprocess.run(['latex', name + ".tex"])
    
    # Render .dvi into .svg
    
    subprocess.run(['dvipng', '-bg', 'Transparent',  name + ".dvi", "-o", name + ".png"])
