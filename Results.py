# No Truce With The Furies
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math

with open('N_80_data.pkl', 'rb') as f:
    shower_data = pickle.load(f)
(N80_particle_x, N80_particle_y, N80_particle_z, N80_particle_en, N80_particle_name,
 N80_parent_ids_m1, N80_parent_ids_m2) = \
    (shower_data["particle_x"], shower_data["particle_y"], shower_data["particle_z"], shower_data["particle_en"], shower_data["particle_name"],
     shower_data["parent_ids_m1"], shower_data["parent_ids_m2"])

with open('N_40_data.pkl', 'rb') as f:
    shower_data = pickle.load(f)
(N40_particle_x, N40_particle_y, N40_particle_z, N40_particle_en, N40_particle_name,
 N40_parent_ids_m1, N40_parent_ids_m2) = \
    (shower_data["particle_x"], shower_data["particle_y"], shower_data["particle_z"], shower_data["particle_en"], shower_data["particle_name"],
     shower_data["parent_ids_m1"], shower_data["parent_ids_m2"])

with open('C_80_data.pkl', 'rb') as f:
    shower_data = pickle.load(f)
(C80_particle_x, C80_particle_y, C80_particle_z, C80_particle_en, C80_particle_name,
 C80_parent_ids_m1, C80_parent_ids_m2) = \
    (shower_data["particle_x"], shower_data["particle_y"], shower_data["particle_z"], shower_data["particle_en"], shower_data["particle_name"],
     shower_data["parent_ids_m1"], shower_data["parent_ids_m2"])

with open('C_40_data.pkl', 'rb') as f:
    shower_data = pickle.load(f)
(C40_particle_x, C40_particle_y, C40_particle_z, C40_particle_en, C40_particle_name,
 C40_parent_ids_m1, C40_parent_ids_m2) = \
    (shower_data["particle_x"], shower_data["particle_y"], shower_data["particle_z"], shower_data["particle_en"], shower_data["particle_name"],
     shower_data["parent_ids_m1"], shower_data["parent_ids_m2"])

print(len(N80_particle_en))

N80_flattened_energies = [energy for sub_list in N80_particle_en for energy in sub_list if energy != 0]
N40_flattened_energies = [energy for sub_list in N40_particle_en for energy in sub_list if energy != 0]
C80_flattened_energies = [energy for sub_list in C80_particle_en for energy in sub_list if energy != 0]
C40_flattened_energies = [energy for sub_list in C40_particle_en for energy in sub_list if energy != 0]

plt.figure(figsize=(10, 10))
plt.hist(N80_flattened_energies, bins=50, density=False, alpha=0.7, label='80Gev proton to Nitrogen')
plt.hist(C80_flattened_energies, bins=50, density=False, alpha=0.7, label='80Gev proton to Carbon')
plt.legend()
plt.xlabel('Particle Energy (MeV)')
plt.ylabel('Frequency')
plt.title('Particle Energy Distribution in Proton to Nitrogen / Carbon Simulation')

C40_flattened_energies_sum = np.array(C40_flattened_energies).sum()
N40_flattened_energies_sum = np.array(N40_flattened_energies).sum()

C80_flattened_energies_sum = np.array(C80_flattened_energies).sum()
print(N40_flattened_energies_sum)
print(C40_flattened_energies_sum)
print(C40_flattened_energies[0])
plt.figure(figsize=(10, 10))
plt.hist(N40_flattened_energies, bins=50, density=False, alpha=0.7, label='40Gev proton to Nitrogen')
plt.hist(C40_flattened_energies, bins=50, density=False, alpha=0.7, label='40Gev proton to Carbon')
plt.xlabel('Particle Energy (MeV)')
plt.ylabel('Frequency')
plt.title('Particle Energy Distribution in Proton to Nitrogen / Carbon Simulation')

plt.legend()

N80_par_dict = {}
N80_par_name = []
for N80_name in N80_particle_name:
    N80_par_name.extend(N80_name)
for name in N80_par_name:

    if name in N80_par_dict:
        N80_par_dict[name] += 1
    else:
        N80_par_dict[name] = 1

N40_par_dict = {}
N40_par_name = []
for N40_name in N40_particle_name:
    N40_par_name.extend(N40_name)
for name in N40_par_name:

    if name in N40_par_dict:
        N40_par_dict[name] += 1
    else:
        N40_par_dict[name] = 1

C80_par_dict = {}
C80_par_name = []
for C80_name in C80_particle_name:
    C80_par_name.extend(C80_name)
