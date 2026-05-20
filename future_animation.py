from manim import *

class SquareToLogo(Scene):
    def construct(self):
        # Professional dark background
        self.camera.background_color = "#121212"

        # 1. Create a stylish initial square
        square = Square(side_length=2.5)
        square.set_stroke(color=WHITE, width=4)
        square.set_fill(WHITE, opacity=0.6)
        
        # 2. Prepare the Logo Mark (Paths from SVG)
        # SVGMobject will pick up the paths but likely skip the <text> element
        logo_mark = SVGMobject("futurebusiness.svg")
        # logo_mark.set_color(WHITE) # Optional: uniform color or keep SVG colors
        
        # 3. Prepare the Text (since SVG <text> is unsupported)
        # Using a clean sans-serif font
        logo_text = Text("Passify", font="sans-serif", weight=BOLD)
        
        # 4. Compose the full logo
        # We arrange them side-by-side
        logo_group = VGroup(logo_mark, logo_text).arrange(RIGHT, buff=0.5)
        logo_group.width = 7 # Adjust size to fit screen nicely
        logo_group.center()

        # 5. Animation Sequence
        
        # Intro: Show the square
        self.play(
            Create(square),
            run_time=1,
            rate_func=smooth
        )
        self.wait(0.5)

        # Transformation: Square -> Full Logo
        # ReplacementTransform will attempt to morph the square into the multiple parts of the logo
        self.play(
            ReplacementTransform(square, logo_group),
            run_time=2.5,
            rate_func=smooth
        )
        
        ## Subtle "pulse" or scaling for the final logo
        #self.play(
        #    logo_group.animate.scale(1.05),
        #    rate_func=there_and_back,
        #    run_time=1.5
        #)
        #
        self.wait(2)
