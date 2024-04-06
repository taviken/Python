import numpy as np
import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


class Engine:
    """
        Responsible for drawing scenes
    """

    def __init__(self, width, height):
        """
            Initialize a flat raytracing context
            
                Parameters:
                    width (int): width of screen
                    height (int): height of screen
        """
        self.screenWidth = width
        self.screenHeight = height
        self.main_vertices = None
        self.main_vertex_count = None
        self.vao = None
        self.vbo = None
        self.colorBuffer = None
        self.num_objects = None
        self.num_attributes = None
        self.num_pixels = None
        self.objectData = None
        self.objectDataTexture = None

        # general OpenGL configuration
        self.shader = self.create_shader("shaders/frameBufferVertex.glsl",
                                         "shaders/frameBufferFragment.glsl")

        self.compute_shader = self.create_compute_shader("Shaders/rayTracer.glsl")

        glUseProgram(self.shader)

        self.create_main_quad()
        self.create_color_buffer()
        self.create_resource_memory()

    def create_main_quad(self):
        # x, y, z, s, t
        self.main_vertices = np.array(
            (1.0, 1.0, 0.0, 1.0, 1.0,  # top-right
             -1.0, 1.0, 0.0, 0.0, 1.0,  # top-left
             -1.0, -1.0, 0.0, 0.0, 0.0,  # bottom-left
             -1.0, -1.0, 0.0, 0.0, 0.0,  # bottom-left
             1.0, -1.0, 0.0, 1.0, 0.0,  # bottom-right
             1.0, 1.0, 0.0, 1.0, 1.0),  # top-right
            dtype=np.float32
        )

        self.main_vertex_count = 6

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.main_vertices.nbytes, self.main_vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))

    def create_color_buffer(self):

        self.colorBuffer = glGenTextures(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.colorBuffer)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.screenWidth, self.screenHeight, 0, GL_RGBA, GL_FLOAT, None)

    def create_resource_memory(self, num_objects=1024, num_attributes=20):

        """
            allocate storage for up to 1024 objects (why not?)
        """
        self.num_objects = num_objects
        self.num_attributes = num_attributes
        self.num_pixels = num_attributes / 4

        # sphere: (cx cy cz r) (r g b -)     (- - - -)     (- - - -)             (- - - -)
        # plane: (cx cy cz tx) (ty tz bx by) (bz nx ny nz) (umin umax vmin vmax) (r g b -)
        self.objectData = np.zeros([num_objects * num_attributes], dtype=np.float32)

        self.objectDataTexture = glGenTextures(1)
        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, self.objectDataTexture)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.num_pixels, self.num_objects, 0, GL_RGBA, GL_FLOAT,
                     bytes(self.objectData))

    @staticmethod
    def create_shader(vertexFilepath, fragmentFilepath):
        """
            Read source code, compile and link shaders.
            Returns the compiled and linked program.
        """

        with open(vertexFilepath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                                compileShader(fragment_src, GL_FRAGMENT_SHADER))

        return shader

    @staticmethod
    def create_compute_shader(filepath):
        """
            Read source code, compile and link shaders.
            Returns the compiled and linked program.
        """

        with open(filepath, 'r') as f:
            compute_src = f.readlines()

        shader = compileProgram(compileShader(compute_src, GL_COMPUTE_SHADER))

        return shader

    def record_sphere(self, i, _sphere):

        # sphere: (cx cy cz r) (r g b -) (- - - -) (- - - -) (- - - -)

        self.objectData[20 * i] = _sphere.center[0]
        self.objectData[20 * i + 1] = _sphere.center[1]
        self.objectData[20 * i + 2] = _sphere.center[2]

        self.objectData[20 * i + 3] = _sphere.radius

        self.objectData[20 * i + 4] = _sphere.color[0]
        self.objectData[20 * i + 5] = _sphere.color[1]
        self.objectData[20 * i + 6] = _sphere.color[2]

    def record_plane(self, i, _plane):

        # plane: (cx cy cz tx) (ty tz bx by) (bz nx ny nz) (umin umax vmin vmax) (r g b -)

        self.objectData[20 * i] = _plane.center[0]
        self.objectData[20 * i + 1] = _plane.center[1]
        self.objectData[20 * i + 2] = _plane.center[2]

        self.objectData[20 * i + 3] = _plane.tangent[0]
        self.objectData[20 * i + 4] = _plane.tangent[1]
        self.objectData[20 * i + 5] = _plane.tangent[2]

        self.objectData[20 * i + 6] = _plane.bitangent[0]
        self.objectData[20 * i + 7] = _plane.bitangent[1]
        self.objectData[20 * i + 8] = _plane.bitangent[2]

        self.objectData[20 * i + 9] = _plane.normal[0]
        self.objectData[20 * i + 10] = _plane.normal[1]
        self.objectData[20 * i + 11] = _plane.normal[2]

        self.objectData[20 * i + 12] = _plane.uMin
        self.objectData[20 * i + 13] = _plane.uMax
        self.objectData[20 * i + 14] = _plane.vMin
        self.objectData[20 * i + 15] = _plane.vMax

        self.objectData[20 * i + 16] = _plane.color[0]
        self.objectData[20 * i + 17] = _plane.color[1]
        self.objectData[20 * i + 18] = _plane.color[2]

    def update_scene(self, scene):

        scene.outDated = False

        glUseProgram(self.compute_shader)

        glUniform1f(glGetUniformLocation(self.compute_shader, "sphereCount"), len(scene.spheres))

        for i, _sphere in enumerate(scene.spheres):
            self.record_sphere(i, _sphere)

        glUniform1f(glGetUniformLocation(self.compute_shader, "planeCount"), len(scene.planes))

        for i, _plane in enumerate(scene.planes):
            self.record_plane(i + len(scene.spheres), _plane)

        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, self.objectDataTexture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.num_pixels, self.num_objects, 0, GL_RGBA, GL_FLOAT,
                     bytes(self.objectData))

    def prepare_scene(self, scene):
        """
            Send scene data to the shader.
        """

        glUseProgram(self.compute_shader)

        glUniform3fv(glGetUniformLocation(self.compute_shader, "viewer.position"), 1, scene.camera.position)
        glUniform3fv(glGetUniformLocation(self.compute_shader, "viewer.forwards"), 1, scene.camera.forwards)
        glUniform3fv(glGetUniformLocation(self.compute_shader, "viewer.right"), 1, scene.camera.right)
        glUniform3fv(glGetUniformLocation(self.compute_shader, "viewer.up"), 1, scene.camera.up)

        if scene.outDated:
            self.update_scene(scene)

        glActiveTexture(GL_TEXTURE1)
        glBindImageTexture(1, self.objectDataTexture, 0, GL_FALSE, 0, GL_READ_ONLY, GL_RGBA32F)

    def render_scene(self, scene):
        """
            Draw all objects in the scene
        """

        glUseProgram(self.compute_shader)

        self.prepare_scene(scene)

        glActiveTexture(GL_TEXTURE0)
        glBindImageTexture(0, self.colorBuffer, 0, GL_FALSE, 0, GL_WRITE_ONLY, GL_RGBA32F)

        glDispatchCompute(self.screenWidth, self.screenHeight, 1)

        # make sure writing to image has finished before read
        glMemoryBarrier(GL_SHADER_IMAGE_ACCESS_BARRIER_BIT)
        glBindImageTexture(0, 0, 0, GL_FALSE, 0, GL_WRITE_ONLY, GL_RGBA32F)
        self.draw_screen()

    def draw_screen(self):
        glUseProgram(self.shader)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.colorBuffer)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, self.main_vertex_count)
        pg.display.flip()

    def destroy(self):
        """
            Free any allocated memory
        """
        glUseProgram(self.compute_shader)
        glMemoryBarrier(GL_ALL_BARRIER_BITS)
        glDeleteProgram(self.compute_shader)
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))
        glDeleteTextures(1, (self.colorBuffer,))
        glDeleteProgram(self.shader)
