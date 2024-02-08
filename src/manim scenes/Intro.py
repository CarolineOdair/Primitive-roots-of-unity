from manim import *

class IntroduceProblem(Scene):
    def construct(self):

        problem_text = Tex("Find all primitive $n$-th roots of unity.").scale(1)
        self.play(Write(problem_text))
        self.wait(3)

        self.play(problem_text.animate.shift(UP), run_time=2)

        plan = [
            "Complex numbers",
            "Complex roots",
            "Some abstract algebra",
            "Back to nice things"
            ]

        plan = [Text(text).set_opacity(0.5) for text in plan]

        group = VGroup(*plan).arrange(direction=DOWN).scale(0.5).next_to(ORIGIN, DOWN)
        self.play(Write(group))

        for num in range(len(plan)):
            obj = group.submobjects[num]
            self.wait(1)
            obj.set_opacity(1)
            self.wait(0.5)
            obj.set_opacity(0.5)


        self.wait(1)
