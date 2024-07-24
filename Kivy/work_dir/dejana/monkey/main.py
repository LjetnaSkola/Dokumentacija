from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.resources import resource_find
from kivy.graphics.transformation import Matrix
from kivy.graphics.opengl import glEnable, glDisable, GL_DEPTH_TEST
from kivy.graphics import RenderContext, Callback, PushMatrix, PopMatrix, \
    Color, Translate, Rotate, Mesh, UpdateNormalMatrix
from objloader import ObjFile


class Renderer(Widget):
    def __init__(self, **kwargs):
        super(Renderer, self).__init__(**kwargs)
        
        self.rotation_speed = 100  # Initial rotation speed
        self.rot_direction = 1  # Initial rotation direction (1 for clockwise, -1 for counter-clockwise)
        
        self.canvas = RenderContext(compute_normal_mat=True)
        self.canvas.shader.source = resource_find('simple.glsl')
        self.scene = ObjFile(resource_find("monkey.obj"))
        
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
        self.rot.angle += delta * self.rotation_speed * self.rot_direction

    def setup_scene(self):
        Color(1, 1, 1, 1)
        PushMatrix()
        Translate(0, 0, -3)
        self.rot = Rotate(1, 0, -1, 0)
        m = list(self.scene.objects.values())[0]
        UpdateNormalMatrix()
        self.mesh = Mesh(
            vertices=m.vertices,
            indices=m.indices,
            fmt=m.vertex_format,
            mode='triangles',
        )
        PopMatrix()

    def toggle_rotation_direction(self):
        self.rot_direction *= -1  # Toggle rotation direction


class RendererApp(App):
    def build(self):
        self.renderer = Renderer()
        
        # Create a button to toggle rotation direction
        button = Button(text="Smjer: click", size_hint=(None, None), size=(200, 50), pos=(20, 20))
        button.bind(on_press=self.toggle_rotation)
        
        layout = Widget()
        layout.add_widget(self.renderer)
        layout.add_widget(button)
        
        return layout

    def toggle_rotation(self, instance):
        self.renderer.toggle_rotation_direction()


if __name__ == "__main__":
    RendererApp().run()
