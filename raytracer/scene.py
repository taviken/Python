import numpy as np

import camera
import plane
import sphere


class Scene:
    """
        Holds pointers to all objects in the scene
    """

    def __init__(self):
        """
            Set up scene objects.
        """

        self.spheres = [
            sphere.Sphere(
                center=[
                    np.random.uniform(low=3.0, high=10.0),
                    np.random.uniform(low=-5.0, high=5.0),
                    np.random.uniform(low=-5.0, high=5.0)
                ],
                radius=np.random.uniform(low=0.3, high=2.0),
                color=[
                    np.random.uniform(low=0.3, high=1.0),
                    np.random.uniform(low=0.3, high=1.0),
                    np.random.uniform(low=0.3, high=1.0)
                ]
            ) for i in range(16)
        ]

        self.planes = [
            plane.Plane(
                normal=[0, 0, 1],
                tangent=[1, 0, 0],
                bitangent=[0, 1, 0],
                uMin=-5,
                uMax=5,
                vMin=-5,
                vMax=5,
                center=[0, 0, -2],
                color=[
                    np.random.uniform(low=0.3, high=1.0),
                    np.random.uniform(low=0.3, high=1.0),
                    np.random.uniform(low=0.3, high=1.0)
                ]
            ),
        ]

        self.camera = camera.Camera(
            position=[-5, 0, 0],
            phi=0
        )

        self.outDated = True
