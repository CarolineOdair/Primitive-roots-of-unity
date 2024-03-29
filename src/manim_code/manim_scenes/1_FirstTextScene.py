from imports import *

class S1_FirstTextScene(MyScene):  # 1st scene
    def construct(self):
        
        TEXT = Text('"Matematyka to ładne warzywo"').scale(0.5)
        self.play(Write(TEXT.to_edge(RIGHT)))
        self.wait(3)

        self.play(FadeOut(TEXT))
