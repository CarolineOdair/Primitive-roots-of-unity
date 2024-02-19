from imports import *


class ComplexRoots(MyScene):  # 6th scene
    def construct(self):
        FS = 35
        
        ######    formulas    ######
        formula_number, vgroup = self.animate_text_on_the_beg(font_size=FS)
        formula_root, formula_power, formula_roots = vgroup

        plane = self.add_plane(azimuth_step=8, shiftt=3*RIGHT+0.5*DOWN, r_values=[1,2])
        self.add(plane)
        

        ######    examples    ######
        self.manage_examples(plane)


        ######    unity case    ######
        problem_text = Tex(r"Find all primitive\\", r"$n^{th}$ roots of unity", r".").shift(3*RIGHT)
        self.play(Write(problem_text))
        self.play(FadeToColor(problem_text[-2], color=COLOR_1))

        formula_number_2, vgroup_2 = self.animate_text_about_unity(formula_number, *vgroup)


        ######    clear screen    ######
        mobj_on_screen = VGroup(formula_number_2, *vgroup_2, problem_text)
        self.clear_screen(mobj_on_screen, color=NAVY_BLUE)


        ######    roots of 1 examples    ######
        planes_roots_of_1 = self.display_examples_roots_of_1()


        self.clear_screen(planes_roots_of_1, COLOR_1)




        self.wait(5)


    def display_examples_roots_of_1(self):
        def get_pos(i, length):
            if i < length/2:
                VER = 1.5*UP 
            else:
                VER = 1.5*DOWN 
            HOR = 4.5*LEFT + (i % 4)*3*RIGHT
            return VER+HOR
            
        def get_color(i, length):
            if (i < length/2 and i%2 == 0) or (i > length/2 and i%2 == 1):
                return COLOR_1
            return COLOR_2


        elements_for_planes_group = []
        n_ = [2, 3, 4, 5, 8, 12, 17, 20]
        length = len(n_)

        for i in range(length):
            pos = get_pos(i, length)
            col = get_color(i, length)

            plane = self.add_plane(azimuth_step=1, size=2.5, radius_max=1.5, radius_step=0.5).shift(pos)
            z_point, z_n_group = self.get_point_and_n_roots((1,0), n_[i], plane, roots_color=col)

            gr = VGroup(plane, z_n_group)
            elements_for_planes_group.append(gr)
            

        vgr = VGroup(*elements_for_planes_group)
        self.play(Create(vgr), run_time=8)

        return vgr



    def clear_screen(self, mobjects_on_screen, color=COLOR_1) -> None:

        last_dot = Dot(color=color)
        self.play(ReplacementTransform(mobjects_on_screen, last_dot))
        self.wait(0.5)
        self.play(Uncreate(last_dot))




    def animate_text_about_unity(self, formula_number, formula_root, formula_power, formula_roots, font_size:int=35):
        FS = font_size

        ######    prepare changes    ######

        # z = r e^{i*phi}
        formula_number_ch = [
            [r"z", r"=", r"r", r"e^{\imath", r"\varphi", r"}", r"= 1"],
            [r"z", r"=", r"1", r"e^{\imath", r"\varphi", r"}", r"= 1"], # 2 -> r = 1
            [r"z", r"=", r"e^{\imath", r"\varphi", r"}", r"= 1"],
            [r"z", r"=", r"e^{\imath", r"0", r"}", r"= 1"], # 4 -> phi = 0
            [r"z", r"=", r"1"],
        ]
        formula_number_ch = [MathTex(*text, font_size=FS+10).to_edge(UP) for text in formula_number_ch]
        formula_number_ch.insert(0, formula_number)

        # \sqrt[n] = w
        # w^n = z
        formula_root_ch = MathTex(r"\sqrt[n]{1}", r"=", r"w", font_size=FS+10).shift(3*LEFT+UP)
        formula_power_ch = MathTex(r"w^n", r"=", r"1", font_size=FS+10).shift(3*LEFT)
        formulas_ch_z = [
            (formula_root, formula_root_ch),
            (formula_power, formula_power_ch)
        ]

        # w_k = \sqrt[n]{r} e^{i (phi + 2k*pi)/n}
        formula_roots_list_ch = [
            [r"w_k", r"=", r"\sqrt[n]{|1|}", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)"], # 1 -> r = 1
            [r"w_k", r"=", r"1", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)"],
            [r"w_k", r"=", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)"],
            [r"w_k", r"=", r"\exp\left(\imath\frac{0+2k\pi}{n}\right)"], # 4 -> phi = 0
            [r"w_k", r"=", r"\exp\left(\imath\frac{2k\pi}{n}\right)"],
            [r"w_k", r"=", r"\exp\left(\frac{\imath 2k\pi}{n}\right)"]
        ]
        formula_roots_list_ch = [MathTex(*text, font_size=FS+10).shift(3*LEFT+DOWN) for text in formula_roots_list_ch]
        formula_roots_list_ch.insert(0, formula_roots)

        
        
        ######    changes    ######

        # z = 1 change
        self.play(TransformMatchingTex(formula_number_ch[0], formula_number_ch[1]))
        for text in formulas_ch_z:
            self.play(TransformMatchingTex(text[0], text[1]))

        # r = 1 change
        self.show_transform_and_fadeout_expl(formula_number_ch, start=2, end=4, fade_out=False)
        self.show_transform_and_fadeout_expl(formula_roots_list_ch, start=1, end=4, fade_out=False)

        # phi = 0 change
        self.show_transform_and_fadeout_expl(formula_number_ch, start=4, fade_out=False)
        self.show_transform_and_fadeout_expl(formula_roots_list_ch, start=4, fade_out=False)



        vgroup = VGroup(formula_root_ch, formula_power_ch, formula_roots_list_ch[-1])
        return formula_number_ch[-1], vgroup



    def manage_examples(self, plane, font_size:int=35):
        FS = font_size
        examples = [
            ((2, 0*PI), 2, r"$2^{nd}$ roots of $2$"),
            ((2, 1/2*PI), 5, r"$5^{th}$ roots of $2 e^{\imath 1/2\pi}$"),
            ((2, PI), 10, r"$10^{th}$ roots of $2 e^{\imath \pi}$"),
            ((1, 3/2*PI), 2, r"$2^{nd}$ roots of $1 e^{\imath 3/2\pi}$"),
            ((1, 0*PI), 5, r"$5^{th}$ roots of $1$"),
            ((1, 5/3*PI), 10, r"$10^{th}$ roots of $1 e^{\imath 5/3\pi}$"),
            ((0.5, 7/4*PI), 2, r"$2^{nd}$ roots of $0.5 e^{\imath 7/4\pi}$"),
            ((0.5, 4/3*PI), 5, r"$5^{th}$ roots of $0.5 e^{\imath 4/3\pi}$"),
            ((0.5, 0*PI), 10, r"$10^{th}$ roots of $0.5$"),
        ]


        elements_for_planes_group = []

        for (z, n, text) in examples:

            roots_formula = Tex(text, font_size=FS, tex_environment="center").next_to(plane.get_top(), 0.5*UP)
            self.add(roots_formula)

            z_point, z_n_group = self.get_point_and_n_roots(z, n, plane)
            self.add_and_remove_point_and_n_roots(z_point, z_n_group)

            self.remove(roots_formula)

            gr = VGroup(plane.copy().set_color(GREY_B), z_point, z_n_group).scale(0.5).shift(3*LEFT+0.5*UP)
            elements_for_planes_group.append(gr)


        self.play(Uncreate(plane), run_time=0.5)

        planes_group = VGroup(*elements_for_planes_group).arrange_in_grid(rows=3, cols=3, buff=0.2).shift(3*RIGHT+0.5*DOWN)
        self.play(AnimationGroup(*[FadeIn(p) for p in planes_group], lag_ratio=0.25))
        self.wait(2)
        self.play(FadeOut(planes_group))




    def animate_text_on_the_beg(self, font_size:int=35):
        FS = font_size

        formula_number = MathTex(r"z", r"=", r"r", r"e^{\imath", r"\varphi", r"}", font_size=FS+10).to_edge(UP)
        formula_root = MathTex(r"\sqrt[n]{z}", r"=", r"w", font_size=FS+10).shift(UP)
        formula_power = MathTex(r"w^n", r"=", r"z", font_size=FS+10)
        
        formula_roots_list = [
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)", r",\quad k\in", r"\mathbb{Z}"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)", r",\quad k\in", r"\{0,1,...,n-1\}"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)", r",\quad k\in", r"\mathbb{Z}_n"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath\frac{\varphi+2k\pi}{n}\right)"]
        ]
        formula_roots_list = [MathTex(*text, font_size=FS+10).shift(DOWN) for text in formula_roots_list]

        formula_roots_power_expl_list = [
            [r"w_k^n", r"=", r"\left(", r"\sqrt[n]{r}", r"\exp\left( \imath", r"\frac{\varphi+2k\pi}{n}",       r"\right)", r"\right)^n", r",\quad k\in\mathbb{Z}"],
            [r"w_k^n", r"=",          r"\sqrt[n]{r}^n", r"\exp\left( \imath", r"\frac{\varphi+2k\pi}{n}",       r"\right)", r"^n",        r",\quad k\in\mathbb{Z}"],
            [r"w_k^n", r"=", r"r",                      r"\exp\left( \imath", r"\frac{\varphi+2k\pi}{n}\cdot n",r"\right)",               r",\quad k\in\mathbb{Z}"],
            [r"w_k^n", r"=", r"r",                      r"\exp\left( \imath",       r"\varphi+2k\pi",           r"\right)",               r",\quad k\in\mathbb{Z}"],
            [r"w_k^n", r"=", r"r",                      r"\exp\left( \imath",       r"\varphi",                 r"\right)",               r",\quad k\in\mathbb{Z}"],
            [r"w_k^n", r"=", r"z", r",\quad k\in\mathbb{Z}"]
        ]
        formula_roots_power_expl_list = [MathTex(*text, font_size=FS).shift(2.3*DOWN) for text in formula_roots_power_expl_list]

        formula_roots_expl_list = [
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath",            r"\frac{\varphi+2(n+m)\pi}{n}",         r"\right)", r",\quad k = n+m,\; m < n"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath",            r"\frac{\varphi+2m\pi+2n\pi}{n}",       r"\right)", r",\quad k = n+m,\; m < n"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath", r"\left(", r"\frac{\varphi+2m\pi}{n}", r"+2\pi", r"\right)", r"\right)", r",\quad k = n+m,\; m < n"],
            [r"w_k", r"=", r"\sqrt[n]{r}", r"\exp\left(\imath",            r"\frac{\varphi+2m\pi}{n}",                       r"\right)", r",\quad k = n+m,\; m < n"]
        ]
        formula_roots_expl_list = [MathTex(*text, font_size=FS).shift(2.3*DOWN) for text in formula_roots_expl_list]

        start_formulas = [formula_number, formula_root, formula_power, formula_roots_list[0]]
        for f in start_formulas:
            self.play(Write(f))

        self.show_transform_and_fadeout_expl(formula_roots_power_expl_list, circumscribe=True, transform_goal=formula_power)
        self.show_transform_and_fadeout_expl(formula_roots_expl_list, circumscribe=True, transform_goal=formula_roots_list[0])
        self.show_transform_and_fadeout_expl(formula_roots_list, start=1, fade_out=False, circumscribe=True)

        vgroup = VGroup(formula_root, formula_power, formula_roots_list[3])
        self.play(vgroup.animate.shift(3.5*LEFT))

        return formula_number, vgroup
    



    def show_transform_and_fadeout_expl(self, list_of_formulas, start:int=0, end:int=None, fade_out:bool=True, circumscribe:bool=False, transform_goal=None) -> None:

        length = len(list_of_formulas)
        if end is None or end > length:
            end = length


        for l in range(start, end):
            if l == 0:
                self.play(Write(list_of_formulas[l]))
            elif l > 0 and l < end:
                self.play(TransformMatchingTex(list_of_formulas[l-1], list_of_formulas[l]))


        if circumscribe and transform_goal is not None:
            self.play(Circumscribe(list_of_formulas[end-1], color=COLOR_1), Circumscribe(transform_goal, color=COLOR_2))
        elif circumscribe:
            self.play(Circumscribe(list_of_formulas[end-1], color=COLOR_1, fade_out=True))


        if fade_out:
            self.play(FadeOut(list_of_formulas[end-1]))



    def add_plane(self, azimuth_step=12, shiftt=0, size=4, radius_step=1, radius_max=3, r_values:list=[]):
        plane = PolarPlane(
            azimuth_units="PI radians",
            size=size,
            azimuth_compact_fraction = False,
            azimuth_step = azimuth_step,
            radius_step = radius_step,
            radius_max=radius_max,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        ).add_coordinates(r_values=r_values, a_values=[]).shift(shiftt)

        return plane
    
    def add_and_remove_point_and_n_roots(self, point, roots, if_point:bool=True) -> None:

        self.wait(0.5)
        if if_point:
            self.add(point)
            self.wait(1)
        self.play(Create(roots))
        self.wait(1)
        self.remove(point, roots)
