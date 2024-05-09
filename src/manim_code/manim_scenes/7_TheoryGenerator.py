from imports import *


class S7_GeneratorDef(MyScene):  # 7th scene
    def construct(self):
        self.FS = 35

        #####    def of power in group    ###### 
        group_notation = self.add_group_notation()
        power_def = self.add_power_def()
        generator_def = self.add_generator_def()
        self.play(FadeOut(group_notation), generator_def.animate.move_to(group_notation))

        #####    integers example    ######
        self.manage_integers_example()

        #####    z_8 example    ######
        self.play(FadeOut(power_def, generator_def))
        obj_on_screen = self.z_8_example()


        self.clear_screen(obj_to_clear=obj_on_screen, color=COLOR_2)

        self.wait(5)





    def z_8_example(self):
        temp_group_ex_8 = MathTex(r"(\mathbb{Z}_", r"8", r", +_", r"8", r")", substrings_to_isolate="8").set_color_by_tex("8", COLOR_1).to_edge(UP)
        self.play(Write(temp_group_ex_8))
        a_text = MathTex(r"a=", r"2").next_to(temp_group_ex_8, DOWN)
        self.play(Write(a_text))
        
        # create boxes with numbers from 0 to 8
        boxes = self.get_zn_boxes_group(8, 0.1, 0.4, 10, self.FS*5, (a_text, 6*DOWN))
        self.play(Create(boxes))

        # powers of 2
        a = 2
        # boxes = self.manage_power_z_n(8, 2, 10, boxes)
        self.add_zn_boxes_animation(boxes, a, a*5, step=a, color=COLOR_2)
        generator_text = MathTex(r"\langle 2 \rangle = \{ 0, 2, 4, 6 \} \neq \mathbb{Z}_8").next_to(a_text, DOWN)
        self.play(Write(generator_text))

        self.play(boxes.animate.set_stroke_color(WHITE))
        self.play(FadeOut(generator_text))

        # powers of 1
        a=1
        self.play(Transform(a_text, MathTex(r"a=", r"1").next_to(temp_group_ex_8, DOWN)))
        # boxes = self.manage_power_z_n(8, 1, 7, boxes)
        self.add_zn_boxes_animation(boxes, a, a*8, step=a, color=COLOR_2)
        self.play(boxes[0].animate.set_stroke_color(COLOR_2))
        generator_text = MathTex(r"\langle 1 \rangle = \{ 0,1,2,3,4,5,6,7 \} = \mathbb{Z}_8").next_to(a_text, DOWN)
        self.play(Write(generator_text))

        self.play(boxes.animate.set_stroke_color(WHITE))
        self.play(FadeOut(generator_text))

        # powers of 3
        a = 3
        a_text_2 = MathTex(r"a=", r"3").next_to(temp_group_ex_8, DOWN)
        self.play(ReplacementTransform(a_text, a_text_2))
        self.add_zn_boxes_animation(boxes, a, a*7, step=a, color=COLOR_2)
        self.play(boxes[0].animate.set_stroke_color(COLOR_2))
        generator_text = MathTex(r"\langle 3 \rangle = \{ 0,1,2,3,4,5,6,7 \} = \mathbb{Z}_8").next_to(a_text, DOWN)
        self.play(Write(generator_text))

        mobjects_on_screen = VGroup(temp_group_ex_8, generator_text, boxes, a_text_2)
        return mobjects_on_screen


    def animation_before_the_arrow(self, boxes, start_box_index):
        if boxes[start_box_index].get_stroke_color() != COLOR_2:
            self.play(boxes[start_box_index].animate.set_stroke_color(COLOR_2))

    def animation_after_the_arrow(self, boxes, end_box_index):
        if boxes[end_box_index].get_stroke_color() != COLOR_2:
            self.play(boxes[end_box_index].animate.set_stroke_color(COLOR_2))


    def manage_integers_example(self):
        # Play animations showing power examples for 2
        c = COLOR_2
 

        # Animate `(Z, +)`
        temp_group_ex = MathTex(r"(\mathbb{Z}, +)").shift(1.5*UP)
        underline = Underline(temp_group_ex, color=c)
        self.play(FadeIn(temp_group_ex), Create(underline))
        self.wait(2)


        # Animate powers - explanation
        power_ex = [
            r"2^0 = 0",
            r"2^1 = 2^0 + 2 = 0 + 2 = 2",
            r"2^2 = 2^1 + 2 = 2 + 2 = 4",
            r"2^3 = 2^2 + 2 = 4 + 2 = 6",
            r"2^4 = 2^3 + 2 = 6 + 2 = 8"
        ]
        power_ex = [MathTex(*text) for text in power_ex]
        power_ex_group = VGroup(*power_ex).arrange(direction=DOWN).move_to(DOWN)
        wait_list = [7, 3, 1, 1, 1]
        for i, el in enumerate(power_ex_group):
            self.play(Write(el))
            self.wait(wait_list[i])
        self.play(Uncreate(power_ex_group))


        # Animate tables
        power_ex_table = MathTable(
            [[r"\times", r"\times", r"\times", r"\times", "2^0", "2^1" ,"2^2", "2^3", "2^4"],
            [r"\times", r"\times", r"\times", r"\times", 0, 2, 4, 6, 8]],
        ).scale(0.7).move_to(1*DOWN)
        power_ex_table_2 = MathTable(
            [["2^{-4}", "2^{-3}", "2^{-2}", "2^{-1}", "2^0", "2^1" ,"2^2", "2^3", "2^4"],
            [r"\times", r"\times", r"\times", r"\times", 0, 2, 4, 6, 8]],
        ).scale(0.7).move_to(1*DOWN)
        power_ex_table_3 = MathTable(
            [["2^{-4}", "2^{-3}", "2^{-2}", "2^{-1}", "2^0", "2^1" ,"2^2", "2^3", "2^4"],
            [r"\times", r"\times", r"\times", -2, 0, 2, 4, 6, 8]],
        ).scale(0.7).move_to(1*DOWN)
        power_ex_table_4 = MathTable(
            [["2^{-4}", "2^{-3}", "2^{-2}", "2^{-1}", "2^0", "2^1" ,"2^2", "2^3", "2^4"],
            [-8, -6, -4, -2, 0, 2, 4, 6, 8]],
        ).scale(0.7).move_to(1*DOWN)
        self.play(Create(power_ex_table))
        self.wait()
        self.play(TransformMatchingShapes(power_ex_table, power_ex_table_2))
        self.wait(3)
        self.play(TransformMatchingShapes(power_ex_table_2, power_ex_table_3))
        self.wait(3)
        self.play(TransformMatchingShapes(power_ex_table_3, power_ex_table_4))
        self.wait(3.5)

        # 2 is not a generator
        generator_2 = MathTex(r"\langle", r"2", r"\rangle =", r"2", r"\mathbb{Z}").next_to(temp_group_ex, 1.5*DOWN)
        self.play(Write(generator_2))
        self.wait()
        self.play(Circumscribe(generator_2, color=COLOR_1))
        self.wait()

        # generator change tex `<a> = aZ`
        generator = [
            r"\langle @ a @ \rangle = @ a @ \mathbb{Z}".split("@"), # 1
            r"\langle @ 1 @ \rangle = @ 1 @ \mathbb{Z}".split("@"), # 2
            r"\langle @ 1 @ \rangle = @ \mathbb{Z}".split("@"),
            r"\langle @ -1 @ \rangle = @ -1 @ \mathbb{Z}".split("@"), # 4
            r"\langle @ -1 @ \rangle = @ \mathbb{Z}".split("@"),
        ]
        generator = [MathTex(*text).next_to(temp_group_ex, 1.5*DOWN) for text in generator]
        generator.insert(0, generator_2)

        self.show_transform_and_fadeout_expl(generator, start=1, end=2, fade_out=False)
        self.play(FadeOut(power_ex_table_4))
        self.wait(3.5)
        self.show_transform_and_fadeout_expl(generator, start=2, end=4, circumscribe=True, fade_out=False)
        self.show_transform_and_fadeout_expl(generator, start=4, circumscribe=True, fade_out=True)


        # clean `(Z, +)` elements from screen
        self.play(FadeOut(temp_group_ex, underline))




    def add_generator_def(self) -> VGroup:
        generator_def = MathTex(r"\langle a \rangle = \{ a^k:\; k\in\mathbb{Z} \}")
        generator_def_2 = MathTex(r"G = \langle a \rangle \quad\quad \text{generator}").next_to(generator_def, DOWN)

        self.play(Write(generator_def_2))
        a = self.get_and_add_arrow(DOWN+RIGHT, DOWN+LEFT, radius=-1.3, color=COLOR_1, tip_length=0.2, tip_width=0.2)
        self.wait(3)
        self.play(Write(generator_def))
        self.wait(4)
        self.play(FadeOut(a))
        self.wait(2)

        vgroup = VGroup(generator_def, generator_def_2)
        return vgroup


    def add_power_def(self) -> VGroup:
        def_0 = MathTex(r"a^{k+1} = a^k * a,\quad k\in\mathbb{Z}")
        def_1 = MathTex(r"a^0 = e")

        def_vgroup = VGroup(def_0, def_1).arrange(direction=DOWN, aligned_edge=LEFT).to_edge(UL)
        self.play(Write(def_vgroup[0]), run_time=1.5)
        self.wait(9)
        self.play(Write(def_vgroup[1]))
        self.wait(3)

        return def_vgroup
    
    def add_group_notation(self) -> VGroup:
        # Add (G, *) sign and write it's a group
        # Return VGroup containing 2 texes and arc (arrow from text to '(G, *)')

        group_notation = MathTex(r"(G, *)").shift(3.25*UP+4*RIGHT)  # group notation
        group_text = Tex(r"group").shift(2.25*UP+4*RIGHT)

        self.play(Write(group_notation))
        self.play(Write(group_text))
        a = self.get_and_add_arrow(2.25*UP+4.8*RIGHT, 3.25*UP+4.8*RIGHT, radius=0.7, color=COLOR_1, tip_length=0.2, tip_width=0.2)

        vgroup = VGroup(group_notation, group_text, a)
        return vgroup
    


