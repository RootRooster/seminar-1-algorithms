from manim import *
from manim_slides import slide

config.background_color = "#f5f2eb"


class FOCS(slide.Slide):
    def construct(self):
        title = Text(
            "IEEE Symposium on Foundations of Computer Science", color=BLACK
        ).scale(1.2)
        author = (
            Text(
                "Matej B., Nik Č., Klemen K., Tomaž J. L., Bor P., Marko R., Pia S., Vanja S.",
                color=BLACK,
            )
            .scale(0.7)
            .shift(DOWN)
        )
        self.play(Write(title))
        self.play(Write(author))
        self.next_slide()
