import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import scipy
from scipy import special
from scipy.constants import physical_constants

def radial_function(n, l, r, a0):
    #Latex version :
    #R_{n,l}(r) = \sqrt{ \left( \frac{2}{n a_0} \right)^3 \frac{(n-l-1)!}{2n[(n+l)!]^3} } e^{-\frac{r}{na_0}} \left( \frac{2r}{na_0} \right)^l L_{n-l-1}^{2l+1} \left( \frac{2r}{na_0} \right)

    laguerre = scipy.special.genlaguerre(n-l-1, 2*l+1)
    p = 2*r/(n*a0)
    constant_factor = np.sqrt((2/(n*a0))**3 * np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l)))

    return constant_factor * np.exp(-p/2) * p**l * laguerre(p)

def angular_function(l, m, theta, phi):
    #latex version :
    #Y_{l,m}(\theta, \phi) = (-1)^m \sqrt{ \frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_l^m(\cos(\theta)) e^{i m \phi}

    legendre = scipy.special.lpmv(m, l, np.cos(theta))
    constant_factor = ((-1)**m) * np.sqrt((2*l+1)/(4*np.pi) * np.math.factorial(l-m)/np.math.factorial(l+m))

    return constant_factor * legendre * np.exp(1j*m*phi)

def compute_wave_function(n, l, m, a_0_scale_factor, t=0):
    a0 = a_0_scale_factor * physical_constants['Bohr radius'][0] * 1e10
    grid_extent = 480
    grid_resolution = 680
    z = np.linspace(-grid_extent, grid_extent, grid_resolution)
    z, x = np.meshgrid(z, z)
    eps = np.finfo(float).eps

    if n < 0 or l < 0 or m < 0:
        raise ValueError("n, l, and m must be non-negative")

    if n < l + 1:
        raise ValueError("n must be greater than or equal to l + 1")

    psi_rl = radial_function(n, l, np.sqrt(x**2 + z**2 + eps), a0)
    psi_lm = angular_function(l, m, np.arctan2(np.sqrt(x**2 + z**2), z), np.arctan2(x, z))

    psi = psi_rl * psi_lm
    print(psi)
    return psi

def compute_probability_density(psi):
    return abs(psi)**2

def plot_wave_function(psi, probability_density, n, l, m, ax):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Hydrogen Electron Wave Function")
    ax.set_xlabel("x (pm)")
    ax.set_ylabel("z (pm)")
        #add color bar
    ax = plt.gca()
    
    ax.imshow(probability_density, cmap='magma', extent=(-480, 480, -480, 480))

def update(frame, args, a_0_scale_factor):
    global psi, probability_density
    t = frame * 0.01
    n, l, m = args
    psi = compute_wave_function(n, l, m, a_0_scale_factor, t)
    probability_density = compute_probability_density(psi)
    plot_wave_function(psi, probability_density, n, l, m, ax)

def main():
    global ax

    a_0_scale_factor = 20

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    #bar = plt.colorbar(ax.imshow(probability_density, cmap='magma', extent=(-480, 480, -480, 480)))
    args = (4, 3, 0)
    ani = animation.FuncAnimation(fig, update, frames=1000, interval=10, blit=False, fargs=(args, a_0_scale_factor,))

	# etc.

    plt.show()

if __name__ == "__main__":
    main()