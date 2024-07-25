from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.resources import resource_find
from kivy.graphics.transformation import Matrix
from kivy.graphics.opengl import glEnable, glDisable, GL_DEPTH_TEST
from kivy.graphics import RenderContext, Callback, PushMatrix, PopMatrix, \
    Color, Translate, Rotate, Mesh, UpdateNormalMatrix
from objloader import ObjFile

class Renderer(Widget):
    def __init__(self, **kwargs):
        self.canvas = RenderContext(compute_normal_mat=True)
        self.canvas.shader.source = resource_find('simple.glsl')
        self.scene = ObjFile(resource_find("monkey.obj"))
        super(Renderer, self).__init__(**kwargs)
        self.rotation_directions = {'X': 1, 'Y': 1, 'Z': 1}  # Direction for each axis
        self.active_axes = {'X': False, 'Y': False, 'Z': False}
        self.initial_angles = {'X': 0, 'Y': 0, 'Z': 0}
        with self.canvas:
            self.cb = Callback(self.setup_gl_context)
            PushMatrix()
            self.setup_scene()
            PopMatrix()
            self.cb = Callback(self.reset_gl_context)
        Clock.schedule_interval(self.update_glsl, 1 / 60.)

    def setup_gl_context(self, *args):
        glEnable(GL_DEPTH_TEST)

    def reset_gl_context(self, *args):
        glDisable(GL_DEPTH_TEST)

    def update_glsl(self, delta):
        asp = self.width / float(self.height)
        proj = Matrix().view_clip(-asp, asp, -1, 1, 1, 100, 1)
        self.canvas['projection_mat'] = proj
        self.canvas['diffuse_light'] = (1.0, 1.0, 0.8)
        self.canvas['ambient_light'] = (0.1, 0.1, 0.1)

        # Apply rotation based on active axes and direction
        if self.active_axes['X']:
            self.rot_x.angle += delta * 100 * self.rotation_directions['X']
        if self.active_axes['Y']:
            self.rot_y.angle += delta * 100 * self.rotation_directions['Y']
        if self.active_axes['Z']:
            self.rot_z.angle += delta * 100 * self.rotation_directions['Z']

    def setup_scene(self):
        Color(1, 1, 1, 1)
        PushMatrix()
        Translate(0, 0, -3)
        self.rot_x = Rotate(self.initial_angles['X'], 1, 0, 0)
        self.rot_y = Rotate(self.initial_angles['Y'], 0, 1, 0)
        self.rot_z = Rotate(self.initial_angles['Z'], 0, 0, 1)
        m = list(self.scene.objects.values())[0]
        UpdateNormalMatrix()
        self.mesh = Mesh(
            vertices=m.vertices,
            indices=m.indices,
            fmt=m.vertex_format,
            mode='triangles',
        )
        PopMatrix()

    def set_rotation_axis(self, axis, active):
        self.active_axes[axis] = active

    def change_rotation_direction(self, axis):
        self.rotation_directions[axis] *= -1  # Toggle direction for the given axis

    def reset_rotation(self):
        # Reset the rotation angles
        self.rot_x.angle = self.initial_angles['X']
        self.rot_y.angle = self.initial_angles['Y']
        self.rot_z.angle = self.initial_angles['Z']
