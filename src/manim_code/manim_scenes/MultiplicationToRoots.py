from imports import *


class TransitionToUnit(MyScene):  # 5th scene
    def construct(self):
        Z = (2, PI/6)

        ######    setup    ######
        plane = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_step = 12,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        ).shift(3.5*LEFT)
        Z_point = Dot(plane.polar_to_point(*Z), color=COLOR_1, radius=0.05).set_z_index(2)
        Z_point_label = MathTex("|z|e^{\imath\\varphi}", font_size=35).next_to(Z_point, UR, 0.1)
        Z_norm = Line(plane.get_origin(), Z_point, stroke_width=4, color=COLOR_1).set_z_index(2)
        Z_angle = Angle(plane.get_axis(0), Z_norm, radius=Z[0]/2, color=COLOR_1).set_z_index(2)
        group = VGroup(Z_point, Z_point_label, Z_norm, Z_angle)

        Z_point_elements = [Z_point, Z_point_label, Z_norm, Z_angle]
        main_group = VGroup(plane, *Z_point_elements)

        self.add(main_group)

        self.wait(1)


        plane_2 = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            radius_step=0.5,
            radius_max=1.5,
            azimuth_step = 12,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            },
            radius_config = {
                "include_ticks": True,
            }

        ).shift(3.5*LEFT)

        Z_point_2 = Dot(plane_2.polar_to_point(1, PI/6), color=COLOR_1, radius=0.08).set_z_index(2)
        Z_point_label_2 = MathTex("e^{\imath\\varphi}", font_size=35).next_to(Z_point_2, UR, 0.1)
        main_group_2 = VGroup(plane_2, Z_point_2, Z_point_label_2)

        self.play(ReplacementTransform(main_group, main_group_2))

        self.play(ReplacementTransform(main_group, main_group.shift(3.5*RIGHT)))


        coords = VGroup()
        coords.add(MathTex("-1", font_size=30).next_to(plane_2.polar_to_point(1, PI), DOWN, 0.2))
        coords.add(MathTex("1", font_size=30).next_to(plane_2.polar_to_point(1, 0), DOWN, 0.2))
        coords.add(MathTex(f"-\\imath", font_size=30).next_to(plane_2.polar_to_point(1, 3*PI/2), RIGHT, 0.2))
        coords.add(MathTex(f"\\imath", font_size=30).next_to(plane_2.polar_to_point(1, PI/2), RIGHT, 0.2))
        self.play(FadeIn(coords))


        self.play(Create(Circle(2, color=GREY_A).set_z_index(1)))

        self.wait(2)

