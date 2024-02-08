from manim import *

from math import sqrt

# config.background_color = rgb_to_color([218,165,32])

class MultiplyingComplex(Scene):
    def construct(self):

        GOLDENROD = rgb_to_color([218,165,32])
        ROYALBLUE = rgb_to_color([65,105,225])

        ######    setup    ######
        plane = PolarPlane(
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
        ).shift(3.5*LEFT)
        point = Dot(plane.polar_to_point(2, PI/6), color=GOLDENROD, radius=0.05).set_z_index(2)
        point_label = MathTex("|z|e^{\imath\\varphi}").next_to(point, UR, 0.1)
        norm = Line(plane.get_origin(), point, stroke_width=4, color=GOLDENROD).set_z_index(1)
        angle = Angle(plane.get_axis(0), norm, radius=1, color=GOLDENROD)

        elements = [plane, point, point_label, norm, angle]
        main_group = VGroup(*elements)

        self.add(main_group)

        self.wait(1)


        ######    add second point    ######

        point_2 = Dot(plane.polar_to_point(1.5, 7*PI/6), color=BLUE_D, radius=0.05).set_z_index(2)
        point_label_2 = MathTex("|w|e^{\imath\\theta}").next_to(point_2, DL, 0.1)
        norm_2 = Line(plane.get_origin(), point_2, stroke_width=4, color=BLUE_D).set_z_index(1)
        angle_2 = Angle(plane.get_axis(0), norm_2, radius=0.75, color=BLUE_D).set_z_index(2)

        point_2_elements = [point_2, point_label_2, norm_2, angle_2]
        point_2_group = VGroup(*point_2_elements)
        self.play(Create(point_2_group), run_time=3)

        self.wait(1)

        
        ######    multiplying equations    ######

        




        self.wait(2)
