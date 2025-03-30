from manim import *
from manim_slides import slide

config.background_color = "#f5f2eb"


class FOCS(slide.Slide):
    def construct(self):
        # TitleSlide
        title1 = Tex(r"\textbf{IEEE Symposium on}", color=BLACK).scale(1.2)
        title2 = Tex(r"\textbf{Foundations of Computer Science}", color=BLACK).scale(
            1.2
        )

        title_group = (
            VGroup(title1, title2)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .to_edge(LEFT, buff=1)
            .shift(UP * 0.7)
        )

        author = (
            Tex(
                "Matej B., Nik Č., Klemen K., Tomaž J. L., Bor P., Marko R., Pia S., Vanja S.",
                color=BLACK,
            )
            .scale(0.7)
            .shift(DOWN * 2)
            .to_edge(LEFT, buff=1)
        )
        self.play(Write(title_group))

        self.play(Write(author, run_time=0.8))
        self.next_slide()

        # First slide
