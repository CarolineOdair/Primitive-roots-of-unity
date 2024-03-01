from imports import *


class RootsAreGroup(MyScene):  # 7th scene
    def construct(self):
        self.FS = 35

        axioms_color = GREY_C
        roots_color = COLOR_1

        ######    add_plane    ######
        plane_obj_group = self.add_plane_on_right()
        right_limit = plane_obj_group[0].get_left()
        left_limit = 7*LEFT
        horizontal_shift = (right_limit+left_limit)/2


        ######    check group axioms    ######
        group_notation_group = self.add_group_text(axioms_color, roots_color, horizontal_shift)
        self.check_0_axiom(axioms_color, roots_color, plane_obj_group, horizontal_shift)
        self.check_1_axiom(axioms_color, roots_color, plane_obj_group, horizontal_shift)
        self.check_2_axiom(axioms_color, roots_color, plane_obj_group, horizontal_shift)
        self.check_3_axiom(axioms_color, roots_color, plane_obj_group, horizontal_shift)


        self.wait(2)

        self.play(FadeOut(group_notation_group, plane_obj_group))

        self.wait(2)



    # add plane on the right of the screen
    def add_plane_on_right(self) -> VGroup:

        n=8

        plane = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(RIGHT)
        z_point, z_n_group = self.get_point_and_n_roots((1,0), 13, plane, roots_color=COLOR_2, dot_radius=0.07)
        plane_title = MathTex(r"\text{E}_n", font_size=self.FS).next_to(plane, 0.5*UP)
        plane_title_update = MathTex(r"\text{E}_n", r"= \{ e^{\imath 2k\pi/n}: k\in\mathbb{Z}_n \}", font_size=self.FS).next_to(plane, 0.5*UP)

        self.play(Create(VGroup(plane, z_n_group, plane_title)), run_time=4)
        self.wait()
        self.play(TransformMatchingTex(plane_title, plane_title_update))

        gr = VGroup(plane, plane_title_update, z_n_group)
        self.add(gr)

        return gr

    def add_plane(self, azimuth_step:float=12, shiftt:Vector=0, size:float=4, radius_step:float=1, radius_max:float=3, r_values:list=[]) -> PolarPlane:
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
    


    # add text `(G,*)   (E_n, \cdot)`
    def add_group_text(self, theory_color:ManimColor, example_color:ManimColor, hor_position:Vector=ORIGIN) -> VGroup:
        theory = MathTex(r"(G,*)", color=theory_color, font_size=self.FS+10)
        example = MathTex(r"(E_n, \cdot)", color=example_color, font_size=self.FS+10)
        vgr = VGroup(theory, example).arrange_in_grid(rows=1, cols=2, buff=0.5).shift(hor_position).to_edge(UP)

        self.play(AnimationGroup(*[Write(p) for p in vgr], lag_ratio=1))
        
        return vgr
    

    # manage 0 axiom - inner
    def check_0_axiom(self, theory_color:ManimColor, example_color:ManimColor, plane_vgr:VGroup, hor_position:Vector=ORIGIN) -> None:
        theory = MathTex(r"\forall_{a,b\in G}\quad a*b\in G", color=theory_color, font_size=self.FS+10).shift(1.5*UP)
        example = MathTex(r"\forall_{w_k, w_l\in E_n}\quad w_k\cdot w_l &=", 
                          r"e^{\imath 2k\pi/n}\cdot e^{\imath 2l\pi/n}\\",
                          r"&= e^{\imath 2 (k+l) \pi /n}\\",
                          r"k+l\in\mathbb{Z}",
                          color=example_color, font_size=self.FS+10).shift(0.5*DOWN)
        vgr = VGroup(theory, example).shift(hor_position)

        self.play(AnimationGroup(*[Write(theory), *[Write(example[i]) for i in range(4)]], lag_ratio=1.5))

        temp_plane_vgr = self.animation_to_0_axiom(plane_vgr[0])

        self.play(Circumscribe(example, color=theory_color, fade_out=True, run_time=2, buff=0.3))
        self.play(FadeOut(vgr), FadeOut(temp_plane_vgr))

    def animation_to_0_axiom(self, plane:PolarPlane) -> VGroup:
        z = (1, 2*5/13*PI)
        w = (1, 2*10/13*PI)
        z_point = Dot(plane.polar_to_point(*z), color=COLOR_1, radius=0.08).set_z_index(2)
        w_point = Dot(plane.polar_to_point(*w), color=COLOR_1, radius=0.08).set_z_index(2)
        z_w_point = Dot(plane.polar_to_point(1, z[1]+w[1]), color=COLOR_1, radius=0.08).set_z_index(2)

        z_label = MathTex(r"w_k", font_size=self.FS).next_to(z_point, 0.5*UL)
        w_label = MathTex(r"w_l", font_size=self.FS).next_to(w_point, 0.5*DR)
        z_w_label = MathTex(r"w_k\cdot w_l", font_size=self.FS).next_to(z_w_point, 0.2*UR)

        self.play(AnimationGroup(*[Create(VGroup(z_point, z_label)), 
                                   Create(VGroup(w_point, w_label)), 
                                   Create(VGroup(z_w_point, z_w_label))], lag_ratio=1.25))


        return VGroup(z_point, w_point, z_w_point, z_label, w_label, z_w_label)

        


    # manage 1 axiom - associativity
    def check_1_axiom(self, theory_color:ManimColor, example_color:ManimColor, plane_vgr:VGroup, hor_position:Vector=ORIGIN) -> None:
        theory = MathTex(r"\forall_{a,b,c\in G}\quad (a*b)*c = a*(b*c)", color=theory_color, font_size=self.FS+10).shift(2*UP)
        example = MathTex(r"(w_k\cdot w_l)\cdot w_m &=", 
                          r"(e^{\imath 2k\pi/n}\cdot e^{\imath 2l\pi/n})\cdot e^{\imath 2m\pi/n} \\", 
                          r"&= e^{\imath 2 (k+l) \pi /n}\cdot e^{\imath 2m\pi /n} \\",
                          r"&= e^{\imath 2 ((k+l)+m) \pi /n} \\", 
                          r"&= e^{\imath 2 (k+(l+m)) \pi /n} \\",
                          r"&= e^{\imath 2k\pi /n}\cdot e^{\imath 2(k+m)\pi /n} \\",
                          r"&= e^{\imath 2k\pi/n}\cdot (e^{\imath 2l\pi/n}\cdot e^{\imath 2m\pi/n}) \\",
                          r"&= w_k\cdot (w_l\cdot w_m) ", 
                          color=example_color, font_size=self.FS+10).shift(1.3*DOWN)
        example_short = MathTex(r"(w_k\cdot w_l)\cdot w_m &=", 
                          r"w_k\cdot (w_l\cdot w_m)", 
                          color=example_color, font_size=self.FS+10).shift(hor_position+0.5*UP)
        vgr = VGroup(theory, example).shift(hor_position)

        self.play(AnimationGroup(*[Write(theory), *[Write(example[i]) for i in range(8)]], lag_ratio=1.5))
        self.wait()
        self.play(TransformMatchingTex(example, example_short))
        self.play(Circumscribe(example_short, color=theory_color, fade_out=True, run_time=2, buff=0.3))
        self.wait()
        self.play(FadeOut(theory, example_short))




    # manage 2 axiom - identity element
    def check_2_axiom(self, theory_color:ManimColor, example_color:ManimColor, plane_vgr:VGroup, hor_position:Vector=ORIGIN) -> None:
        theory = MathTex(r"\exists_{e\in G}\;\; \forall_{a\in G}\quad a*e=e*a=a", color=theory_color, font_size=self.FS+10).shift(UP)
        example = MathTex(r"w_k\cdot 1 &=",
                          r"1 \cdot w_k = w_k", 
                          color=example_color, font_size=self.FS+10)
        vgr = VGroup(theory, example).shift(hor_position)

        self.play(AnimationGroup(*[Write(theory), *[Write(example[i]) for i in range(2)]], lag_ratio=1.5))
        self.wait()
        self.play(Circumscribe(example, color=theory_color, fade_out=True, run_time=2, buff=0.3))
        self.wait()
        self.play(FadeOut(vgr))



    # manage 3 axiom - inverse element
    def check_3_axiom(self, theory_color:ManimColor, example_color:ManimColor, plane_vgr:VGroup, hor_position:Vector=ORIGIN) -> None:
        theory = MathTex(r"\forall_{a\in G}\;\; \exists_{a^{-1}\in G}\quad a*a^{-1}=a^{-1}*a=e", color=theory_color, font_size=self.FS+10).shift(2*UP)
        example = MathTex(r"w_k\cdot w_l &= 1\\",
                          r"e^{\imath 2k\pi /n}\cdot e^{\imath 2l\pi /n} &= e^{\imath 0\pi /n}\\",
                          r"e^{\imath 2(k+l)\pi /n} &= e^{\imath 0\pi /n}\\",
                          r"2(k+l) &= 0\\",
                          r"l &= -k\\",
                          r"l &= -k+n\\",
                          color=example_color, font_size=self.FS+10).shift(DOWN)
        vgr = VGroup(theory, example).shift(hor_position)

        self.play(AnimationGroup(*[Write(theory), *[Write(example[i]) for i in range(6)]], lag_ratio=1.5))

        temp_plane_vgr = self.animation_to_3_axiom(plane_vgr[0])

        self.play(Circumscribe(example, color=theory_color, fade_out=True, run_time=2, buff=0.3))
        self.play(FadeOut(vgr), FadeOut(temp_plane_vgr))
    

    def animation_to_3_axiom(self, plane:PolarPlane) -> VGroup:
        z = (1, 2*4/13*PI)
        w = (1, -2*4/13*PI)
        z_point = Dot(plane.polar_to_point(*z), color=COLOR_1, radius=0.08).set_z_index(2)
        w_point = Dot(plane.polar_to_point(*w), color=COLOR_1, radius=0.08).set_z_index(2)
        z_w_point = Dot(plane.polar_to_point(1, z[1]+w[1]), color=COLOR_1, radius=0.08).set_z_index(2)

        z_label = MathTex(r"w_k", font_size=self.FS).next_to(z_point, 0.5*UL)
        w_label = MathTex(r"w_l=w_{-k+n}", font_size=self.FS).next_to(w_point, 0.5*DL)
        z_w_label = MathTex(r"w_k\cdot w_l=1", font_size=self.FS).next_to(z_w_point, 0.2*UR)

        self.play(AnimationGroup(*[Create(VGroup(z_point, z_label)), 
                                   Create(VGroup(w_point, w_label)), 
                                   Create(VGroup(z_w_point, z_w_label))], lag_ratio=1.25))


        return VGroup(z_point, w_point, z_w_point, z_label, w_label, z_w_label)