for name in C80_par_name:

    if name in C80_par_dict:
        C80_par_dict[name] += 1
    else:
        C80_par_dict[name] = 1

C40_par_dict = {}
C40_par_name = []
for C40_name in C40_particle_name:
    C40_par_name.extend(C40_name)
for name in C40_par_name:

    if name in C40_par_dict:
        C40_par_dict[name] += 1
    else:
        C40_par_dict[name] = 1

labels1 = list(N80_par_dict.keys())
values1 = list(N80_par_dict.values())
labels2 = list(N40_par_dict.keys())
values2 = list(N40_par_dict.values())
labels3 = list(C80_par_dict.keys())
values3 = list(C80_par_dict.values())
labels4 = list(C40_par_dict.keys())
values4 = list(C40_par_dict.values())
plt.figure(figsize=(10, 4))
plt.stem(labels1, values1, linefmt='r-', label= "80GeV proton to Nitrogen")
plt.stem(labels3, values3, linefmt='b-', label= "80GeV proton to Carbon")
plt.legend()
plt.xlabel('Particle Name')
plt.ylabel('Frequency')
plt.title('Particle ID Distribution under 80Gev proton')

plt.figure(figsize=(10, 4))
plt.stem(labels2, values2, linefmt='r-', label= "40GeV proton to Nitrogen")
plt.stem(labels4, values4, linefmt='b-', label= "40GeV proton to Carbon")
plt.xlabel('Particle Name')
plt.ylabel('Frequency')
plt.title('Particle ID Distribution')
plt.xticks(rotation=90)
plt.legend()

fig = plt.figure(figsize=(10, 8))
ax_3d = fig.add_subplot(111, projection='3d')

for j in range(len(N80_particle_x)):
    ax_3d.scatter(N80_particle_x[j], N80_particle_y[j], N80_particle_z[j], c=N80_particle_en[j], s=50, alpha=0.7)

    for k in range(len(N80_particle_x[j])):
        if N80_parent_ids_m1[j][k] != 0:
            ax_3d.plot([N80_particle_x[j][N80_parent_ids_m1[j][k]], N80_particle_x[j][k]],
                       [N80_particle_y[j][N80_parent_ids_m1[j][k]], N80_particle_y[j][k]],
                       [N80_particle_z[j][N80_parent_ids_m1[j][k]], N80_particle_z[j][k]], color='gray', linestyle='--')
        if N80_parent_ids_m2[j][k] != 0:
            ax_3d.plot([N80_particle_x[j][N80_parent_ids_m2[j][k]], N80_particle_x[j][k]],
                       [N80_particle_y[j][N80_parent_ids_m2[j][k]], N80_particle_y[j][k]],
                       [N80_particle_z[j][N80_parent_ids_m2[j][k]], N80_particle_z[j][k]], color='gray', linestyle='--')
ax_3d.set_xlabel('X')
ax_3d.set_ylabel('Y')
ax_3d.set_zlabel('Z')
ax_3d.set_title('3D Coordinates of Proton to Nitrogen Simulation')


cbar_ax_3d = plt.colorbar(ax_3d.collections[0], ax=ax_3d, orientation='vertical')
cbar_ax_3d.set_label('Color')


ax_3d.set_xlim(-25, 25)
ax_3d.set_ylim(-25, 25)
ax_3d.set_zlim(-25, 25)


print(f"Number of  shower particles for N40{len(N40_flattened_energies)}")
print(f"Number of  shower particles for C40{len(C40_flattened_energies)}")

num_points = sum([len(particles) for particles in N80_particle_x])
print(f"Number of shower particles: {num_points}")

par_x = []
for sec_x in N80_particle_x:
    par_x.extend(sec_x)
par_y = []
for sec_y in N80_particle_y:
    par_y.extend(sec_y)
par_z = []
for sec_z in N80_particle_z:
    par_z.extend(sec_z)
N80_cross_section_particles = np.array(list(zip(par_x, par_y)))

par_x = []
for sec_x in N40_particle_x:
    par_x.extend(sec_x)
par_y = []
for sec_y in N40_particle_y:
    par_y.extend(sec_y)
par_z = []
for sec_z in N40_particle_z:
    par_z.extend(sec_z)

N40_cross_section_particles = np.array(list(zip(par_x, par_y)))

par_x = []
for sec_x in C80_particle_x:
    par_x.extend(sec_x)
par_y = []
for sec_y in C80_particle_y:
    par_y.extend(sec_y)
par_z = []
for sec_z in C80_particle_z:
    par_z.extend(sec_z)

C80_cross_section_particles = np.array(list(zip(par_x, par_y)))

