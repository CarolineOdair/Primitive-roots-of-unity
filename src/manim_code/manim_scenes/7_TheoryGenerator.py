from imports import *


class GeneratorDef(MyScene):  # 7th scene
    def construct(self):
        self.FS = 35

        ######    def of power in group    ###### 
        group_notation = self.add_group_notation()
        power_def = self.add_power_def()
        generator_def = self.add_generator_def()
        self.play(FadeOut(group_notation), generator_def.animate.move_to(group_notation))

        ######    integers example    ######
        self.manage_integers_example()


        self.wait(5)


    def manage_integers_example(self):
        # Play animations showing power examples for 2
        c = COLOR_2
 

        # Animate `(Z, +)`
        temp_group_ex = MathTex(r"(\mathbb{Z}, +)").shift(1.5*UP)
        underline = Underline(temp_group_ex, color=c)
        self.play(FadeIn(temp_group_ex), Create(underline))


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
        for el in power_ex_group:
            self.play(Write(el))
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
            [-8, -6, -4, -2, 0, 2, 4, 6, 8]],
        ).scale(0.7).move_to(1*DOWN)
        self.play(Create(power_ex_table))
        self.wait()
        self.play(TransformMatchingShapes(power_ex_table, power_ex_table_2))
        self.play(TransformMatchingShapes(power_ex_table_2, power_ex_table_3))

        # 2 is not a generator
        generator_2 = MathTex(r"\langle", r"2", r"\rangle =", r"2", r"\mathbb{Z}").next_to(temp_group_ex, 1.5*DOWN)
        self.play(Write(generator_2))
        self.play(Circumscribe(generator_2, color=COLOR_1))

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
        self.play(FadeOut(power_ex_table_3))
        self.show_transform_and_fadeout_expl(generator, start=2, end=4, circumscribe=True, fade_out=False)
        self.show_transform_and_fadeout_expl(generator, start=4, circumscribe=True, fade_out=True)


        # clean `(Z, +)` elements from screen
        self.play(FadeOut(temp_group_ex, underline))




    def add_generator_def(self) -> VGroup:
        generator_def = MathTex(r"\langle a \rangle = \{ a^k:\; k\in\mathbb{Z} \}")
        generator_def_2 = MathTex(r"G = \langle a \rangle \quad\quad \text{generator}").next_to(generator_def, DOWN)

        self.play(Write(generator_def))
        self.play(Write(generator_def_2))
        a = self.get_and_add_arrow(DOWN+RIGHT, DOWN+LEFT, radius=-1.3, color=COLOR_1, tip_length=0.2, tip_width=0.2)
        self.play(FadeOut(a))

        vgroup = VGroup(generator_def, generator_def_2)
        return vgroup


    def add_power_def(self) -> VGroup:
        def_0 = MathTex(r"a^{k+1} = a^k * a,\quad k\in\mathbb{Z}")
        def_1 = MathTex(r"a^0 = e")

        def_vgroup = VGroup(def_0, def_1).arrange(direction=DOWN, aligned_edge=LEFT).to_edge(UL)
        self.play(Write(def_vgroup))

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
    
    def get_and_add_arrow(self, start, end, radius:float=2, color=WHITE, tip_length=0.2, tip_width=0.2, play:bool=True):
        # Play creating arc between given points
        # Return arc

        a = ArcBetweenPoints(start, end, radius=radius, color=color)
        a.add_tip(tip_shape=StealthTip, tip_length=tip_length, tip_width=tip_width)

        if play:
            self.play(Create(a))

        return a

