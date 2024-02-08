from manim import *
from math import sqrt

# config.background_color = rgb_to_color([0, 17, 38])

class ComplexNumbers(Scene):

    def construct(self):
        # self.camera.background_color = WHITE

        GOLDENROD = rgb_to_color([218,165,32])
        Z = sqrt(3) + 1j

        ######    left plane    ######

        add_group = VGroup() # make group

        c_plane = ComplexPlane( # def plane
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),

            x_length=6,
            y_length=6,

            background_line_style={
                "stroke_color": LIGHT_PINK,
                "stroke_width": 4,
                "stroke_opacity": 0.5
            }
        )

        self.play(Write(c_plane), run_time=2)
        self.wait(2)

        point_1 = Dot(c_plane.n2p(sqrt(3) + 1j), color=GOLDENROD, radius=0.05).set_z_index(2) # def point
        label_1 = MathTex("a+\imath b").next_to(point_1, UR, 0.1) # def label
        self.play(Create(point_1), Write(label_1))

        z_label = MathTex("z = a+\imath b", color=GOLDENROD)
        self.play(Write(z_label.to_edge(UP)))

        vline = c_plane.get_vertical_line(c_plane.c2p(sqrt(3), 1, 0), color=GOLDENROD, stroke_width=4).set_z_index(1)
        mark_vline = MathTex("a").next_to(c_plane.c2p(sqrt(3), 0, 0), DOWN)
        hline = c_plane.get_horizontal_line(c_plane.c2p(sqrt(3), 1, 0), color=GOLDENROD, stroke_width=4).set_z_index(1)
        mark_hline = MathTex("b").next_to(c_plane.c2p(0, 1, 0), LEFT)      

        self.play(Create(vline, run_time=1), Write(mark_vline))
        self.play(Create(hline, run_time=1), Write(mark_hline))
        hv_lines_group = VGroup(vline, mark_vline, hline, mark_hline)

        add_group.add(c_plane, point_1, label_1, hv_lines_group)
        self.play(add_group.animate.shift(3.5*LEFT))


        ######    right plane    ######

        plane_2 = c_plane.copy()
        point_2 = point_1.copy()
        label_2_cart = label_1.copy()
        hv_lines_2_group = hv_lines_group.copy()

        multiply_group = VGroup(plane_2, point_2, label_2_cart, hv_lines_2_group).shift(7*RIGHT)

        self.play(Create(multiply_group))
        
        norm_of_point = Line(plane_2.get_origin(), point_2, stroke_width=4, buff=0).set_z_index(1)
        norm_label = MathTex("\sqrt{a^2+b^2}", font_size=25).move_to(norm_of_point.end).shift(0.7*LEFT+0.1*DOWN).rotate(PI/6)
        self.play(Create(norm_of_point), Write(norm_label), run_time=3)
        self.play(Transform(norm_label, MathTex("|z|", font_size=25).move_to(norm_of_point.end).shift(0.7*LEFT+0.1*DOWN).rotate(PI/6)))

        angle = Angle(plane_2.get_axis(0), norm_of_point, radius=1)
        self.play(Create(angle))
        angle_label = MathTex("\\varphi", font_size=25).next_to(angle, 0.5*RIGHT)
        self.play(Write(angle_label))

        self.remove(hv_lines_2_group)

        multiply_group.add(norm_of_point, norm_label, angle, angle_label)
        multiply_group.remove(hv_lines_2_group)


        self.wait(1)
        self.play(
            ReplacementTransform(norm_of_point, norm_of_point.set_color(GOLDENROD)), 
            ReplacementTransform(angle, angle.set_color(GOLDENROD))
            )


        plane_2.prepare_for_nonlinear_transform()
        p_plane = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_step = 12,
            azimuth_label_font_size=20,
            radius_config={"font_size": 20},
            background_line_style={
                "stroke_color": LIGHT_PINK,
                "stroke_width": 4,
                "stroke_opacity": 0.5
            }
            ).shift(3.5*RIGHT)
        self.play(Transform(plane_2, p_plane))

        label_2_exp = MathTex("|z| e^{\imath \\varphi}").next_to(point_2, UR, 0.1)
        self.play(Transform(label_2_cart, label_2_exp), run_time=3)

        z_label_edited = MathTex("z = a+\imath b = |z| e^{\imath \\varphi}", color=GOLDENROD).to_edge(UP)
        self.play(Transform(z_label, z_label_edited))

        self.play(FadeOut(add_group), multiply_group.animate.shift(7*LEFT))

        self.play(FadeOut(norm_label, angle_label, z_label))

        self.wait(2)