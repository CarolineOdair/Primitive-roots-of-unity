from imports import *

class S6_IntroGroup(MovingCameraScene):  # 6th scene
    # Some functions are copied from MyScene class
    # They have to be defined here because IntroGroupDef class 
    # inherits from MovingCameraScene, not MyScene
    def construct(self):

        self.FS = 35
        self.camera_shift = 4*DOWN

        ######    axioms    ######
        group_notation = self.add_group_notation()
        axioms_vgroup = self.add_group_axioms()
        self.wait(3)

        ######    integers example    ######
        self.manage_integers_example(axioms_vgroup)

        # ######    Z_n example    ######
        mobj_on_screen = self.manage_zn_group_def()
        self.wait(1)
        self.clear_screen(mobj_on_screen, COLOR_1)
        self.wait()

    def clear_screen(self, mobjects_on_screen, color=COLOR_1) -> None:

        last_dot = Dot(self.camera.frame_center, color=color)
        self.play(ReplacementTransform(mobjects_on_screen, last_dot))
        self.wait(0.5)
        self.play(Uncreate(last_dot))

    def manage_zn_group_def(self):
        # Play animations explaining Z_n group, and Z_8 example in particular
        temp_group_ex = MathTex(r"(\mathbb{Z}_", r"n", r", +_", r"n", r")").shift(DOWN)
        temp_group_ex_8 = MathTex(r"(\mathbb{Z}_", r"8", r", +_", r"8", r")", substrings_to_isolate="8").set_color_by_tex("8", COLOR_1).shift(DOWN)
        zn_set = MathTex(r"\mathbb{Z}_", r"n", r" = \{ 0,1,...,", r"n-1", r"\}").next_to(temp_group_ex, 2*DOWN)
        zn_set_8 = MathTex(r"\mathbb{Z}_", r"8", r" = \{ 0,1,...,", r"7", r"\}", substrings_to_isolate=["8", "7"]).set_color_by_tex("8", COLOR_1).set_color_by_tex("7", COLOR_1).next_to(temp_group_ex, 2*DOWN)
        zn_plus_operation =  MathTex(r"k+_", r"n", r"l = (k+l)\text{ mod }", r"n").next_to(zn_set, DOWN)
        zn_plus_operation_8 =  MathTex(r"k+_", r"8", r"l = (k+l)\text{ mod }", r"8", substrings_to_isolate="8").set_color_by_tex("8", COLOR_1).next_to(zn_set, DOWN)

        zn_list = [temp_group_ex, zn_set, zn_plus_operation]
        z8_list = [temp_group_ex_8, zn_set_8, zn_plus_operation_8]

        self.play(FadeIn(temp_group_ex))
        self.play(self.camera.frame.animate.shift(self.camera_shift))
        self.wait(6)
        self.play(FadeIn(zn_set))
        self.wait(3)
        self.play(FadeIn(zn_plus_operation))
        self.wait(6)

        for prev, cur in zip(zn_list, z8_list):
            self.play(TransformMatchingTex(prev, cur))

        # create boxes with numbers from 0 to 8
        boxes = self.get_zn_boxes_group(8, 0.1, 0.4, 10, self.FS*5, (zn_set, 5*DOWN))
        self.play(Create(boxes))

        # 2 + 3 = 5 
        zn_plus_operation_2_3 =  MathTex(r"2", r"+_", r"8", r"3", r"=", r"(2+3)", r"\text{ mod }", r"8", r"= 5", r"\text{ mod }", r"8", r"=", r"5").next_to(zn_set, DOWN)
        self.play(TransformMatchingTex(zn_plus_operation_8, zn_plus_operation_2_3))
        self.wait(2)
        self.add_zn_boxes_animation(boxes, 2, 3, color=COLOR_2)

        # 5 + 6 = 3
        zn_plus_operation_5_6 =  MathTex(r"5", r"+_", r"8", r"6 = (5+6)", r"\text{ mod }", r"8", r"= 11", r"\text{ mod }", r"8", r"=", r"3").next_to(zn_set, DOWN)
        self.play(TransformMatchingTex(zn_plus_operation_2_3, zn_plus_operation_5_6))
        self.wait(2)
        self.add_zn_boxes_animation(boxes, 5, 6, color=COLOR_2)
        self.wait(2)

        mobjects_on_screen = VGroup(temp_group_ex_8, zn_set_8, zn_plus_operation_5_6, boxes)

        return mobjects_on_screen


        
    def add_zn_boxes_animation(self, boxes:VGroup, start:int, add:int, arc_radius:float=1.5, color=WHITE):

        n = len(boxes)
        start_index = start
        last_arrows = []

        length_between_boxes = boxes.submobjects[1].get_top() - boxes.submobjects[0].get_top()
        
        for plus in range(add):
            if start_index != n-1:
                start_top = boxes.submobjects[start_index % n].get_top() + [0, 0.1, 0]
                next_top = start_top + length_between_boxes
                arrow = self.get_and_add_arrow(start_top, next_top, radius=-arc_radius, play=False, color=color)

                if len(last_arrows) != 0:
                    self.play(Create(arrow), FadeOut(*last_arrows))
                else:
                    self.play(Create(arrow))

                start_index += 1
                last_arrows = [arrow]

            elif start_index == len(boxes)-1:
                start_1_top = boxes.submobjects[start_index % n].get_top() + [0, 0.1, 0]
                next_1_top = start_1_top + length_between_boxes
                arrow_1 = self.get_and_add_arrow(start_1_top, next_1_top, radius=-arc_radius, play=False, color=color)

                next_2_top = boxes.submobjects[0].get_top() + [0, 0.1, 0]
                start_2_top = next_2_top - length_between_boxes
                arrow_2 =  self.get_and_add_arrow(start_2_top, next_2_top, radius=-arc_radius, play=False, color=color)

                if len(last_arrows) != 0:
                    self.play(Create(arrow_1), Create(arrow_2), FadeOut(*last_arrows))
                else:
                    self.play(Create(arrow_1), Create(arrow_2))

                start_index += 1
                last_arrows = [arrow_1, arrow_2]

        self.play(FadeOut(*last_arrows))




    def get_zn_boxes_group(self, n:int, buff_to_width_ratio:float=0.1, height_to_width_ratio:float=0.4,
                           width:float=10, font_size:float=40, relative_position:tuple=(ORIGIN, 0)):
        # Create VGroup of n boxes fitting the width of the screen with numbers from 0 to n-1 

        buff = width * buff_to_width_ratio
        boxes = VGroup(*[
            Rectangle(WHITE, width=width, height=width*height_to_width_ratio).add(Text(str(i), font_size=font_size, color=COLOR_1))
            for i in range(n)
        ])

        boxes.arrange_in_grid(cols=n, buff=buff).next_to(*relative_position)

        # width_of_boxes = n*width+(n-1)*buff
        scale = config.frame_width / (n*(width+buff))
        buff_on_outside = buff*scale/2
        boxes.width = config.frame_width - 2*buff_on_outside

        return boxes





    def manage_integers_example(self, axioms_vgroup):
        # Play animations checking that (Z, +) is a group
        c = COLOR_2

        temp_group_ex = MathTex(r"(\mathbb{Z}, +)").shift(4*RIGHT+0.5*DOWN)
        underline = Underline(temp_group_ex, color=c)
        self.play(FadeIn(temp_group_ex), Create(underline), run_time=3)
        self.wait()

        ######    axiom 0    ######
        ax_0 = axioms_vgroup.submobjects[0]
        ax_0_quantifier = MathTex(r"\forall_{", r"k,l", r"\in\mathbb{Z}}", color=c).shift(1.5*DOWN+4.5*LEFT)
        ax_0_text = MathTex(r"k+l\in\mathbb{Z}", color=c).shift(1.5*DOWN)

        self.play(
            FadeToColor(ax_0, color=COLOR_1),
            Write(ax_0_quantifier), 
            Write(ax_0_text),
            run_time=2
            )
        self.play(FadeToColor(ax_0, color=WHITE))


        ######    axiom 1    ######
        ax_1 = axioms_vgroup.submobjects[1]
        ax_1_quantifier = MathTex(r"\forall_{", r"k,l,m", r"\in\mathbb{Z}}", color=c).shift(1.5*DOWN+4.5*LEFT)
        ax_1_text = MathTex(r"(k+l)+m", r"=", r"k+(l+m)", color=c).shift(1.5*DOWN)
        
        self.play(
            FadeToColor(ax_1, color=COLOR_1),
            TransformMatchingTex(ax_0_quantifier, ax_1_quantifier), 
            TransformMatchingTex(ax_0_text, ax_1_text), 
            run_time=3
            )
        self.wait(6)
        self.play(FadeToColor(ax_1, color=WHITE))

        ######    axiom 2    ######
        ax_2 = axioms_vgroup.submobjects[2]
        ax_2_quantifier = MathTex(r"\forall_{", r"k", r"\in\mathbb{Z}}", color=c).shift(1.5*DOWN+4.5*LEFT)
        ax_2_text = MathTex(r"k+0", r"=", r"0+k", r"=", r"k", color=c).shift(1.5*DOWN)
        
        self.play(
            FadeToColor(ax_2, color=COLOR_1), 
            TransformMatchingTex(ax_1_quantifier, ax_2_quantifier), 
            TransformMatchingTex(ax_1_text, ax_2_text),
            run_time=2
            )
        self.wait()
        self.play(FadeToColor(ax_2, color=WHITE))

        ######    axiom 3    ######
        ax_3 = axioms_vgroup.submobjects[3]
        ax_3_quantifier = MathTex(r"\forall_{", r"k", r"\in\mathbb{Z}}", color=c).shift(1.5*DOWN+4.5*LEFT)
        ax_3_text = MathTex(r"k+(-k)", r"=", r"(-k)+k", r"=", r"0", color=c).shift(1.5*DOWN)
        
        self.play(
            FadeToColor(ax_3, color=COLOR_1), 
            TransformMatchingTex(ax_2_quantifier, ax_3_quantifier), 
            TransformMatchingTex(ax_2_text, ax_3_text),
            run_time=2
            )
        self.wait()
        self.play(FadeToColor(ax_3, color=WHITE))


        self.wait(1)
        self.play(FadeOut(temp_group_ex, underline, ax_3_quantifier, ax_3_text))



    def add_group_axioms(self) -> VGroup:
        # Play writing of group requirements
        # Return VGroup containing all four requirements

        ax_0 = MathTex(r"\forall_{a,b\in G}\quad a*b\in G")  # inner
        ax_1 = MathTex(r"\forall_{a,b,c\in G}\quad (a*b)*c = a*(b*c)")  # Associativity
        ax_2 = MathTex(r"\exists_{e\in G}\;\; \forall_{a\in G}\quad a*e=e*a=a")  # Identity element
        ax_3 = MathTex(r"\forall_{a\in G}\;\; \exists_{a^{-1}\in G}\quad a*a^{-1}=a^{-1}*a=e")  # Inverse element

        axioms_vgroup = VGroup(ax_0, ax_1, ax_2, ax_3).arrange(direction=DOWN, aligned_edge=LEFT).to_edge(UL)
        wait_list = [12, 23, 16.5, 26.5]
        self.wait()
        for i, ax in enumerate(axioms_vgroup):
            self.play(Write(ax), run_time=2)
            self.wait(wait_list[i])

        return axioms_vgroup



    def add_group_notation(self) -> VGroup:
        # Add (G, *) sign and write it's a group
        # Return VGroup containing 2 texes and arc (arrow from text to '(G, *)')

        group_notation = MathTex(r"(G, *)").shift(2.5*UP+4*RIGHT)  # group notation
        group_text = Tex(r"group").shift(1.5*UP+4*RIGHT)

        self.play(Write(group_text), run_time=1.5)
        self.wait(2)
        self.play(Write(group_notation), run_time=1.5)
        self.wait()
        a = self.get_and_add_arrow(1.6*UP+4.8*RIGHT, 2.5*UP+4.8*RIGHT, radius=0.7, color=COLOR_1, tip_length=0.2, tip_width=0.2)
        self.wait(4)

        vgroup = VGroup(group_notation, group_text, a)
        return vgroup



    def get_and_add_arrow(self, start, end, radius:float=2, color=WHITE, tip_length=0.2, tip_width=0.2, play:bool=True):
        # Play creating arc between given points
        # Return arc

        a = ArcBetweenPoints(start, end, radius=radius, color=color)
        a.add_tip(tip_shape=StealthTip, tip_length=tip_length, tip_width=tip_width)

        if play:
            self.play(Create(a))

        return a
