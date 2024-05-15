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

        implication_to_not_zn_questioned = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"=b", r"< n \quad", r"\overset{?}{\implies}", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_questioned, [(0,8), (4,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_questioned, [(2,-1), (4,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_questioned[:3]))
        self.wait()
        self.play(Write(implication_to_not_zn_questioned[3]))
        self.play(Write(implication_to_not_zn_questioned[4:]))
        self.wait(3)

        implication_to_not_zn = MathTex(r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"< n \quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn, [(0,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn, [(1,-1), (-1,-1)], self.n_color)

        implication_to_not_zn_expl = MathTex(r"b\in\mathbb{N} \;\land\; b<n \;\land\; k^b=0", r"\quad\implies\quad |\langle k \rangle| = b < n = |\mathbb{Z}_n|\\", r"\implies \langle k \rangle \neq \mathbb{Z}_n ").shift(1.5*DOWN)
        self.set_color_method(implication_to_not_zn_expl, [(0,8), (1,4), (2,3)], self.k_color)
        self.set_color_method(implication_to_not_zn_expl, [(0,6), (1,10), (1,14), (2,-1)], self.n_color)
        self.play(Write(implication_to_not_zn_expl[0]))
        self.wait(2)
        self.play(Write(implication_to_not_zn_expl[1]))
        self.wait(5)
        self.play(Write(implication_to_not_zn_expl[2]))
        self.wait(6)
        self.play(FadeOut(implication_to_not_zn_expl))

        self.play(TransformMatchingTex(implication_to_not_zn_questioned, implication_to_not_zn))
        self.wait()
        self.play(FadeOut(k_text), FadeOut(m_text))

        implication_to_not_zn_with_b = MathTex(r"b=", r"\min\{ c\in\mathbb{N}: k^c=0 \}", r"< n \quad", r"\implies", r"\quad \langle k \rangle \neq \mathbb{Z}_n ")
        self.set_color_method(implication_to_not_zn_with_b, [(1,8), (-1,1)], self.k_color)
        self.set_color_method(implication_to_not_zn_with_b, [(2,-1), (-1,-1)], self.n_color)
        self.play(TransformMatchingTex(implication_to_not_zn, implication_to_not_zn_with_b))

        return implication_to_not_zn_with_b


    def solution_part_2(self, implies_not_zn):

        self.play(implies_not_zn.animate.shift(1.5*UP))
        self.wait(2) # +1

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
        self.wait(2)
        self.play(FadeOut(not_rel_prime_expl))

        not_rel_prime = MathTex(r"\gcd(n,k) \neq 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n")
        self.set_color_method(not_rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(not_rel_prime, [(0,4), (2,-1)], self.n_color)
        self.play(Write(not_rel_prime))
        self.play(Circumscribe(not_rel_prime, fade_out=True, buff=MED_SMALL_BUFF, color=GREY_B))

        self.wait(2)
        self.play(FadeOut(implies_not_zn), FadeOut(not_rel_prime))


        # now we want to show that only k relatively prime to n can generate Z_n group
        rel_prime = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle = \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime, [(0,4), (2,-1)], self.n_color)
        self.play(Write(rel_prime))
        self.wait(14)

        rel_prime_contr = MathTex(r"\gcd(n,k) = 1", r"\quad\implies\quad", r"\langle k \rangle \neq \mathbb{Z}_n").shift(1.5*UP)
        self.set_color_method(rel_prime_contr, [(0,6), (2,1)], self.k_color)
        self.set_color_method(rel_prime_contr, [(0,4), (2,-1)], self.n_color)
        self.play(TransformMatchingTex(rel_prime, rel_prime_contr), run_time=2)
        self.wait(12)

        self.play(Write(not_rel_prime))
        self.wait(17)
        box = SurroundingRectangle(VGroup(rel_prime_contr, not_rel_prime), color=RED_D, buff=MED_LARGE_BUFF, corner_radius=0.1)
        self.play(FadeIn(box), run_time=2)
        self.wait(3)
        self.play(FadeOut(not_rel_prime, box))
        self.wait(6)



        rel_prime_expl = MathTex(r"a\in\mathbb{N}&,\; a<n\\", 
                                 r"k^a &= 0\\", 
                                 r"ak &= nl\\", 
                                 r"n&|ak\\", 
                                 r"n&|a").shift(DOWN)
        self.set_color_method(rel_prime_expl, [(1,0), (2,1), (3,-1)], self.k_color)
        self.set_color_method(rel_prime_expl, [(0,-1), (2,4), (3,0), (4,0)], self.n_color)
        self.play(AnimationGroup(*[Write(rel_prime_expl[i]) for i in range(4)], lag_ratio=1.8))
        self.wait(7)
        self.play(Write(rel_prime_expl[4]))
        self.wait(5)
        self.play(Circumscribe(rel_prime_expl[0], color=RED_D))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{stmaryrd}")
        lightning = Tex(r"$\lightning$", tex_template=myTemplate, color=RED_D).shift(2.5*DOWN+1.5*RIGHT)
        self.play(Create(lightning))

        self.wait(3)
        self.play(FadeOut(rel_prime_expl, lightning))

        self.play(TransformMatchingTex(rel_prime_contr, rel_prime))
        self.wait()
        self.play(Circumscribe(rel_prime, fade_out=True, color=GREY_B, buff=MED_SMALL_BUFF))
        self.wait()

        self.play(Write(not_rel_prime))
        self.wait(2)

        return rel_prime, not_rel_prime


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





    
