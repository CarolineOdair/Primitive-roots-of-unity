from imports import *
from threading import Thread


class S9_TaskExpl(MyScene):  # 9th scene
    def construct(self):
        self.FS = 35

        obj = self.display_text()

        n = 8

        plane_left, plane_right = self.add_planes(n)
        self.animate_about_primitives(plane_left[0], plane_right[0], n, 2, 3)

        self.wait(2)
        self.clear_screen(VGroup(obj, plane_left, plane_right), color=COLOR_2)



    def display_text(self) -> VGroup:

        task = Tex(r"Find all ", r"primitive ", r"$n$-th roots of unity", r".").shift(UP)
        formula_1 = MathTex(r"\varepsilon_k = \sqrt[n]{1}", color=COLOR_2).shift(2*UP)
        formula_2 = MathTex(r"\langle \varepsilon_k \rangle = E_n", color=COLOR_1)


        self.play(Write(task))
        self.play(FadeToColor(task[2], color=COLOR_2))

        self.play(Write(formula_1))
        self.wait(3)

        self.play(FadeToColor(task[1], color=COLOR_1))
        self.play(Write(formula_2))

        return VGroup(task, formula_1, formula_2)


    # add plane on the right of the screen
    def add_plane_on_down_right(self, n:int) -> VGroup:
        # I do not use it, but it was nice when I wanted only 1 plane (on the right)

        plane = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(DR)
        z_point, z_n_group = self.get_point_and_n_roots((1,0), n, plane, roots_color=COLOR_2, dot_radius=0.07)

        gr = VGroup(plane, z_n_group)
        self.play(Create(gr), run_time=4)
        self.wait()

        return gr
    
    def add_planes(self, n:int) -> VGroup:

        plane_right = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(DR)
        z_point_right, z_n_group_right = self.get_point_and_n_roots((1,0), n, plane_right, roots_color=COLOR_2, dot_radius=0.07)
        gr_right = VGroup(plane_right, z_n_group_right)

        plane_left = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(DL)
        z_point_left, z_n_group_left = self.get_point_and_n_roots((1,0), n, plane_left, roots_color=COLOR_2, dot_radius=0.07)
        gr_left = VGroup(plane_left, z_n_group_left)

 
        self.play(Create(gr_left), Create(gr_right), run_time=4)
        self.wait()

        return gr_left, gr_right
    
    # def animate_about_primitives(self, plane, n:int, a:int, run_time_weight=1) -> None:
    #     # version for managing one plane at time

    #     c = COLOR_1

    #     z = (1, a/n*2*PI)
    #     z_dot = Dot(plane.polar_to_point(*z), color=c, radius=0.08).set_z_index(2)
    #     z_label = MathTex(r"\varepsilon_k", font_size=self.FS).next_to(z_dot, 0.5*UR)

    #     num = [z]
    #     points = [plane.polar_to_point(*z)]
    #     dots = [z_dot]


    #     self.play(Create(dots[-1]))
    #     self.play(Write(z_label))


    #     for i in range(n-1):
    #         temp_num = (num[-1][0], num[-1][1]+a/n*2*PI)
    #         temp_point = plane.polar_to_point(*temp_num)
    #         temp_dot = Dot(temp_point, color=c, radius=0.08).set_z_index(2)

    #         length = (temp_point - points[-1])/2
    #         r = np.sqrt(length[0]**2 + length[1]**2)
    #         arrow = self.get_and_add_arrow(points[-1], temp_point, tip_length=0.2, radius=r*1.05, color=GRAY_B)


    #         num.append(temp_num)
    #         points.append(temp_point)
    #         dots.append(temp_dot)

    #         self.play(Create(temp_dot))
    #         self.play(FadeOut(arrow), run_time=0.5)


    #     self.play(FadeOut(z_label, *dots))



    def animate_about_primitives(self, plane1, plane2, n:int, a1:int, a2:int, run_time_weight=1) -> None:

        c = COLOR_1

        # left part
        z1 = (1, a1/n*2*PI)
        z_dot1 = Dot(plane1.polar_to_point(*z1), color=c, radius=0.08).set_z_index(2)
        z_label1 = MathTex(r"\varepsilon_k", font_size=self.FS).next_to(z_dot1, 0.5*UR)

        num1 = [z1]
        points1 = [plane1.polar_to_point(*z1)]
        dots1 = [z_dot1]


        # right part
        z2 = (1, a2/n*2*PI)
        z_dot2 = Dot(plane2.polar_to_point(*z2), color=c, radius=0.08).set_z_index(2)
        z_label2 = MathTex(r"\varepsilon_k", font_size=self.FS).next_to(z_dot2, 0.5*UR)

        num2 = [z2]
        points2 = [plane2.polar_to_point(*z2)]
        dots2 = [z_dot2]


        # both
        self.play(Create(dots1[-1]), Create(dots2[-1]), run_time=run_time_weight)
        self.play(Write(z_label1),Write(z_label2), run_time=run_time_weight)


        for i in range(n-1):
            # left part
            temp_num1 = (num1[-1][0], num1[-1][1]+a1/n*2*PI)
            temp_point1 = plane1.polar_to_point(*temp_num1)
            temp_dot1 = Dot(temp_point1, color=c, radius=0.08).set_z_index(2)

            length1 = (temp_point1 - points1[-1])/2
            r1 = np.sqrt(length1[0]**2 + length1[1]**2)
            arrow1 = self.get_and_add_arrow(points1[-1], temp_point1, tip_length=0.2, radius=r1*1.05, color=GRAY_B, play=False)

            num1.append(temp_num1)
            points1.append(temp_point1)
            dots1.append(temp_dot1)


            # right part
            temp_num2 = (num2[-1][0], num2[-1][1]+a2/n*2*PI)
            temp_point2 = plane2.polar_to_point(*temp_num2)
            temp_dot2 = Dot(temp_point2, color=c, radius=0.08).set_z_index(2)

            length2 = (temp_point2 - points2[-1])/2
            r2 = np.sqrt(length2[0]**2 + length2[1]**2)
            arrow2 = self.get_and_add_arrow(points2[-1], temp_point2, tip_length=0.2, radius=r2*1.05, color=GRAY_B, play=False)

            num2.append(temp_num2)
            points2.append(temp_point2)
            dots2.append(temp_dot2)


            # both
            self.play(Create(arrow1), Create(arrow2), run_time=run_time_weight)
            self.play(Create(temp_dot1), Create(temp_dot2), run_time=run_time_weight)
            self.play(FadeOut(arrow1), FadeOut(arrow2), run_time=0.5*run_time_weight)


        self.play(FadeOut(z_label1, *dots1, z_label2, *dots2), run_time=run_time_weight)
