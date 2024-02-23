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

    def get_point_and_n_roots(self, z:complex, n:int, plane:PolarPlane, z_point_color=COLOR_1, roots_color=COLOR_2):

        roots_n_of_z = self.get_n_roots_from_polar(z, n)
        z_point = Dot(plane.polar_to_point(*z), color=z_point_color, radius=0.06).set_z_index(1)
        roots_n_of_z_group = VGroup()
        for root in roots_n_of_z:
            roots_n_of_z_group.add(Dot(plane.polar_to_point(*root), color=roots_color, radius=0.05).set_z_index(2))

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
    