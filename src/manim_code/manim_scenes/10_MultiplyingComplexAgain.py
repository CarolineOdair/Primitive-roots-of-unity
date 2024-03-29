from imports import *


class ShowComplexAndZnSimilarity(MyScene):  # 10th scene
    def construct(self):
        self.FS = 35

        equation_on_top = self.multiply_complex_part()

        self.manage_groups_animations()

        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(5)


    def multiply_complex_part(self) -> MathTex:
        n_color = COLOR_3
        m_color = COLOR_2
        k_color = COLOR_1

        en_group_text, zn_group_text = self.get_groups_text(n_color)        
        roots = self.get_wk_wl_formula(k_color, m_color, n_color)
        formula = self.get_expl_formula(k_color, m_color, n_color)
        end_formula = self.get_end_expl_formula(k_color, m_color, n_color)
        iso_symbol = MathTex(r"\simeq")

        self.play(Write(en_group_text))
        self.play(AnimationGroup(*[Write(roots), *[Write(formula[i]) for i in range(5)]], lag_ratio=1.5))
        self.wait()
        self.play(FadeOut(formula[1:-1]))
        self.play(Unwrite(VGroup(formula[0], formula[-1])))
        self.play(Write(end_formula))
        self.play(en_group_text.animate.next_to(roots, 2*UP).shift(1.2*LEFT))
        self.play(Write(zn_group_text.next_to(roots, 2*UP).shift(1.5*RIGHT)))
        
        coordinates = (en_group_text.get_right() + zn_group_text.get_left())/2
        self.play(Write(iso_symbol.move_to(coordinates)))

        self.play(FadeOut(en_group_text, iso_symbol, zn_group_text, roots))
        self.play(end_formula.animate.to_edge(UP))

        return end_formula


    def get_groups_text(self, n_color):
        en_group_text = MathTex(r"(E_n, \cdot)").to_edge(UP)
        en_group_text[0][2].set_color(n_color)

        zn_group_text = MathTex(r"(\mathbb{Z}_n, +_n)")
        zn_group_text[0][2].set_color(n_color)
        zn_group_text[0][-2].set_color(n_color)

        return en_group_text, zn_group_text

    def get_wk_wl_formula(self, k_color, m_color, n_color) -> MathTex:
        roots = MathTex(r"w_k,w_m\in E_n\qquad k,m\in\mathbb{Z}_n", font_size=self.FS+10).shift(1.5*UP)
        self.set_color_method(roots, [(0,1),(0,8)], k_color)
        self.set_color_method(roots, [(0,4),(0,-4)], m_color)
        self.set_color_method(roots, [(0,7),(0,-1)], n_color)

        return roots
    
    def get_expl_formula(self, k_color, m_color, n_color) -> MathTex:
        formula = MathTex(r"w_k \cdot w_m &=", 
                          r"e^{\imath 2\pi \frac{k}{n}} \cdot e^{\imath 2\pi \frac{m}{n}}=",
                          r"e^{\imath 2\pi \frac{k+m}{n}}=\\",
                          r"&= e^{\imath 2\pi \frac{k+_nm}{n}}=",
                          r"w_{k+_nm}",
                          font_size=self.FS+20).shift(0.5*DOWN)
        
        self.set_color_method(formula, [(0,1),(1,4),(2,4),(3,5),(4,1)], k_color)
        self.set_color_method(formula, [(0,4),(1,12),(2,6),(3,8),(4,-1)], m_color)
        self.set_color_method(formula, [(1,6),(1,14),(2,-2),(3,-5),(3,-2),(4,3)], n_color)

        return formula
    
    def get_end_expl_formula(self, k_color, m_color, n_color) -> MathTex:
        formula = MathTex(r"w_k \cdot w_m =", r"w_{k+_nm}", font_size=self.FS+20)
        self.set_color_method(formula, [(0,1),(1,1)], k_color)
        self.set_color_method(formula, [(0,4),(1,-1)], m_color)
        self.set_color_method(formula, [(1,3)], n_color)

        return formula

    def manage_groups_animations(self):
        plane_group = self.add_plane_on_down_left(6)
        boxes = self.get_zn_boxes_group(6, font_size=self.FS*5, height_to_width_ratio=0.7, boxes_color=COLOR_2, numbers_color=WHITE)
        self.boxes_settings(boxes)
        self.play(Create(boxes))

        en_expression = MathTex(r"(w_2)^3 = w_2 \cdot w_2 \cdot w_2").shift(2*UP+3*LEFT)
        zn_expression = MathTex(r"2^3 = 2+_6 2+_6 2 ").shift(2*UP+3*RIGHT)
        self.play(Write(en_expression), Write(zn_expression))

        self.animate_about_primitives(plane_group[0], 6, 2, num_of_steps=2, if_fade=False)
        self.add_zn_boxes_animation(boxes, 2, 4, color=COLOR_1, step=2, stroke_color=COLOR_1)

        self.add_last_expressions_and_frameboxes(en_expression, zn_expression)


    def add_last_expressions_and_frameboxes(self, en_prev, zn_prev):

        en_expression_1 = MathTex(r"(w_2)^3 = w_2 \cdot w_2 \cdot w_2", r"= w_0").shift(2*UP+3*LEFT)
        zn_expression_1 = MathTex(r"2^3 = 2+_6 2+_6 2", r"=0").shift(2*UP+3*RIGHT)
        self.play(TransformMatchingTex(en_prev, en_expression_1), TransformMatchingTex(zn_prev, zn_expression_1))
    
        frameboxes = [
            [en_expression_1[0][2], zn_expression_1[0][0]],
            [en_expression_1[0][4], zn_expression_1[0][1]],
            [en_expression_1[1][2], zn_expression_1[1][1]]
        ]

        for framebox in frameboxes:
            fr_1 = SurroundingRectangle(framebox[0], buff=.1, color=COLOR_3)
            fr_2 = SurroundingRectangle(framebox[1], buff=.1, color=COLOR_3)

            self.play(Create(fr_1), Create(fr_2))


    def animation_before_the_arrow(self, boxes, start_box_index):
        if start_box_index == 2:
            self.play(boxes[start_box_index].animate.set_stroke_color(COLOR_1))


    # add plane on the left of the screen
    def add_plane_on_down_left(self, n:int) -> VGroup:

        plane = self.add_plane(azimuth_step=1, size=4, radius_max=1.5, radius_step=0.5).to_edge(LEFT).shift(DOWN)
        z_point, z_n_group = self.get_point_and_n_roots((1,0), n, plane, roots_color=COLOR_2, dot_radius=0.07)

        gr = VGroup(plane, z_n_group)
        self.play(Create(gr), run_time=4)
        self.wait()

        for index, pos in zip(range(len(z_n_group)), [UR, UR, UL, UL, DL, DR]):
            label = MathTex(r"w_", rf"{index}").next_to(z_n_group[index], 0.5*pos)
            self.play(Write(label))

        return gr
    
    def boxes_settings(self, boxes):
        boxes.width = boxes.width/2
        buff = boxes[1].get_left() - boxes[0].get_right()
        boxes.to_edge(RIGHT, buff=buff/2).shift(DOWN)

        # It's horrible way of solving the problem, but I do not know Manim enough to be able to solve the problem with the arrow differently
        rectangle = Rectangle(height=boxes.height*4, width=boxes.width/3, color=NAVY_BLUE).next_to(boxes, LEFT, buff=buff)
        rectangle.set_fill(NAVY_BLUE, opacity=1)
        boxes.z_index = 0
        rectangle.z_index = 0.1

        self.add(rectangle)
        


    def animate_about_primitives(self, plane, n:int, a:int, if_fade:bool=True, num_of_steps:int=None) -> None:

        if num_of_steps is None:
            num_of_steps = n-1
        c = COLOR_1
        z = (1, a/n*2*PI)
        z_dot = Dot(plane.polar_to_point(*z), color=c, radius=0.08).set_z_index(2)

        num = [z]
        points = [plane.polar_to_point(*z)]
        dots = [z_dot]

        self.play(Create(dots[-1]))


        for i in range(num_of_steps):
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

        if if_fade:
            self.play(FadeOut(*dots))

