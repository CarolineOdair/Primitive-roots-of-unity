from manim import *

class DisplayAndRemoveText(Scene):
    def construct(self):
        
        TEXT = Text('"Matematyka to ładne warzywo"').scale(0.5)
        self.play(Write(TEXT.to_edge(RIGHT)))
        self.wait(5)

        self.play(FadeOut(TEXT))