par_x = []
for sec_x in C40_particle_x:
    par_x.extend(sec_x)
par_y = []
for sec_y in C40_particle_y:
    par_y.extend(sec_y)
par_z = []
for sec_z in C40_particle_z:
    par_z.extend(sec_z)

C40_cross_section_particles = np.array(list(zip(par_x, par_y)))

grid_size = 0.005
N80_grid_counts = np.zeros((200, 200), dtype=int)
for pos in N80_cross_section_particles:
    if abs(pos[0]) < 0.5 and abs(pos[1]) < 0.5:
        grid_x = int((pos[0] + 0.5) / grid_size)
        grid_y = int((pos[1] + 0.5) / grid_size)
        N80_grid_counts[grid_x, grid_y] += 1

N40_grid_counts = np.zeros((200, 200), dtype=int)
for pos in N40_cross_section_particles:
    if abs(pos[0]) < 0.5 and abs(pos[1]) < 0.5:
        grid_x = int((pos[0] + 0.5) / grid_size)
        grid_y = int((pos[1] + 0.5) / grid_size)
        N40_grid_counts[grid_x, grid_y] += 1

C80_grid_counts = np.zeros((200, 200), dtype=int)
for pos in C80_cross_section_particles:
    if abs(pos[0]) < 0.5 and abs(pos[1]) < 0.5:
        grid_x = int((pos[0] + 0.5) / grid_size)
        grid_y = int((pos[1] + 0.5) / grid_size)
        C80_grid_counts[grid_x, grid_y] += 1

C40_grid_counts = np.zeros((200, 200), dtype=int)
for pos in C40_cross_section_particles:
    if abs(pos[0]) < 0.5 and abs(pos[1]) < 0.5:
        grid_x = int((pos[0] + 0.5) / grid_size)
        grid_y = int((pos[1] + 0.5) / grid_size)
        C40_grid_counts[grid_x, grid_y] += 1

plt.figure(figsize=(10, 8))
plt.imshow(N80_grid_counts, aspect='auto', origin='lower', cmap='viridis', extent=[-0.5, 0.5, -0.5, 0.5])
plt.colorbar(label='Density')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cross-sectional Density Plot of 80GeV Proton to Nitrogen')

plt.figure(figsize=(10, 8))
plt.imshow(N40_grid_counts, aspect='auto', origin='lower', cmap='viridis', extent=[-0.5, 0.5, -0.5, 0.5])
plt.colorbar(label='Density')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cross-sectional Density Plot of 40GeV Proton to Nitrogen')

plt.figure(figsize=(10, 8))
plt.imshow(C80_grid_counts, aspect='auto', origin='lower', cmap='viridis', extent=[-0.5, 0.5, -0.5, 0.5])
plt.colorbar(label='Density')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cross-sectional Density Plot of 80GeV Proton to Carbon')

plt.figure(figsize=(10, 8))
plt.imshow(C40_grid_counts, aspect='auto', origin='lower', cmap='viridis', extent=[-0.5, 0.5, -0.5, 0.5])
plt.colorbar(label='Density')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cross-sectional Density Plot of 40GeV Proton to Carbon')

N80_sum_grid_counts = N80_grid_counts.sum(axis=0).reshape(1, -1)[0]
N40_sum_grid_counts = N40_grid_counts.sum(axis=0).reshape(1, -1)[0]
C80_sum_grid_counts = C80_grid_counts.sum(axis=0).reshape(1, -1)[0]
C40_sum_grid_counts = C40_grid_counts.sum(axis=0).reshape(1, -1)[0]
x = np.linspace(-0.5, 0.5, len(N80_sum_grid_counts))
plt.figure(figsize=(10, 8))
plt.plot(x, N80_sum_grid_counts, label= '80GeV N')
plt.plot(x, C80_sum_grid_counts, label= '80GeV C')
plt.title('X Cross-sectional Density Plot of Proton under 80geV to Carbon / Nirtogen Simulation ')
plt.ylabel('Number of particles')
plt.xlabel('X Coordinates / Meters')
plt.legend()

plt.figure(figsize=(10, 8))
plt.plot(x, N40_sum_grid_counts, color="g", label= '40GeV P to N')
plt.plot(x, C40_sum_grid_counts, color="r", label= '40GeV P to C')
plt.title('X Cross-sectional Density Plot of Proton under 40GeV to Carbon  / Nirtogen Simulation ')
plt.ylabel('Number of particles')
plt.xlabel('distance from the reference point (m)')
plt.legend()
plt.show()
