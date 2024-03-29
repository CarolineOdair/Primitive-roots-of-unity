from imports import *

class ProblemSolver(MyScene):  # 11th scene
    def construct(self):
        self.FS = 35

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
        self.clear_screen(vgr, color=COLOR_3)
        self.wait(4)


    def n_assumption(self) -> MathTex:

        n_text = MathTex(r"n\geqslant 2")
        self.play(Write(n_text))
        self.wait()

        e1_group_text = MathTex(r"E_1 = \{ w_0 \}").next_to(n_text, 1.5*DOWN)
        self.play(Write(e1_group_text))
        self.wait()
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
        self.play(Write(m_text))

        l_case = MathTex(r"k^m =", r"\underbrace{(k+k+...+k)}_{m \text{ times}} \text{ mod } n =", r"k\cdot m \text{ mod } n")
        l_case_1 = MathTex(r"k^m =", r"k\cdot m \text{ mod } n")
        self.set_color_method(l_case, [(1,-2), (2,-1)], self.n_color)
        self.set_color_method(l_case, [(0,0), (1,1), (1,3), (1,9), (2,0)], self.k_color)
        self.set_color_method(l_case_1, [(1,-1)], self.n_color)
        self.set_color_method(l_case_1, [(0,0), (1,0)], self.k_color)
        self.play(Write(l_case))
        self.wait()
        self.play(TransformMatchingTex(l_case, l_case_1))
        self.play(Circumscribe(l_case_1, color=COLOR_3, fade_out=True, buff=MED_SMALL_BUFF))
        self.wait()
        self.play(FadeOut(l_case_1))

        k = 0
        case_0 = MathTex(rf"k = {k}").shift(1.5*UP)
        case_1 = MathTex(rf"{k}^m = {k}")
        self.set_color_method(case_0, [(0,0)], self.k_color)
        self.play(Write(case_0))
        self.play(Write(case_1))
        self.wait()
        self.play(Unwrite(case_0), Unwrite(case_1))

        k = 1
        case_0 = MathTex(rf"k = {k}").shift(1.5*UP)
        case_1 = MathTex(rf"{k}^m = m \text{{ mod }} n")
        self.set_color_method(case_0, [(0,0)], self.k_color)
        self.set_color_method(case_1, [(0,-1)], self.n_color)
        self.play(Write(case_0))
        self.play(Write(case_1))
        self.wait()
        self.play(Unwrite(case_0), Unwrite(case_1))

        self.play(FadeOut(m_text))


    def intro_to_solution_hit_1_ends_circle(self):

        boxes_0 = self.get_zn_boxes_group(6, relative_position=(ORIGIN, 0), font_size=self.FS*4)
        boxes_1 = self.get_zn_boxes_group(6, relative_position=(ORIGIN, 2*DOWN), font_size=self.FS*4)

        self.play(Create(boxes_0))
        self.play(Create(boxes_1))

        self.add_zn_boxes_animation(boxes_0, 2, 4, step=2)

        self.play(boxes_1[0].animate.set_stroke_color(COLOR_2))
        self.play(boxes_0[0].animate.set_fill(COLOR_2, opacity=0.2), boxes_1[0].animate.set_fill(COLOR_2, opacity=0.2))

        arrow_0 = self.get_arrow_from_0_to_2(boxes_0)
        arrow_1 = self.get_arrow_from_0_to_2(boxes_1)

        self.play(Create(arrow_0), Create(arrow_1))

        self.wait(1)
        self.play(*[FadeOut(el) for el in [arrow_0, arrow_1, boxes_0, boxes_1]], run_time=5)


    def solution_part_1(self):

        m_text = MathTex(r"m\in\mathbb{Z}_n").shift(2*UP+4*RIGHT)
        self.set_color_method(m_text, [(0,-1)], self.n_color)
        self.play(Write(m_text))

        k_text = MathTex(r"k^m = 0", r"= n\cdot l \text{ mod } n")
        self.set_color_method(k_text, [(0,0)], self.k_color)
        self.set_color_method(k_text, [(1,1), (1,-1)], self.n_color)
        self.play(AnimationGroup(*[Write(p) for p in k_text], lag_ratio=1))

        self.play(k_text.animate.shift(UP))

        implication_to_not_zn_questioned = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"=b", r"< n \quad", r"\overset{?}{\implies}", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_questioned, [(0,8), (4,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_questioned, [(2,-1), (4,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_questioned))

        implication_to_not_zn = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"< n \quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn, [(0,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn, [(1,-1), (-1,-1)], self.n_color)

        implication_to_not_zn_expl = MathTex(r"b\in\mathbb{N} \;\land\; b<n \;\land\; k^b=0 \quad\implies\quad |\langle k \rangle| = b < n = |\mathbb{Z}_n|\\ \implies \langle k \rangle \neq \mathbb{Z}_n ").shift(1.5*DOWN)
        self.set_color_method(implication_to_not_zn_expl, [(0,8), (0,16), (0,31)], self.k_color)
        self.set_color_method(implication_to_not_zn_expl, [(0,6), (0,22), (0,26), (0,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_expl))
        self.wait()
        self.play(FadeOut(implication_to_not_zn_expl))

        self.play(TransformMatchingTex(implication_to_not_zn_questioned, implication_to_not_zn))

        # implication_to_zn = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \} = n \quad\implies\quad \langle k \rangle = \mathbb{Z}_n ").shift(DOWN)
        # self.set_color_method(implication_to_zn, [(0,8), (0,18)], self.k_color)
        # self.set_color_method(implication_to_zn, [(0,14), (0,-1)], self.n_color)
        # self.play(Write(implication_to_zn))

        # implication_to_zn_expl = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \} = n \quad\implies\quad |\langle k \rangle| = n").shift(2*DOWN)
        # self.set_color_method(implication_to_zn_expl, [(0,8), (0,19)], self.k_color)
        # self.set_color_method(implication_to_zn_expl, [(0,14), (0,-1)], self.n_color)
        # self.play(Write(implication_to_zn_expl))
        # self.wait()
        # self.play(FadeOut(implication_to_zn_expl))

        # implication_false = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \} > n \quad").shift(2*DOWN)
        # self.set_color_method(implication_false, [(0,8)  ], self.k_color)
        # self.set_color_method(implication_false, [(0,-1)], self.n_color)
        # self.play(Write(implication_false))
        
        # implication_false_expl = MathTex(r"k^n = k\cdot n \text{ mod } n = 0").shift(3*DOWN)
        # self.set_color_method(implication_false_expl, [(0,0), (0,3)], self.k_color)
        # self.set_color_method(implication_false_expl, [(0,1), (0,5), (0,10)], self.n_color)
        # self.play(Write(implication_false_expl))
        # cross = Cross(mobject=implication_false)
        # self.play(Create(cross))
        # self.play(FadeOut(cross))
        # self.wait()
        # self.play(FadeOut(implication_false_expl))
        # self.play(FadeOut(implication_false))


        self.wait()
        self.play(FadeOut(k_text), FadeOut(m_text))


        implication_to_not_zn_with_b = MathTex(r"b=", r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"< n \quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_with_b, [(1,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_with_b, [(2,-1), (-1,-1)], self.n_color)
        self.play(TransformMatchingTex(implication_to_not_zn, implication_to_not_zn_with_b))

        # implication_to_zn_with_b = MathTex(r"b=", r"\min\{ c\in\mathbb{N}: k^c=0 \} = n \quad\implies\quad \langle k \rangle = \mathbb{Z}_n ").shift(DOWN)
        # self.set_color_method(implication_to_zn_with_b, [(1,8), (1,18)], self.k_color)
        # self.set_color_method(implication_to_zn_with_b, [(1,14), (1,-1)], self.n_color)
        # self.play(TransformMatchingTex(implication_to_zn, implication_to_zn_with_b))


        return implication_to_not_zn_with_b


    def solution_part_2(self, implies_not_zn):

        self.play(implies_not_zn.animate.shift(1.5*UP))

        not_rel_prime_expl = MathTex(r"k^b", r"=k\cdot &b", r"=l\cdot n\\", r"n|&kb\\", r"\gcd(n,&k) \neq 1")
        self.set_color_method(not_rel_prime_expl, [(0,0), (1,1), (3,2), (4,6)], self.k_color)
        self.set_color_method(not_rel_prime_expl, [(2,-1), (3,0), (4,4)], self.n_color)
        self.play(AnimationGroup(*[Write(p) for p in not_rel_prime_expl], lag_ratio=1))
        self.play(FadeOut(not_rel_prime_expl))

        not_rel_prime = MathTex(r"\gcd(n,k) \neq 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n")
        self.set_color_method(not_rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(not_rel_prime, [(0,4), (2,-1)], self.n_color)
        self.play(Write(not_rel_prime))
        self.play(Circumscribe(not_rel_prime, fade_out=True, color=COLOR_3, buff=MED_SMALL_BUFF))

        self.wait(2)
        self.play(FadeOut(implies_not_zn), FadeOut(not_rel_prime))



        # now we want to show that only k relatively prime to n can generate Z_n group
        rel_prime = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle = \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime, [(0,4), (2,-1)], self.n_color)
        self.play(Write(rel_prime))

        rel_prime_contr = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime_contr, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime_contr, [(0,4), (2,-1)], self.n_color)
        self.play(TransformMatchingTex(rel_prime, rel_prime_contr))

        rel_prime_expl = MathTex(r"a\in\mathbb{N}&,\; a<n\\", r"k^a &= 0\\", r"a\cdot k &= n\cdot l\\", r"n&|ak\\", r"n&|a").shift(DOWN)
        self.set_color_method(rel_prime_expl, [(1,0), (2,2), (3,-1)], self.k_color)
        self.set_color_method(rel_prime_expl, [(0,-1), (2,4), (3,0), (4,0)], self.n_color)
        self.play(AnimationGroup(*[Write(p) for p in rel_prime_expl], lag_ratio=1))
        self.wait()
        self.play(FadeOut(rel_prime_expl))

        self.play(TransformMatchingTex(rel_prime_contr, rel_prime))
        self.play(Circumscribe(rel_prime, fade_out=True, color=COLOR_3, buff=MED_SMALL_BUFF))

        self.play(Write(not_rel_prime))

        return rel_prime, not_rel_prime










    def animation_before_the_arrow(self, boxes, start_box_index):
        if start_box_index == 0 or start_box_index == 2:
            self.play(boxes[start_box_index].animate.set_stroke_color(COLOR_2))


    def get_arrow_from_0_to_2(self, boxes) -> Arc:

        length_between_boxes = boxes[2].get_top() - boxes[0].get_top()
        arc_radius = 0.9*length_between_boxes[0]

        start = boxes[0].get_top() + [0, 0.1, 0]
        end = start + length_between_boxes
        arrow = self.get_and_add_arrow(start, end, radius=-arc_radius, play=False, color=COLOR_1)

        return arrow





    
