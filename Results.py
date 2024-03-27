# No Truce With The Furies
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pschitt.emission as em
import pschitt.vizualisation as viz
import pschitt.sky_objects as sky
import pschitt.geometry as geo
import pschitt.camera_image as ci
import numpy as np
import matplotlib.pyplot as plt
import math

with open('new_data.pkl', 'rb') as f:
    Primary_shower_data = pickle.load(f)
    Secondary_shower_data = pickle.load(f)
(particle_x, particle_y, particle_z, particle_en,
 parent_ids_m1, parent_ids_m2, particle_eta, particle_phi) = \
    (Primary_shower_data["particle_x"], Primary_shower_data["particle_y"], Primary_shower_data["particle_z"], Primary_shower_data["particle_en"],
     Primary_shower_data["parent_ids_m1"], Primary_shower_data["parent_ids_m2"], Primary_shower_data["particle_eta"], Primary_shower_data["particle_phi"])

(sec_particle_x, sec_particle_y, sec_particle_z, sec_particle_en,
 sec_parent_ids_m1, sec_parent_ids_m2, sec_particle_eta, sec_particle_phi) = \
    (Secondary_shower_data["sec_particle_x"], Secondary_shower_data["sec_particle_y"], Secondary_shower_data["sec_particle_z"], Secondary_shower_data["sec_particle_en"],
     Secondary_shower_data["sec_parent_ids_m1"], Secondary_shower_data["sec_parent_ids_m2"], Secondary_shower_data["sec_particle_eta"], Secondary_shower_data["sec_particle_phi"])

shower_color = 'black'
sec_color = '#d18580'
shower_colors = [shower_color] * len(particle_x)
sec_colors = [sec_color] * sum(len(particles) for particles in sec_particle_x)

"""
fig, ax_polar = plt.subplots(1, 1, subplot_kw=dict(projection='polar'), figsize=(10, 8))
for i in range(len(particle_x)):
    ax_polar.scatter(particle_phi[i], particle_eta[i], c=particle_en[i], cmap='viridis', s=50, alpha=0.7)
    if parent_ids_m1[i] != 0:
        ax_polar.plot([particle_phi[parent_ids_m1[i]], particle_phi[i]],
                      [particle_eta[parent_ids_m1[i]], particle_eta[i]], color='gray', linestyle='--')
    if parent_ids_m2[i] != 0:
        ax_polar.plot([particle_phi[parent_ids_m2[i]], particle_phi[i]],
                      [particle_eta[parent_ids_m2[i]], particle_eta[i]], color='gray', linestyle='--')

for j in range(len(sec_particle_x)):
    for k in range(len(sec_particle_x[0])):
        ax_polar.scatter(sec_particle_phi[j][k], sec_particle_eta[j][k], c=sec_particle_en[j][k], cmap='viridis', s=50, alpha=0.7)
        if sec_parent_ids_m1[j][k] != 0:
            ax_polar.plot([sec_particle_phi[j][sec_parent_ids_m1[j][k]], sec_particle_phi[j][k]],
                          [sec_particle_eta[j][sec_parent_ids_m1[j][k]], sec_particle_eta[j][k]], color='gray', linestyle='--')
        if sec_parent_ids_m2[j][k] != 0:
            ax_polar.plot([sec_particle_phi[j][sec_parent_ids_m2[j][k]], sec_particle_phi[j][k]],
                          [sec_particle_eta[j][sec_parent_ids_m2[j][k]], sec_particle_eta[j][k]], color='gray', linestyle='--')

ax_polar.set_title('Polar Coordinates')
cbar_polar = plt.colorbar(ax_polar.collections[0], ax=ax_polar, orientation='vertical')
cbar_polar.set_label('Energy')
"""

fig = plt.figure(figsize=(10, 8))
ax_3d = fig.add_subplot(111, projection='3d')
ax_3d.scatter(particle_x, particle_y, particle_z, c=particle_en, s=50, alpha=0.7)

for i in range(len(particle_x)):
    if parent_ids_m1[i] != 0:
        ax_3d.plot([particle_x[parent_ids_m1[i]], particle_x[i]],
                   [particle_y[parent_ids_m1[i]], particle_y[i]],
                   [particle_z[parent_ids_m1[i]], particle_z[i]], color='gray', linestyle='--')
    if parent_ids_m2[i] != 0:
        ax_3d.plot([particle_x[parent_ids_m2[i]], particle_x[i]],
                   [particle_y[parent_ids_m2[i]], particle_y[i]],
                   [particle_z[parent_ids_m2[i]], particle_z[i]], color='gray', linestyle='--')

for j in range(len(sec_particle_x)):
    ax_3d.scatter(sec_particle_x[j], sec_particle_y[j], sec_particle_z[j], c=sec_particle_en[j], s=50, alpha=0.7)

    for k in range(len(sec_particle_x[j])):
        if sec_parent_ids_m1[j][k] != 0:
            ax_3d.plot([sec_particle_x[j][sec_parent_ids_m1[j][k]], sec_particle_x[j][k]],
                       [sec_particle_y[j][sec_parent_ids_m1[j][k]], sec_particle_y[j][k]],
                       [sec_particle_z[j][sec_parent_ids_m1[j][k]], sec_particle_z[j][k]], color='gray', linestyle='--')
        if sec_parent_ids_m2[j][k] != 0:
            ax_3d.plot([sec_particle_x[j][sec_parent_ids_m2[j][k]], sec_particle_x[j][k]],
                       [sec_particle_y[j][sec_parent_ids_m2[j][k]], sec_particle_y[j][k]],
                       [sec_particle_z[j][sec_parent_ids_m2[j][k]], sec_particle_z[j][k]], color='gray', linestyle='--')
ax_3d.set_xlabel('X')
ax_3d.set_ylabel('Y')
ax_3d.set_zlabel('Z')
ax_3d.set_title('3D Coordinates')


cbar_ax_3d = plt.colorbar(ax_3d.collections[0], ax=ax_3d, orientation='vertical')
cbar_ax_3d.set_label('Color')


ax_3d.set_xlim(-25, 25)
ax_3d.set_ylim(-25, 25)
ax_3d.set_zlim(-25, 25)

print(f"Number of primary shower particles{len(particle_x)}")
num_points = len(particle_x) + sum([len(particles) for particles in sec_particle_x])
print(f"Number of shower particles: {num_points}")

par_x = [x for x in particle_x]
for sec_x in sec_particle_x:
    par_x.extend(sec_x)
par_y = [y for y in particle_y]
for sec_y in sec_particle_y:
    par_y.extend(sec_y)
par_z = [z for z in particle_z]
for sec_z in sec_particle_z:
    par_z.extend(sec_z)
shower = sky.shower()
shower.particles = np.array(list(zip(par_x, par_y, par_z)))

talt = math.radians(270)
taz = math.radians(0)
tel_normal = geo.altaz_to_normal(talt, taz)

tel1 = geo.Telescope([1, 1, 50], tel_normal)
tel2 = geo.Telescope([-1, 1, 50], tel_normal)
tel3 = geo.Telescope([-1, -1, 50], tel_normal)
tel4 = geo.Telescope([1, -1, 50], tel_normal)
tel5 = geo.Telescope([0, 0, 50], tel_normal)

altel = [tel1, tel2, tel3, tel4, tel5]

noise = 0
ci.array_shower_imaging(shower, altel, noise)
fig, axes = plt.subplots(1, len(altel), figsize=(20, 3))
for tel, ax in zip(altel, axes):
    ax = viz.display_camera_image(tel, s=4, ax=ax)
    ax.set_title("Signal sum = {}".format(tel.signal_hist.sum()))
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()
