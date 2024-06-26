from imports import *

class S12_Finish(MyScene):  # 12th scene
    def construct(self):
        
        task = Tex(r"Find all ", r"primitive ", r"$n$-th roots of unity", r".").shift(2*UP)
        line_gradient = Line(task.get_corner(DL), task.get_corner(DR))
        # line_gradient.set_color(color=[COLOR_2, COLOR_2, COLOR_1, COLOR_1])
        line_gradient.set_color(color=[COLOR_2, COLOR_1])

        self.play(Write(task), Create(line_gradient))

        solution = MathTex(r"\langle \varepsilon_k \rangle = E_n", r"\quad\iff\quad", r"\gcd(n,k)=1")
        solution[0].set_color(COLOR_1)
        solution[2].set_color(COLOR_2)

        self.play(Write(solution), run_tim=4)

        signature = ["Author:", "Karolina Fisiak"]
        signature = [Tex(el).set_opacity(0.5) for el in signature]
        signature_gr = VGroup(*signature).arrange(DOWN).scale(0.4).to_edge(DR)
        self.wait(2)
        self.play(Write(signature_gr))

        self.wait(2)
        vgr = VGroup(task, line_gradient, solution, signature_gr)

        final_dots = VGroup(Dot(color=COLOR_1), Dot(color=COLOR_2), Dot(color=COLOR_3)).arrange(RIGHT, 1)
        self.play(ReplacementTransform(vgr, final_dots))
        self.wait(0.5)
        self.play(Uncreate(final_dots))
        self.wait(2)

        
