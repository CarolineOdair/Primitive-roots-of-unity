from imports import *

class S2_IntroduceProblem(MyScene):  # 2nd scene
    def construct(self):

        problem_text = Tex("Find all primitive $n$-th roots of unity.").scale(1.2)
        self.play(Write(problem_text))
        self.wait(3)

        self.play(problem_text.animate.shift(2*UP))
        self.play(ReplacementTransform(problem_text, Tex("Find all primitive $n$-th roots of unity.", color=COLOR_1, opacity=0.5).scale(1.2).shift(2*UP)))

        plan = [
            "Complex numbers",
            "Complex roots",
            "Some abstract algebra",
            "Algebra + complex numbers"
            ]

        plan = [Text(text).set_opacity(0.5) for text in plan]

        group = VGroup(*plan).arrange(DOWN).scale(0.65).next_to(problem_text.get_bottom(), 2.5*DOWN)
        self.play(Write(group))

        for num in range(len(plan)):
            obj = group.submobjects[num]
            self.wait(1)
            obj.set_opacity(1)
            self.wait(6)
            obj.set_opacity(0.5)


        self.wait(3)
