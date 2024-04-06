from collections import namedtuple

import numpy as np
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

shader_src = namedtuple('shader_src', ['path', 'source_lines'])
Color = namedtuple('Color', ['r', 'g', 'b', 'a'])


# compiled_shader = namedtuple('compiled_shader', ['shader_pointer', 'vertex_array_objects','vertex_buffer_objects'])


class ShaderException(Exception): pass


class Engine:

    def __init__(self, screen_width, screen_height, **options):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shader_srcs = {}
        self.compiled_shaders = {}

        self.background_color = options.get('background_color', Color(.2, .2, .2, 1.0))

        self.vertex_objects = {}

        self.get_shader(name='vertex_src', path='./shaders/vertex.glsl')
        self.get_shader(name='fragment_src', path='./shaders/fragment.glsl')
        self.compile_shader(vert_name='vertex_src', frag_name='fragment_src')

    def compile_shader(self, vert_name: str = 'vertex_src',
                       frag_name: str = 'fragment_src'):
        vert_src = self.shader_srcs.get(vert_name)
        if vert_src is None:
            msg = 'Vertex shader not loaded'
            raise ShaderException(msg)
        frag_src = self.shader_srcs.get(frag_name)
        if frag_src is None:
            msg = 'Fragment shader not loaded'
            raise ShaderException(msg)

        vert_shader = compileShader(vert_src.source_lines, GL_VERTEX_SHADER)
        frag_shader = compileShader(frag_src.source_lines, GL_FRAGMENT_SHADER)
        shader = compileProgram(vert_shader,
                                frag_shader)

        self.compiled_shaders['basic_shader'] = shader

        glDeleteShader(vert_shader)
        glDeleteShader(frag_shader)

        # self.create_vertex_object(name='basic_tri',
        #                           data=self.create_basic_triangle())

        self.tri_verts = self.create_basic_triangle()

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.tri_verts.nbytes, self.tri_verts, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glBindBuffer(GL_ARRAY_BUFFER,0)
        glBindVertexArray(0)

    def get_shader(self, name: str, path: str) -> None:
        with open(path) as f:
            source = f.readlines()
        self.shader_srcs[name] = shader_src(path, source)

    @staticmethod
    def create_basic_quad():
        vertex_data = np.array(
            (1.0, 1.0, 0.0, 1.0, 1.0,  # top-right
             -1.0, 1.0, 0.0, 0.0, 1.0,  # top-left
             -1.0, -1.0, 0.0, 0.0, 0.0,  # bottom-left
             -1.0, -1.0, 0.0, 0.0, 0.0,  # bottom-left
             1.0, -1.0, 0.0, 1.0, 0.0,  # bottom-right
             1.0, 1.0, 0.0, 1.0, 1.0),  # top-right
            dtype=np.float32
        )
        return vertex_data

    @staticmethod
    def create_basic_triangle():
        vertex_data = np.array([
            [-.5, 0.5 * np.sqrt(3) / 3, 0.0],
            [.5, 0.5 * np.sqrt(3) / 3, 0.0],
            [0.0, 0.5 * np.sqrt(3) / 3, 0.0]
        ],
            dtype=np.float32)

        return vertex_data

    def create_vertex_object(self, name: str,
                             data: np.array):
        self.vertex_objects[name] = VertexObject(name=name,
                                                 data=data,
                                                 stride=3,
                                                 offset=0)

    def clear_color(self):
        r, g, b, a = self.background_color
        glClearColor(r, g, b, a)
        glClear(GL_COLOR_BUFFER_BIT)

    def use_shader(self, name: str):
        glUseProgram(self.compiled_shaders[name])

    def use_vao(self, name: str):

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def render(self):
        self.clear_color()
        self.use_shader('basic_shader')
        self.use_vao('basic_tri')

    def destroy(self):
        for shader in self.compiled_shaders.values():
            glDeleteProgram(shader)
        for vertex_obj in self.vertex_objects.values():
            vertex_obj.destroy()


class VertexObject:
    def __init__(self, name: str,
                 data: 'numpy array',
                 stride: int,
                 offset: int,
                 num_arrays: int = 1,
                 num_buffers: int = 1,
                 normalized=False,
                 type_=GL_STATIC_DRAW):
        self.data = data
        self.name = name
        self.stride = stride
        self._offset = offset
        self._normalized = normalized

        # gen vao
        self.vao = glGenVertexArrays(num_arrays)
        # gen vbo
        self.vbo = glGenBuffers(num_buffers)

        # bind array, buffer
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        vertex_attr_position = 0
        glVertexAttribPointer(vertex_attr_position,
                              self.num_attributes,
                              self.d_type,
                              self.normalized,
                              self.stride,
                              ctypes.c_void_p(self.offset))

        glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, type_)
        glEnableVertexAttribArray(vertex_attr_position)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    @property
    def num_attributes(self):
        return self.data.shape[1]  # assuming data is num data, by the num attributes

    @property
    def d_type(self):
        if self.data.dtype == np.float32:
            return GL_FLOAT

    @property
    def normalized(self):
        if self._normalized:
            return GL_TRUE
        else:
            return GL_FALSE

    @normalized.setter
    def normalized(self, val: bool):
        self._normalized = bool(val)

    @property
    def offset(self):
        return self._offset

    def destroy(self):
        glDeleteVertexArrays(1, self.vao)
        glDeleteBuffers(1, self.vbo)
