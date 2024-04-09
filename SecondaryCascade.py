# No Truce With The Furies
import pythia8
import numpy as np
from scipy.spatial.transform import Rotation


def Motion(event, t):
    for particle in event:
        energy = (particle.px() ** 2 + particle.py() ** 2 + particle.pz() ** 2 + particle.m() ** 2) ** 0.5
        particle.xProd(particle.xProd() + particle.px() / energy * t)
        particle.yProd(particle.yProd() + particle.py() / energy * t)
        particle.zProd(particle.zProd() + particle.pz() / energy * t)


class Cascade:
    def __init__(self, primary_event, idx, sec, number_of_showers, time):
        self.primary_event = primary_event
        self.idx = idx
        self.sec = sec
        self.number_of_showers = number_of_showers - 1
        self.time = time
        self.count = 0
        pythia = pythia8.Pythia()
        pythia.readString("Beams:idA = 2212")
        pythia.readString(f"Beams:eA = {self.primary_event[idx].e()}")

        pythia.readString("Beams:idB = 1000070140")
        pythia.readString("Beams:eB = 0")

        pythia.readString("Beams:frameType = 3")
        pythia.readString("HeavyIon:SigFitNGen = 0")
        pythia.readString("HardQCD:all = on")

        pythia.init()
        for events in range(5):
            pythia.next()
        self.event = pythia.event

        # transformation matrix
        axis = [self.primary_event[idx].px(), self.primary_event[idx].py(), self.primary_event[idx].pz()]
        self.rotation_matrix = Rotation.from_rotvec(axis).as_matrix()

    def Transformation(self):

        particle_x = [particle.xProd() for particle in self.event]
        particle_y = [particle.yProd() for particle in self.event]
        particle_z = [particle.zProd() for particle in self.event]
        particle_t = np.array([particle_x, particle_y, particle_z])
        rotated_points = np.dot(self.rotation_matrix, particle_t)

        for i in range(rotated_points.shape[1]):
            rotated_points[0, i] += self.primary_event[self.idx].xProd()
            rotated_points[1, i] += self.primary_event[self.idx].yProd()
            rotated_points[2, i] += self.primary_event[self.idx].zProd()

        for particle, new_coords in zip(self.event, rotated_points.T):
            particle.xProd(new_coords[0])
            particle.yProd(new_coords[1])
            particle.zProd(new_coords[2])

        particle_px = [particle.px() for particle in self.event]
        particle_py = [particle.py() for particle in self.event]
        particle_pz = [particle.pz() for particle in self.event]
        particle_pt = np.array([particle_px, particle_py, particle_pz])
        rotated_PT = np.dot(self.rotation_matrix, particle_pt)

        for particle, new_PT in zip(self.event, rotated_PT.T):
            particle.px(new_PT[0])
            particle.py(new_PT[1])
            particle.pz(new_PT[2])

    def Further_process(self):

        self.sec.append(self.event)

        if self.number_of_showers == 1:
            return self.sec

        else:
            for idx, particle in enumerate(self.event):
                # Add particles and check for collision
                if particle.id() == 2212 and particle.isFinal():
                    if self.count < 3:
                        Cas = Cascade(self.event, idx, self.sec, self.number_of_showers, self.time)
                        self.sec = Cas.Continue()
                        self.count += 1

            for sec_event in self.sec:
                Motion(sec_event, self.time)
            return self.sec

    def Continue(self):
        self.Transformation()
        self.sec = self.Further_process()
        return self.sec
