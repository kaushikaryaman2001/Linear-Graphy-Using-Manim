from manimlib.imports import *
class Graphing(GraphScene):
    CONFIG = {
        "x_min": -7,
        "x_max": 7,
        "y_min": -7,
        "y_max": 7,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "f(x)=2x+4")
        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))
        #Display graph

        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
     #   self.play(Transform(func_graph), Transform(graph_lab))
        self.wait(2)


    def func_to_graph(self, x):
        return (2*x+2)

class Equations(Scene):
    def construct(self):
        eq=TextMobject("$$f(x)=2x+4$$")
#        eq=TextMobject("$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$")
        des1 = TextMobject("With manim, you can write Linear equations like this...")
        des1.set_color(color=PURPLE)
        des1.shift(3*UP)
        eq.set_color(color=DARK_BLUE)
        self.play(Write(des1))
        self.play(Write(eq))
        self.wait(3)
