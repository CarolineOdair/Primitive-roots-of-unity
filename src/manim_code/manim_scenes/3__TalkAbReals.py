from imports import *
from random import randrange

class S3_TalkAbReals(MyScene):  # 3nd scene (before 3nd scene, it turned out that there's a hole in video narration)
    def construct(self):

        lines_and_labels = self.display_rational_nums()
        first_plane = self.get_first_plane()
        second_plane = self.get_plane_on_left()

        self.play(Create(first_plane))
        self.play(FadeOut(lines_and_labels))
        self.play(Transform(first_plane, second_plane))




    def display_rational_nums(self):
        rationals = []
        while len(rationals) < 100:
            rat = randrange(-730, 730) / 100
            if rat not in rationals:
                rationals.append(rat)
        

        vgr = VGroup(
            *[Dot(radius=0.04, color=COLOR_2).set_z_index(10).shift(rat*RIGHT) for rat in rationals]
            )
        dot1 = Dot(radius=0.04, color=COLOR_2).set_z_index(10)
        
        self.play(Create(dot1))
        self.play(AnimationGroup(*[Create(dot) for dot in vgr], run_time=21, lag_ratio=0.5))

        label_q = MathTex("\mathbb{Q}", color=COLOR_2).shift(4*RIGHT+0.5*UP)
        self.play(Write(label_q))
        self.wait()

        line_real = Line(-7.5*RIGHT, 7.5*RIGHT, color=GRID_COLOR)
        label_r = MathTex("\mathbb{R}").shift(6*RIGHT+0.5*UP)
        self.play(Create(line_real), run_time=2)
        self.play(Create(label_r))

        self.wait(2)
        self.play(FadeOut(vgr), FadeOut(dot1), FadeOut(label_q))
        self.wait(4)

        label_r_2 = MathTex("\cal{R}").shift(6*RIGHT+0.5*UP)
        self.play(TransformMatchingTex(label_r, label_r_2))

        self.wait(4)
        line_im = Line(-4*UP, 4*UP, color=GRID_COLOR)
        label_im = MathTex("\cal{I}").shift(0.5*RIGHT+3*UP)
        self.play(Create(line_im), run_time=2)
        self.play(Create(label_im))

        return VGroup(line_real, label_r_2, line_im, label_im) 


    def get_first_plane(self):
        c_plane = ComplexPlane(
            x_range=(-8, 8, 1),
            y_range=(-8, 8, 1),

            x_length=15,
            y_length=15,

            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        )

        return c_plane


    def get_plane_on_left(self):

        c_plane = ComplexPlane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),

            x_length=6,
            y_length=6,

            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        )

        return c_plane
    