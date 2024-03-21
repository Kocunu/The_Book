from manim import *

class Einorst(Scene):
    def construct(self):
        # Initial list
        text = Tex("E", "I", "N", "O", "R", "S", "T")
        self.play(Write(text))

        # Perform Einorst Sort (Insertion Sort)
        for i in range(1, len(text)):
            key = text[i].copy()
            j = i - 1
            while j >= 0 and text[j].get_tex_string() > key.get_tex_string():
                text[j + 1].become(text[j].copy())
                j -= 1
                self.play(TransformFromCopy(text[j + 1], text[j]))
                self.wait(0.5)
            text[j + 1].become(key.copy())
            self.play(TransformFromCopy(key, text[j + 1]))
            self.wait(0.5)

        self.wait(2)


