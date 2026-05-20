from manim import *

class LogoAnimation(Scene):
    def construct(self):
        # Load your logo (must be .svg)
        logo = SVGMobject("html.svg").set_height(3)
        
        # Animation sequence
        self.play(DrawBorderThenFill(logo), run_time=3)
        self.wait(2)