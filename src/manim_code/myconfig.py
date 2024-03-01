from manim import *


######    colors    ######
GOLDENROD = rgb_to_color([218,165,32])
ROYALBLUE = rgb_to_color([65,105,225])
NAVY_BLUE = rgb_to_color([4, 4, 15])

COLOR_1 = GOLDENROD
COLOR_2 = BLUE_D
COLOR_3 = rgb_to_color([113, 203, 82])


######    grid    ######
GRID_COLOR = GREY


######    config    ######
config.background_color = NAVY_BLUE
config.max_files_cached = 250


######    my scene class    ######
class MyScene(Scene):

    def clear_screen(self, obj_to_clear:VGroup=None, color:ManimColor=COLOR_1) -> None:
        if obj_to_clear is None:
            obj_to_clear = VGroup(*self.vmobjects)

        last_dot = Dot(color=color)
        self.play(ReplacementTransform(obj_to_clear, last_dot))
        self.wait(0.5)
        self.play(Uncreate(last_dot))


    def add_plane(self, azimuth_step:float=12, shiftt:Vector=0, size:float=4, radius_step:float=1, radius_max:float=3, r_values:list=[]) -> PolarPlane:
        plane = PolarPlane(
            azimuth_units="PI radians",
            size=size,
            azimuth_compact_fraction = False,
            azimuth_step = azimuth_step,
            radius_step = radius_step,
            radius_max=radius_max,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_opacity": 0.5
            }
        ).add_coordinates(r_values=r_values, a_values=[]).shift(shiftt)

        return plane
    


    def add_zn_boxes_animation(self, boxes:VGroup, start:int, add:int, arc_radius:float=None, color=WHITE, step:int=1):

        n = len(boxes)
        if step <= 0:
            raise Exception(f"`step` must be grater then 0, not {step}")
        elif step >= n:
            raise Exception(f"{step}>={n}, but `step` must be lower then number of `boxes`")
        
        if add % step != 0:
            raise Exception(f"`add` must be multiple of `step`, but `add`({add}) % `step`({step}) == {add%step} ")

        start_index = start
        last_arrows = []

        length_between_boxes = boxes.submobjects[step].get_top() - boxes.submobjects[0].get_top()
 
        if arc_radius is None:
            arc_radius = 0.9*length_between_boxes[0]
        if length_between_boxes[0]/2 > abs(arc_radius):
            raise Exception(f"`arc_radius`(={arc_radius}) must be greater, now it is lower then 1/2*length between boxes (={length_between_boxes[0]})")
        
        for plus in range(int(add/step)):
            if (start_index % n) + step < n:
                self.animation_before_the_arrow(boxes=boxes, start_box_index=start_index%n)
                start_top = boxes.submobjects[start_index % n].get_top() + [0, 0.1, 0]
                next_top = start_top + length_between_boxes
                arrow = self.get_and_add_arrow(start_top, next_top, radius=-arc_radius, play=False, color=color)

                if len(last_arrows) != 0:
                    self.play(Create(arrow), FadeOut(*last_arrows))
                else:
                    self.play(Create(arrow))

                self.play(boxes[start_index%n+step].animate.set_stroke_color(COLOR_2))
                start_index += step
                last_arrows = [arrow]


            elif (start_index % n) + step >= n:
                start_1_top = boxes.submobjects[start_index % n].get_top() + [0, 0.1, 0]
                next_1_top = start_1_top + length_between_boxes
                arrow_1 = self.get_and_add_arrow(start_1_top, next_1_top, radius=-arc_radius, play=False, color=color)

                next_2_top = boxes.submobjects[(start_index + step) % n].get_top() + [0, 0.1, 0]
                start_2_top = next_2_top - length_between_boxes
                arrow_2 =  self.get_and_add_arrow(start_2_top, next_2_top, radius=-arc_radius, play=False, color=color)

                if len(last_arrows) != 0:
                    self.play(Create(arrow_1), Create(arrow_2), FadeOut(*last_arrows))
                else:
                    self.play(Create(arrow_1), Create(arrow_2))

                self.play(boxes[(start_index+step)%n].animate.set_stroke_color(COLOR_2))

                start_index += step
                last_arrows = [arrow_1, arrow_2]

        self.play(FadeOut(*last_arrows))


    def animation_before_the_arrow(self, boxes, start_box_index):
        pass

    def animation_after_the_arrow(self, boxes, end_box_index):
        pass

    def get_and_add_arrow(self, start, end, radius:float=2, color=WHITE, tip_length=0.2, tip_width=0.2, play:bool=True):
        # Play creating arc between given points
        # Return arc

        a = ArcBetweenPoints(start, end, radius=radius, color=color)
        a.add_tip(tip_shape=StealthTip, tip_length=tip_length, tip_width=tip_width)

        if play:
            self.play(Create(a))

        return a




    def get_zn_boxes_group(self, n:int, buff_to_width_ratio:float=0.1, height_to_width_ratio:float=0.4,
                           width:float=10, font_size:float=40, relative_position:tuple=(ORIGIN, 0)):
        # Create VGroup of n boxes fitting the width of the screen with numbers from 0 to n-1 

        buff = width * buff_to_width_ratio
        boxes = VGroup(*[
            Rectangle(WHITE, width=width, height=width*height_to_width_ratio).add(Text(str(i), font_size=font_size, color=COLOR_1))
            for i in range(n)
        ])

        boxes.arrange_in_grid(cols=n, buff=buff).next_to(*relative_position)

        # width_of_boxes = n*width+(n-1)*buff
        scale = config.frame_width / (n*(width+buff))
        buff_on_outside = buff*scale/2
        boxes.width = config.frame_width - 2*buff_on_outside

        return boxes
    


    def show_transform_and_fadeout_expl(self, list_of_formulas, start:int=0, end:int=None, fade_out:bool=True, circumscribe:bool=False, transform_goal=None) -> None:

        length = len(list_of_formulas)
        if end is None or end > length:
            end = length


        for l in range(start, end):
            if l == 0:
                self.play(Write(list_of_formulas[l]))
            elif l > 0 and l < end:
                self.play(TransformMatchingTex(list_of_formulas[l-1], list_of_formulas[l]))


        if circumscribe and transform_goal is not None:
            self.play(Circumscribe(list_of_formulas[end-1], color=COLOR_1), Circumscribe(transform_goal, color=COLOR_2))
        elif circumscribe:
            self.play(Circumscribe(list_of_formulas[end-1], color=COLOR_1, fade_out=True))


        if fade_out:
            self.play(FadeOut(list_of_formulas[end-1]))

            

    def get_point_and_n_roots(self, z:complex, n:int, plane:PolarPlane, z_point_color=COLOR_1, dot_radius:float=0.05, roots_color=COLOR_2):

        roots_n_of_z = self.get_n_roots_from_polar(z, n)
        z_point = Dot(plane.polar_to_point(*z), color=z_point_color, radius=0.06).set_z_index(1)
        roots_n_of_z_group = VGroup()
        for root in roots_n_of_z:
            roots_n_of_z_group.add(Dot(plane.polar_to_point(*root), color=roots_color, radius=dot_radius).set_z_index(2))

        return z_point, roots_n_of_z_group

    def get_n_roots_from_cart(self, z:complex, n:int):
        phi = 1j**(2/n)
        r = z**(1/n)
        rt = []
        for num in range(n):
            rt.append(r*phi**num)
        return rt
    
    def get_n_roots_from_polar(self, z:tuple, n:int):
        phi = z[1]/n
        r = z[0]**(1/n)
        rt = []
        for num in range(n):
            rt.append((r, phi+PI*2*num/n))
        return rt

    def cart2pol(self, z:complex):
        x = z.real
        y = z.imag
        r = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        return (r, phi)

    def pol2cart(self, r, phi):
        x = r * np.cos(phi)
        y = r * np.sin(phi)
        return x+y*1j
    