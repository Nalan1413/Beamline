# No Truce With The Furies
import pythia8
import numpy as np
from scipy.spatial.transform import Rotation


class Cascade:
    def __init__(self, eA, px, py, pz, xprod, yprod, zprod, idx):

        self.xprod, self.yprod, self.zprod = xprod, yprod, zprod
        self.idx = idx
        pythia = pythia8.Pythia()
        pythia.readString("Beams:idA = 2212")
        pythia.readString(f"Beams:eA = {eA}")

        pythia.readString("Beams:idB = 1000070140")
        pythia.readString("Beams:eB = 14")

        pythia.readString("Beams:frameType = 3")
        pythia.readString("HeavyIon:SigFitNGen = 0")
        pythia.readString("HeavyIon:SigFitDefPar = 29.95,2.19,0.60")
        pythia.readString("HardQCD:all = on")

        pythia.init()
        pythia.next()
        self.event = pythia.event

        # transformation matrix
        axis = [px, py, pz]
        self.rotation_matrix = Rotation.from_rotvec(axis).as_matrix()


    def transformation(self):
        particle_x = [particle.xProd() for particle in self.event]
        particle_y = [particle.yProd() for particle in self.event]
        particle_z = [particle.zProd() for particle in self.event]
        particle_t = np.array([particle_x, particle_y, particle_z])
        rotated_points = np.dot(self.rotation_matrix, particle_t)
        for i in range(rotated_points.shape[1]):
            rotated_points[0, i] += self.xprod
            rotated_points[1, i] += self.yprod
            rotated_points[2, i] += self.zprod

        for particle, new_coords in zip(self.event, rotated_points.T):
            particle.xProd(new_coords[0])
            particle.yProd(new_coords[1])
            particle.zProd(new_coords[2])
        return self.event