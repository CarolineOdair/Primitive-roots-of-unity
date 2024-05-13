from imports import *

from math import sqrt



class S3_ComplexNumbers(Scene):  # 3rd scene

    def construct(self):

        GOLDENROD = rgb_to_color([218,165,32])

        ######    left plane    ######

        add_group = VGroup() # make group

        c_plane = ComplexPlane( # def plane
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),

            x_length=6,
            y_length=6,

            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        )

        self.play(Write(c_plane), run_time=5)
        self.wait(6)

        point_1 = Dot(c_plane.n2p(sqrt(3) + 1j), color=COLOR_1, radius=0.05).set_z_index(2) # def point
        self.play(Create(point_1))

        vline = c_plane.get_vertical_line(c_plane.c2p(sqrt(3), 1, 0), color=COLOR_1, stroke_width=4).set_z_index(1)
        mark_vline = MathTex("a").next_to(c_plane.c2p(sqrt(3), 0, 0), DOWN)
        hline = c_plane.get_horizontal_line(c_plane.c2p(sqrt(3), 1, 0), color=COLOR_1, stroke_width=4).set_z_index(1)
        mark_hline = MathTex("b").next_to(c_plane.c2p(0, 1, 0), LEFT)      

        self.wait(2)
        self.play(Create(vline, run_time=1), Write(mark_vline))
        self.wait()
        self.play(Create(hline, run_time=1), Write(mark_hline))
        hv_lines_group = VGroup(vline, mark_vline, hline, mark_hline)

        label_1 = MathTex("a+\imath b").next_to(point_1, UR, 0.1) # def label
        self.play(Write(label_1), run_time=2)

        z_label = MathTex("z = a+\imath b", color=COLOR_1)
        self.play(Write(z_label.to_edge(UP)), run_time=3)

        self.wait(8.5)

        add_group.add(c_plane, point_1, label_1, hv_lines_group)
        self.play(add_group.animate.shift(3.5*LEFT))


        ######    right plane    ######

        plane_2 = c_plane.copy()
        point_2 = point_1.copy()
        label_2_cart = label_1.copy()
        hv_lines_2_group = hv_lines_group.copy()

        multiply_group = VGroup(plane_2, point_2, label_2_cart, hv_lines_2_group).shift(7*RIGHT)

        self.play(Create(multiply_group), run_time=4.5)
        
        norm_of_point = Line(plane_2.get_origin(), point_2, stroke_width=4, buff=0).set_z_index(1)
        self.play(Create(norm_of_point), run_time=3)

        angle = Angle(plane_2.get_axis(0), norm_of_point, radius=1)
        self.play(Create(angle), run_time=3)
        self.wait(5.5)

        norm_label = MathTex("\sqrt{a^2+b^2}", font_size=25).move_to(norm_of_point.end).shift(0.7*LEFT+0.1*DOWN).rotate(PI/6)
        self.play(Write(norm_label), run_time=3)
        self.play(Transform(norm_label, MathTex("r", font_size=25).move_to(norm_of_point.end).shift(0.7*LEFT+0.1*DOWN).rotate(PI/6)))
        angle_label = MathTex("\\varphi", font_size=25).next_to(angle, 0.5*RIGHT)
        self.play(Write(angle_label))

        self.remove(hv_lines_2_group)

        multiply_group.add(norm_of_point, norm_label, angle, angle_label)
        multiply_group.remove(hv_lines_2_group)


        self.wait(2)
        self.play(
            FadeToColor(norm_of_point, COLOR_1), 
            FadeToColor(angle, COLOR_1)
        )


        label_2_exp = MathTex("r e^{\imath \\varphi}").next_to(point_2, UR, 0.1)
        self.play(Transform(label_2_cart, label_2_exp), run_time=5)
        self.wait()

        # Z_point_label = MathTex("|z|e^{\imath\\varphi}", font_size=35).set_z_index(3).next_to(point_2, UP, 0.1)

        label_3_exp = MathTex("|z| e^{\imath \\varphi}", font_size=35).next_to(point_2, UP, 0.1)
        self.play(Transform(label_2_cart, label_3_exp), run_time=2)

        z_label_edited = MathTex("z = a+\imath b = |z| e^{\imath \\varphi}", color=COLOR_1).to_edge(UP)
        self.play(Transform(z_label, z_label_edited))

        self.wait(2)


        plane_2.prepare_for_nonlinear_transform()
        p_plane = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_step = 12,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
            ).shift(3.5*RIGHT)
        self.play(Transform(plane_2, p_plane))


        ######    remove left plane and prepare for next scene    ######

        self.play(FadeOut(add_group), multiply_group.animate.shift(7*LEFT))

        self.play(FadeOut(norm_label, angle_label, z_label))

        self.wait(2)