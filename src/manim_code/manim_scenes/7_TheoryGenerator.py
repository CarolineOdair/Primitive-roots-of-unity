from imports import *


class GeneratorDef(MyScene):  # 7th scene
    def construct(self):

        ######    def of power in group    ###### 
        group_notation = self.add_group_notation()
        power_def = self.manage_power()


        self.wait(5)


    

    def manage_power(self) -> VGroup:
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

