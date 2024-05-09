from imports import *


class S4_MultiplyingComplex(MyScene):  # 4th scene
    def construct(self):
        Z = (2, PI/6)
        W = (1.5, 7*PI/6)

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
        Z_point_label = MathTex("|z|e^{\imath\\varphi}", font_size=35).set_z_index(3).next_to(Z_point, UP, 0.1)
        Z_norm = Line(plane.get_origin(), Z_point, stroke_width=4, color=COLOR_1).set_z_index(2)
        Z_angle = Angle(plane.get_axis(0), Z_norm, radius=Z[0]/2, color=COLOR_1).set_z_index(2)

        Z_point_elements = [Z_point, Z_point_label, Z_norm, Z_angle]
        main_group = VGroup(plane, *Z_point_elements)

        self.add(main_group)

        self.wait(10)


        ######    add second point    ######

        W_point = Dot(plane.polar_to_point(*W), color=COLOR_2, radius=0.05).set_z_index(2)
        W_point_label = MathTex("|w|e^{\imath\\theta}", font_size=35).set_z_index(3).next_to(W_point, DOWN, 0.1)
        W_norm = Line(plane.get_origin(), W_point, stroke_width=4, color=COLOR_2).set_z_index(2)
        W_angle = Angle(plane.get_axis(0), W_norm, radius=W[0]/2, color=COLOR_2).set_z_index(2)

        W_point_elements = [W_point, W_norm, W_angle, W_point_label]
        W_point_group = VGroup(*W_point_elements)
        self.play(Create(W_point_group), run_time=3)

        self.wait(1)


        # equation z*w
        equation = MathTex(
            r"z \cdot w &=", 
            r"|z|", r"\;e^{\imath", r"\varphi}", r"\cdot", r"|w|", r"\;e^{\imath", r"\theta}", r"\\ &=", 
            r"|z||w|", r"\;e^{\imath (",r"\varphi + \theta", r")}",
        ).next_to((plane.get_corner(UR) + plane.get_right())/2, 3*RIGHT)
        
        self.play(Write(equation))

        rel_elements = [plane, Z, Z_point, Z_point_label, Z_norm, Z_angle]
        temp_group = self.multiplying(equation, rel_elements, abs(Z[0]-Z[0]*W[0]), W[1])
        temp_point = [sub for sub in temp_group.submobjects if type(sub)==Dot][0]
        temp_label = MathTex("|z||w|e^{\imath(\\varphi+\\theta)}", font_size=35).set_z_index(3).next_to(temp_point, DOWN, 0.1)
        self.play(Write(temp_label))
        self.wait(0.5)
        self.play(FadeOut(temp_group, temp_label, W_point_group
                           ), run_time=4)

        self.wait(0.5)

        # equation z^2
        equation_2 = MathTex(
            r"z^2 &= ", 
            r"|z|", r"\;e^{\imath", r"\varphi}", r"\cdot", r"|z|", r"\;e^{\imath", r"\varphi}", r"\\ &=", 
            r"|z|^2", r"\;e^{\imath ",r"2\varphi", r"}",
        ).next_to((plane.get_corner(UR) + plane.get_right())/2, 3*RIGHT)

        self.play(TransformMatchingTex(equation, equation_2))
        # self.play(ReplacementTransform(equation, equation_2))

        temp_group_2 = self.multiplying(equation_2, rel_elements, abs(Z[0]-Z[0]**2), Z[1])
        temp_point_2 = [sub for sub in temp_group_2.submobjects if type(sub)==Dot][0]
        temp_label_2 = MathTex("|z|^2e^{\imath 2\\varphi}", font_size=35).set_z_index(3).next_to(temp_point_2, UP, 0.1)
        self.play(Write(temp_label_2))
        self.wait(1)
        self.play(FadeOut(temp_group_2, temp_label_2, equation_2))


        last_dot = Dot(plane.get_origin(), color=COLOR_2, radius=0.05)
        self.play(ReplacementTransform(main_group, last_dot))
        self.play(Wiggle(last_dot), run_time=0.5)
        self.play(last_dot.animate.shift(3.5*RIGHT))
        self.play(Wiggle(last_dot), run_time=0.5)
        self.play(Uncreate(last_dot))

        self.wait(0.5)






    def multiplying(self, equation, rel_elements, delta_radius:float=0, delta_angle:float=0) -> VGroup:
        plane, Z, Z_point, Z_point_label, Z_norm, Z_angle = rel_elements

        # add tracker
        tracker_radius = ValueTracker(Z[0])
        tracker_angle = ValueTracker(Z[1])
        self.add(tracker_radius)
        self.add(tracker_radius)

        # add Z*W elements and up_daters
        ZW = Z
        ZW_point = Z_point.copy().set_color(COLOR_3).set_z_index(1)
        ZW_point = ZW_point.add_updater(
            lambda d: d.become(Dot(plane.polar_to_point(tracker_radius.get_value(), tracker_angle.get_value()), color=COLOR_3, radius=0.05).set_z_index(1)), 
        )
        ZW_norm = Z_norm.copy().set_color(COLOR_3).set_z_index(1).add_updater(
            lambda n: n.become(Line(plane.get_origin(), ZW_point, stroke_width=4, color=COLOR_3).set_z_index(1)))
        ZW_angle = Z_angle.copy().set_z_index(1).add_updater(
            lambda x: x.become(Angle(plane.get_axis(0), ZW_norm, radius=tracker_radius.get_value()/2, color=COLOR_3).set_z_index(1))
        )
        ZW_point_elements = [ZW_point, ZW_norm, ZW_angle]
        self.add(*ZW_point_elements)


        # multiplying norms
        mul_framebox_1 = SurroundingRectangle(equation[1], buff=.1, color=COLOR_1)
        mul_framebox_2 = SurroundingRectangle(equation[5], buff=.1, color=COLOR_2)
        mul_framebox_3 = SurroundingRectangle(equation[9], buff=.1, color=COLOR_3)
        mul_framebox_group = VGroup(mul_framebox_1, mul_framebox_2)
        self.play(Create(mul_framebox_group))

        self.play(Transform(mul_framebox_group, mul_framebox_3), tracker_radius.animate.set_value(Z[0]+delta_radius), run_time=3)
        self.play(FadeOut(mul_framebox_group))

        # adding angles
        add_framebox_1 = SurroundingRectangle(equation[3], buff=.1, color=COLOR_1)
        add_framebox_2 = SurroundingRectangle(equation[7], buff=.1, color=COLOR_2)
        add_framebox_3 = SurroundingRectangle(equation[11], buff=.1, color=COLOR_3)
        add_framebox_group = VGroup(add_framebox_1, add_framebox_2)
        self.play(Create(add_framebox_group))

        self.play(Transform(add_framebox_group, add_framebox_3), tracker_angle.animate.set_value(Z[1]+delta_angle), run_time=3)
        self.play(FadeOut(add_framebox_group))

        self.remove(tracker_angle)
        self.remove(tracker_radius)

        group = VGroup(ZW_point, ZW_norm, ZW_angle)
        for submobj in group:
            submobj.clear_updaters()

        return group


