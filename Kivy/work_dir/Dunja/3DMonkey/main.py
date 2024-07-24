from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
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
        self.reverse_rotation = False  # Flag to toggle reverse rotation
        self.rot = Rotate(angle=0, axis=(1, 0, 1))  # Default rotation along (1, 0, 1)
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
        self.rot.angle += delta * 100
        # Update rotation based on reverse_rotation flag
        if self.reverse_rotation:
            self.rot.axis = (0, -1, 0)   # Reverse rotation
        else:
            self.rot.axis = (0, 1, 0)  # Normal rotation


    def setup_scene(self):
        Color(1, 1, 1, 1)
        PushMatrix()
        Translate(0, 0, -3)
        self.rot = Rotate(angle=1, axis=(1, 0, 1))  # Default rotation along (1, 0, 1)
        m = list(self.scene.objects.values())[0]
        UpdateNormalMatrix()
        self.mesh = Mesh(
            vertices=m.vertices,
            indices=m.indices,
            fmt=m.vertex_format,
            mode='triangles',
        )
        PopMatrix()


class RendererApp(App):
    def build(self):
        layout = RelativeLayout()
        self.renderer = Renderer()
        btn = Button(text="Toggle Rotation", size_hint=(None, None), size=(500, 150), pos_hint={'x': 0, 'y': 0})

        btn.bind(on_press=self.on_button_press)

        layout.add_widget(btn)
        layout.add_widget(self.renderer)
        return layout

    def on_button_press(self, instance):
        self.renderer.reverse_rotation = not self.renderer.reverse_rotation  # Toggle rotation direction


if __name__ == "__main__":
    RendererApp().run()
