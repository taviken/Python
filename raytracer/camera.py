import numpy as np
import pyrr


class Camera:
    """
        Represents a camera in the scene
    """

    def __init__(self, position,theta=0.0,phi=0.0):
        """
            Create a new camera at the given position facing in the given direction.

            Parameters:
                position (array [3,1])
                direction (array [3,1])
        """
        self.forwards = None
        self.right=None
        self.up=None
        self.position = np.array(position, dtype=np.float32)
        self.theta = theta
        self.phi = phi
        self.recalculate_vectors()

    def recalculate_vectors(self):
        self.forwards = np.array([np.cos(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi)),
                                  np.sin(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi)),
                                  np.sin(np.deg2rad(self.phi))],
                                 dtype=np.float32)

        self.right = pyrr.vector3.cross(self.forwards, np.array([0, 0, 1], dtype=np.float32))

        self.up = pyrr.vector3.cross(self.right, self.forwards)
