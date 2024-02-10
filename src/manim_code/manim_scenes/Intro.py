from imports import *

class IntroduceProblem(MyScene):  # 2nd scene
    def construct(self):

        problem_text = Tex("Find all primitive $n$-th roots of unity.").scale(1)
        self.play(Write(problem_text))
        self.wait(3)

        self.play(problem_text.animate.shift(2*UP), run_time=2)
        self.play(ReplacementTransform(problem_text, Tex("Find all primitive $n$-th roots of unity.", color=COLOR_1, opacity=0.5).scale(1).shift(2*UP)))

        plan = [
            "Complex numbers",
            "Complex roots",
            "Some abstract algebra",
            "Back to nice things"
            ]

        plan = [Text(text).set_opacity(0.5) for text in plan]

        # TODO probably positioning needs to be changed
        group = VGroup(*plan).arrange(DOWN).scale(0.5).next_to(problem_text.get_bottom(), 2*DOWN)
        self.play(Write(group))

        for num in range(len(plan)):
            obj = group.submobjects[num]
            self.wait(1)
            obj.set_opacity(1)
            self.wait(0.5)
            obj.set_opacity(0.5)


        self.wait(1)
