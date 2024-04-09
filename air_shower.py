# No Truce With The Furies
import pythia8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from SecondaryCascade import Cascade
import pickle

# Proton
pythia = pythia8.Pythia()
pythia.readString("Beams:idA = 2212")
pythia.readString("Beams:eA = 40")

# Nitrogen - 14
pythia.readString("Beams:idB = 1000070140")
pythia.readString("Beams:eB = 0")

pythia.readString("Beams:frameType = 3")
pythia.readString("HeavyIon:SigFitNGen = 0")
pythia.readString("HardQCD:all = on")

time = 1
number_of_showers = 3
pythia.init()
count = 0
sec = []

for events in range(10):
    pythia.next()
event = pythia.event

for particle in event:
    energy = (particle.px() ** 2 + particle.py() ** 2 + particle.pz() ** 2 + particle.m() ** 2) ** 0.5
    particle.xProd(particle.xProd() + particle.px() / energy * time)
    particle.yProd(particle.yProd() + particle.py() / energy * time)
    particle.zProd(particle.zProd() + particle.pz() / energy * time)
sec.append(event)
for idx, particle in enumerate(event):
    # Add particles and check for collision
    if particle.id() == 2212 and particle.isFinal():
        if count < 3:
            Cas = Cascade(event, idx, sec, number_of_showers, time)
            sec = Cas.Continue()
            count += 1

# Shower particles
particle_x = []
particle_y = []
particle_z = []
particle_en = []
parent_ids_m1 = []
parent_ids_m2 = []
particle_name = []

for m in range(len(sec)):
    particle_x.append([particle.xProd() for particle in sec[m]])
    particle_y.append([particle.yProd() for particle in sec[m]])
    particle_z.append([particle.zProd() for particle in sec[m]])
    particle_en.append([particle.e() for particle in sec[m]])
    particle_name.append([particle.name() for particle in sec[m]])

    parent_ids_m1.append([particle.mother1() for particle in sec[m]])
    parent_ids_m2.append([particle.mother2() for particle in sec[m]])


print(f"Number of primary shower particles{len(particle_x)}")
num_points = len(particle_x) + sum([len(particles) for particles in particle_x])
print(f"Number of shower particles: {num_points}")

plt.show()

shower_data = {'particle_x': particle_x, 'particle_y': particle_y,
                         'particle_z': particle_z, 'particle_en': particle_en, 'particle_name': particle_name,
                         'parent_ids_m1': parent_ids_m1, 'parent_ids_m2': parent_ids_m2}

with open('N_40_data.pkl', 'wb') as f:
    pickle.dump(shower_data, f)
