from imports import *

class S11_ProblemSolver(MyScene):  # 11th scene
    def construct(self):
        self.FS = 35
        self.wait(6)

        self.k_color = COLOR_1
        self.n_color = COLOR_2
        
        n_text = self.n_assumption()
        k_text, if_equal_text = self.further_assumptions()
        self.set_colors(n_text, k_text, if_equal_text)

        self.intro_to_solution_2_base_cases()
        self.intro_to_solution_hit_1_ends_circle()
        implication_to_not_zn = self.solution_part_1()
        rel_prime, not_rel_prime = self.solution_part_2(implication_to_not_zn)
        
        vgr = VGroup(n_text, k_text, if_equal_text, rel_prime, not_rel_prime)
        self.clear_screen(vgr, color=COLOR_1)
        self.wait()


    def n_assumption(self) -> MathTex:

        n_text = MathTex(r"n\geqslant 2")
        self.play(Write(n_text))
        self.wait(3)

        e1_group_text = MathTex(r"E_1 = \{ 1 \}").next_to(n_text, 1.5*DOWN)
        self.play(Write(e1_group_text))
        self.wait(2)
        self.play(Unwrite(e1_group_text))

        self.play(n_text.animate.to_edge(UL))

        return n_text
    
    def further_assumptions(self):

        k_text = MathTex(r"k \in \mathbb{Z}_n")
        self.play(Write(k_text))
        self.play(k_text.animate.to_edge(UR))

        if_equal = MathTex(r"\langle k \rangle \overset{?}{=} \mathbb{Z}_n")
        self.play(Write(if_equal))
        self.play(if_equal.animate.to_edge(UP))

        return k_text, if_equal
    
    def set_colors(self, n_text, k_text, if_equal_text):

        self.set_color_method(n_text, [(0,0)], self.n_color)
        self.set_color_method(k_text, [(0,0)], self.k_color)
        self.set_color_method(if_equal_text, [(0,-1)], self.n_color)
        self.set_color_method(if_equal_text, [(0,1)], self.k_color)
    
    
    def intro_to_solution_2_base_cases(self):
        
        m_text = MathTex(r"m\in\mathbb{Z}_n").shift(2*UP+4*RIGHT)
        self.set_color_method(m_text, [(0,-1)], self.n_color)
        self.wait()
        self.play(Write(m_text))

        l_case = MathTex(r"k^m =", r"\underbrace{(k+k+...+k)}_{m \text{ times}} \text{ mod } n =", r"k\cdot m \text{ mod } n")
        l_case_1 = MathTex(r"k^m =", r"k\cdot m \text{ mod } n")
        self.set_color_method(l_case, [(1,-2), (2,-1)], self.n_color)
        self.set_color_method(l_case, [(0,0), (1,1), (1,3), (1,9), (2,0)], self.k_color)
        self.set_color_method(l_case_1, [(1,-1)], self.n_color)
        self.set_color_method(l_case_1, [(0,0), (1,0)], self.k_color)
        self.wait(3)
        self.play(AnimationGroup(*[Write(l_case[i]) for i in range(3)], lag_ratio=1))
        self.wait(4)
        self.play(TransformMatchingTex(l_case, l_case_1))
        self.play(Circumscribe(l_case_1, color=GREY_B, fade_out=True, buff=MED_SMALL_BUFF))
        self.wait()
        self.play(FadeOut(l_case_1))

        self.play(FadeOut(m_text))


    def intro_to_solution_hit_1_ends_circle(self):

        boxes = self.get_zn_boxes_group(6, font_size=self.FS*4).shift(DOWN)

        self.play(Create(boxes))

        self.wait()
        self.add_zn_boxes_animation(boxes, 2, 18, step=2, color=COLOR_1)
        # self.add_zn_boxes_animation(boxes, 0, 4, step=2, color=COLOR_1) 

        self.wait(1)
        self.play(FadeOut(boxes), run_time=2)


    def solution_part_1(self):

        m_text = MathTex(r"m\in\mathbb{Z}_n").shift(2*UP+4*RIGHT)
        self.set_color_method(m_text, [(0,-1)], self.n_color)
        self.play(Write(m_text))

        k_text = MathTex(r"k^m = 0", r"= n\cdot l \text{ mod } n")
        self.set_color_method(k_text, [(0,0)], self.k_color)
        self.set_color_method(k_text, [(1,1), (1,-1)], self.n_color)
        self.play(AnimationGroup(*[Write(p) for p in k_text], lag_ratio=1))

        self.play(k_text.animate.shift(UP))
        self.wait(9)

        implication_to_not_zn_questioned = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0\quad", r"\overset{?}{\implies}", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_questioned, [(0,8), (2,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_questioned, [(0,7), (2,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_questioned[0]), run_time=2)
        self.wait(2)
        self.play(Write(implication_to_not_zn_questioned[1]))
        self.play(Write(implication_to_not_zn_questioned[2]))
        self.wait(4)

        implication_to_not_zn = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0\quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn, [(0,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn, [(0,7), (-1,-1)], self.n_color)

        implication_to_not_zn_expl = MathTex(r"b\in\mathbb{N} \;\land\; b<n \;\land\; k^b=0", r"\quad\implies\quad |\langle k \rangle| \leqslant b < n = |\mathbb{Z}_n|\\", r"\implies \langle k \rangle \neq \mathbb{Z}_n ").shift(1.5*DOWN)
        self.set_color_method(implication_to_not_zn_expl, [(0,8), (1,4), (2,3)], self.k_color)
        self.set_color_method(implication_to_not_zn_expl, [(0,6), (1,10), (1,14), (2,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_expl[0], run_time=1.5))
        self.wait(5)
        self.play(Write(implication_to_not_zn_expl[1]))
        self.wait(3)
        self.play(Write(implication_to_not_zn_expl[2]))
        self.wait(2)
        self.play(FadeOut(implication_to_not_zn_expl))

        self.play(TransformMatchingTex(implication_to_not_zn_questioned, implication_to_not_zn))
        self.wait()
        self.play(FadeOut(k_text), FadeOut(m_text))

        implication_to_not_zn_with_b = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0\quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_with_b, [(0,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_with_b, [(0,7), (-1,-1)], self.n_color)
        self.play(TransformMatchingTex(implication_to_not_zn, implication_to_not_zn_with_b))

        return implication_to_not_zn_with_b


    def solution_part_2(self, implies_not_zn):

        # 1st part of the proof

        # implication down
        self.implication_down(implies_not_zn)
        # implication up
        self.implication_up()
        # end first part of proof
        self.sum_up_implication()

        # 2nd part of the proof
        self.second_part_proof()


        # show results of the proof
        first_implication = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle = \mathbb{Z}_n").shift(0.5*UP)
        self.set_color_method(first_implication, [(0,6), (2,1)], self.k_color)
        self.set_color_method(first_implication, [(0,4), (2,-1)], self.n_color)

        second_implication = MathTex(r"\gcd(n,k) \neq 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n").shift(0.5*DOWN)
        self.set_color_method(second_implication, [(0,6), (2,1)], self.k_color)
        self.set_color_method(second_implication, [(0,4), (2,-1)], self.n_color)

        self.play(Write(first_implication))
        self.wait(2)
        self.play(Write(second_implication))
        self.wait(4)

        self.play(Circumscribe(VGroup(first_implication, second_implication), color=GREY_B, fade_out=True, buff=MED_SMALL_BUFF))
        self.wait()

        return first_implication, second_implication 

   



    def implication_down(self, text_to_transform) -> None:
        b_smaller_then_n = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0\quad")
        b_smaller_then_n[0][8].set_color(COLOR_1)
        b_smaller_then_n[0][7].set_color(COLOR_2)
        self.play(TransformMatchingTex(text_to_transform, b_smaller_then_n))
        self.play(b_smaller_then_n.animate.shift(1.5*UP))

        self.wait(2)

        not_rel_prime_expl = MathTex(r"k^b &= 0\\", 
                                     r"k\cdot b\mod n", r"&=0\\", 
                                     r"kb &= ln\\", 
                                     r"n&|kb\\", 
                                     r"\gcd(n,k) &\neq 1").shift(0.5*LEFT+DOWN)
        self.set_color_method(not_rel_prime_expl, [(0,0), (1,0), (3,0), (4,2), (5,6)], self.k_color)
        self.set_color_method(not_rel_prime_expl, [(1,-1), (3,-1), (4,0), (5,4)], self.n_color)
        self.play(AnimationGroup(*[Write(not_rel_prime_expl[i]) for i in range(3)], lag_ratio=1))
        self.wait(4)
        self.play(AnimationGroup(*[Write(not_rel_prime_expl[i]) for i in range(3,5)], lag_ratio=3))
        self.wait(6)
        self.play(Write(not_rel_prime_expl[-1]))
        implication_down = MathTex(r"\Downarrow", font_size=100, color=RED_D).shift(5*LEFT).set_z_index(2)
        self.wait(4)
        self.play(Create(implication_down))
        self.wait(2)
        self.play(FadeOut(not_rel_prime_expl[:-1]))
        self.play(implication_down.animate.shift(4*RIGHT+0.5*DOWN))
        implication_up = MathTex(r"\Uparrow", font_size=100, color=GREY_E).shift(RIGHT+0.5*DOWN).set_z_index(1)
        self.wait(7)
        self.play(FadeIn(implication_up))
        self.wait(2)
        self.play(implication_up.animate.shift(LEFT+0.3*UP), implication_down.animate.shift(RIGHT))
        self.wait()
        self.play(Unwrite(b_smaller_then_n), Unwrite(not_rel_prime_expl[-1]), Unwrite(implication_down), Unwrite(implication_up))
        self.wait(4)


    def implication_up(self):
        implications_up = MathTex(r"\gcd(n,k) &= d \neq 1\\",
                                r"n=db,\; b&\in\mathbb{N},\; b<n\\",
                                r"k=da,\; a&\in\mathbb{N},\; a<n\\",
                                r"k^b = kb \;\;&\text{mod}\; n = \\",
                                r"= adb \;\;&\text{mod}\; n = \\",
                                r"= an \;\;&\text{mod}\; n = 0\\",
                                r"\exists_{b\in\mathbb{N},\, b<n}&\; k^b = 0\\").shift(0.5*DOWN)
        self.set_color_method(implications_up, [(0,6), (2,0), (3,0), (3,3), (6,8)], self.k_color)
        self.set_color_method(implications_up, [(0,4), (1,0), (1,11), (2,11), (3,-2), (4,-2), (5,2), (5,-3), (6,7)], self.n_color)
        self.set_color_method(implications_up, [(0,9), (1,2), (2,2), (4,2)], COLOR_3)

        self.write_and_fadeout_implications_up(implications_up)

        implication_down = MathTex(r"\Downarrow", font_size=100, color=RED_D).shift(0.5*DOWN+LEFT).set_z_index(2)
        implication_up = MathTex(r"\Uparrow", font_size=100, color=RED_D).shift(0.5*DOWN+RIGHT).set_z_index(1)

        self.play(Create(implication_down))
        self.wait()
        self.play(Create(implication_up))
        self.play(implication_down.animate.shift(RIGHT), implication_up.animate.shift(LEFT+0.3*UP))

        self.wait(3)
        self.play(Unwrite(implications_up[0]), Unwrite(implications_up[-1]), Unwrite(implication_down), Unwrite(implication_up))

    def write_and_fadeout_implications_up(self, implications):

        self.play(Write(implications[0]))
        self.wait(7)

        self.play(Write(implications[1:3]))
        self.wait(7)

        self.play(Write(implications[3]))
        self.wait(6)

        self.play(Circumscribe(implications[2][:4], color=RED_D), Circumscribe(implications[3][3], color=RED_D))
        self.play(Write(implications[4]))
        self.play(Circumscribe(implications[1][:4], color=RED_D), Circumscribe(implications[4][2:4], color=RED_D))
        self.wait(2)
        self.play(Write(implications[5]))
        self.wait(6)

        self.play(Write(implications[6]))
        self.wait(2)


        self.play(FadeOut(implications[1:-1]))


    def sum_up_implication(self):

        first_part_end_1_2 = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0\quad", r"\iff", r"\quad\gcd(n,k) \neq 1").shift(0.5*DOWN)
        self.set_color_method(first_part_end_1_2, [(0,8), (2,6)], self.k_color)
        self.set_color_method(first_part_end_1_2, [(0,7), (2,4)], self.n_color)
        first_part_end_3 = MathTex(r"\exists_{b\in\mathbb{N},\, b<n}\; k^b = 0", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n ").shift(UP)
        self.set_color_method(first_part_end_3, [(0,8), (2,1)], self.k_color)
        self.set_color_method(first_part_end_3, [(0,7), (2,-1)], self.n_color)
        not_rel_prime = MathTex(r"\gcd(n,k) \neq 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n").shift(0.5*UP)
        self.set_color_method(not_rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(not_rel_prime, [(0,4), (2,-1)], self.n_color)

        self.wait(2)
        self.play(Write(first_part_end_1_2))
        self.play(Write(first_part_end_3))
        self.wait(5)
        self.play(TransformMatchingTex(VGroup(first_part_end_1_2, first_part_end_3), not_rel_prime))

        self.play(Circumscribe(not_rel_prime, fade_out=True, buff=MED_SMALL_BUFF, color=GREY_B))

        self.wait(2)
        self.play(FadeOut(not_rel_prime))


    def second_part_proof(self):
        rel_prime = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle = \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime, [(0,4), (2,-1)], self.n_color)
        self.play(Write(rel_prime))
        self.wait(14)

        rel_prime_contr = MathTex(r"\gcd(n,k) = 1", r"\quad\land\quad", r"\langle k \rangle \neq \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime_contr, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime_contr, [(0,4), (2,-1)], self.n_color)
        self.play(TransformMatchingTex(rel_prime, rel_prime_contr), run_time=2)
        self.wait(6)


        rel_prime_expl = MathTex(r"a\in\mathbb{N}&,\; a<n\\", 
                                 r"k^a &= 0\\", 
                                 r"ak &= nl\\", 
                                 r"n&|ak\\", 
                                 r"n&|a").shift(DOWN)
        self.set_color_method(rel_prime_expl, [(1,0), (2,1), (3,-1)], self.k_color)
        self.set_color_method(rel_prime_expl, [(0,-1), (2,3), (3,0), (4,0)], self.n_color)
        self.play(AnimationGroup(*[Write(rel_prime_expl[i]) for i in range(3)], lag_ratio=1.8))
        self.wait(3)
        self.play(Write(rel_prime_expl[3]))
        self.wait(7)
        self.play(Write(rel_prime_expl[4]))
        self.wait(5)
        self.play(Circumscribe(rel_prime_expl[0], color=RED_D))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{stmaryrd}")
        lightning = Tex(r"$\lightning$", tex_template=myTemplate, color=RED_D).shift(2.5*DOWN+1.5*RIGHT)
        self.play(Create(lightning))

        self.wait(3)
        self.play(FadeOut(rel_prime_expl, lightning, rel_prime_contr))



    def animation_before_the_arrow(self, boxes, start_box_index, run_time_weight=1):
        if start_box_index == 0 or start_box_index == 2:
            self.play(boxes[start_box_index].animate.set_stroke_color(COLOR_2))


    def get_arrow_from_0_to_2(self, boxes) -> Arc:

        length_between_boxes = boxes[2].get_top() - boxes[0].get_top()
        arc_radius = 0.9*length_between_boxes[0]

        start = boxes[0].get_top() + [0, 0.1, 0]
        end = start + length_between_boxes
        arrow = self.get_and_add_arrow(start, end, radius=-arc_radius, play=False, color=COLOR_1)

        return arrow





    
