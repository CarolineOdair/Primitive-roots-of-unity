from imports import *

class S0_Miniature(MyScene):  # 1st scene
    def construct(self):
        
        text = r"Find all primitive $n$-th roots of unity."
        task = Tex(text, font_size=70).shift(0.5*UP)

        task.set_color_by_gradient(COLOR_1, COLOR_1, COLOR_3, COLOR_2, COLOR_2)
            
        line_gradient = Line(task.get_corner(DL)+0.1*DOWN, task.get_corner(DR)+0.1*DOWN)

        self.add(task, line_gradient)
