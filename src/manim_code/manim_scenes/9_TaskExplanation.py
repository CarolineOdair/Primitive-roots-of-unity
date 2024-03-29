from imports import *


class S9_TaskExpl(MyScene):  # 9th scene
    def construct(self):
        self.FS = 35

        obj = self.display_text()

        n = 8
        plane = self.add_plane_on_down_right(n)

        self.animate_about_primitives(plane[0], n, 3)
        self.animate_about_primitives(plane[0], n, 2)


        self.clear_screen(VGroup(obj, plane), color=COLOR_2)

        self.wait(3)


    def display_text(self) -> VGroup:

        task = Tex(r"Find all ", r"primitive ", r"$n$-th roots of unity", r".").shift(UP)
        formula_1 = MathTex(r"\varepsilon_k = \sqrt[n]{1}", color=COLOR_2).shift(2*UP)
        formula_2 = MathTex(r"\langle \varepsilon_k \rangle = E_n", color=COLOR_1)


        self.play(Write(task))
        self.play(FadeToColor(task[2], color=COLOR_2))

        self.play(Write(formula_1))
        self.wait()

        self.play(FadeToColor(task[1], color=COLOR_1))
        self.play(Write(formula_2))

        return VGroup(task, formula_1, formula_2)


    # add plane on the right of the screen
    def add_plane_on_down_right(self, n:int) -> VGroup:

        plane = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(DR)
        z_point, z_n_group = self.get_point_and_n_roots((1,0), n, plane, roots_color=COLOR_2, dot_radius=0.07)

        gr = VGroup(plane, z_n_group)
        self.play(Create(gr), run_time=4)
        self.wait()

        return gr

    def animate_about_primitives(self, plane, n:int, a:int) -> None:

        c = COLOR_1
        z = (1, a/n*2*PI)
        z_dot = Dot(plane.polar_to_point(*z), color=c, radius=0.08).set_z_index(2)
        z_label = MathTex(r"\varepsilon_k", font_size=self.FS).next_to(z_dot, 0.5*UR)

        num = [z]
        points = [plane.polar_to_point(*z)]
        dots = [z_dot]

        self.play(Create(dots[-1]))
        self.play(Write(z_label))


        for i in range(n-1):
            temp_num = (num[-1][0], num[-1][1]+a/n*2*PI)
            temp_point = plane.polar_to_point(*temp_num)
            temp_dot = Dot(temp_point, color=c, radius=0.08).set_z_index(2)

            length = (temp_point - points[-1])/2
            r = np.sqrt(length[0]**2 + length[1]**2)
            arrow = self.get_and_add_arrow(points[-1], temp_point, tip_length=0.2, radius=r*1.05, color=GRAY_B)


            num.append(temp_num)
            points.append(temp_point)
            dots.append(temp_dot)

            self.play(Create(temp_dot))
            self.play(FadeOut(arrow), run_time=0.5)


        self.play(FadeOut(z_label, *dots))
