import warnings
warnings.filterwarnings("ignore")
import  parsing
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Button, Slider
import scipy
from scipy import special
from scipy.constants import physical_constants

def radial_function(n, l, r, a0):
    #Latex version :
    #R_{n,l}(r) = \sqrt{ \left( \frac{2}{n a_0} \right)^3 \frac{(n-l-1)!}{2n[(n+l)!]^3} } e^{-\frac{r}{na_0}} \left( \frac{2r}{na_0} \right)^l L_{n-l-1}^{2l+1} \left( \frac{2r}{na_0} \right)

    laguerre = scipy.special.genlaguerre(int(n-l-1), 2*l+1)
    p = 2*r/(n*a0)
    constant_factor = np.sqrt((2/(n*a0))**3 * np.math.gamma(n-l)/(2*n*np.math.gamma(n+l+1)))

    return constant_factor * np.exp(-p/2) * p**l * laguerre(p)

def angular_function(l, m, theta, phi):
    #latex version :
    #Y_{l,m}(\theta, \phi) = (-1)^m \sqrt{ \frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_l^m(\cos(\theta)) e^{i m \phi}

    legendre = scipy.special.lpmv(m, l, np.cos(theta))
    constant_factor = ((-1)**m) * np.sqrt((2*l+1)/(4*np.pi) * np.math.gamma(l-m+1)/np.math.gamma(l+m+1))

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
    # print(psi)

    return psi

def compute_probability_density(psi):
    return abs(psi)**2

def plot_wave_function(psi, probability_density, ax, color='magma'):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Hydrogen Electron Wave Function")
    ax.set_xlabel("x (pm)")
    ax.set_ylabel("z (pm)")
        #add color bar
    # ax = plt.gca()
    
    ax.imshow(probability_density, cmap=color, extent=(-480, 480, -480, 480))

def get_step(frame, max_frame, steps):
    def percent():
        return frame / max_frame * 100
    def from_to(x):
        v = int(percent() // x)
        return (np.array(steps[v]), np.array(steps[v + 1]))
    x = 100 / (len(steps) - 1)
    a_from, a_to = from_to(x)
    a_smooth = (a_to - a_from) / x
    return (a_from + a_smooth * (frame % x))


def update(frame, args, max_frame):
    global psi, probability_density
    t = frame * 0.01

    if len(args) > 1:
        n, l, m, a_0_scale_factor = get_step(frame, max_frame, args)
    probability_density = compute_probability_density(psi)
    plot_wave_function(psi, probability_density, ax)


def slider(ax_f, ax, fig):
    def draw(n, l, m, scale):
        psi = compute_wave_function(n, l, int(m), scale)
        probability_density = compute_probability_density(psi)
        plot_wave_function(psi, probability_density, ax_f)

    init_W = 10
    axW = fig.add_axes([0.7, 0.2, 0.0225, 0.63]) 
    axX = fig.add_axes([0.78, 0.2, 0.0225, 0.63]) 
    axY = fig.add_axes([0.86, 0.2, 0.0225, 0.63]) 
    axZ = fig.add_axes([0.94, 0.2, 0.0225, 0.63]) 
    W_slider = Slider(
        ax=axW,
        label='n',
        valmin=0.1,
        valmax=init_W,
        valinit=init_W,
        orientation="vertical"
    )
    X_slider = Slider(
        ax=axX,
        label='l',
        valmin=0,
        valmax=init_W,
        valinit=0,
        orientation="vertical"
    )
    Y_slider = Slider(
        ax=axY,
        label='m',
        valmin=0,
        valmax=init_W,
        valinit=0,
        orientation="vertical"
    )
    Z_slider = Slider(
        ax=axZ,
        label='scale',
        valmin=1,
        valmax=10,
        valinit=4,
        orientation="vertical"
    )
    Y_slider.valmax = X_slider.val
    X_slider.valmax = W_slider.val - 1
    def Wupdate(val):
        X_slider.valmax = W_slider.val - 1
        X_slider.eventson = False
        X_slider.set_val(min(X_slider.val, W_slider.val - 1))
        X_slider.eventson = True
        Y_slider.valmax = X_slider.val
        Y_slider.eventson = False
        Y_slider.set_val(min(Y_slider.val, X_slider.val))
        Y_slider.eventson = True
        draw(W_slider.val, X_slider.val, Y_slider.val, Z_slider.val)
        fig.canvas.draw()

    def Xupdate(val):
        Y_slider.valmax = X_slider.val
        Y_slider.eventson = False
        Y_slider.set_val(min(Y_slider.val, X_slider.val))
        Y_slider.eventson = True
        draw(W_slider.val, X_slider.val, Y_slider.val, Z_slider.val)
        fig.canvas.draw()

    def Yupdate(val):
        draw(W_slider.val, X_slider.val, Y_slider.val, Z_slider.val)
        fig.canvas.draw()

    def Zupdate(val):
        draw(W_slider.val, X_slider.val, Y_slider.val, Z_slider.val)
        fig.canvas.draw()

    W_slider.on_changed(Wupdate)
    X_slider.on_changed(Xupdate)
    Y_slider.on_changed(Yupdate)
    Z_slider.on_changed(Zupdate)
    draw(W_slider.val, X_slider.val, Y_slider.val, Z_slider.val)




def main():
    global ax

    plt.style.use('dark_background')
    print(sys.argv)

    if not (len(sys.argv) > 1 and sys.argv[1] == "slider"):
        fig, ax = plt.subplots(figsize=(12, 10))
        max_frame = 200
        steps = parsing.open_file()
        ani = animation.FuncAnimation(fig, update, frames=max_frame, interval=10, blit=False, fargs=(steps, max_frame,))

    else:
        fig, (ax, ax2) = plt.subplots(1,2,
            figsize=(16, 10),
            gridspec_kw={'width_ratios': [2, 1]})
        ax2.set_aspect('equal')
        ax2.axis('off')

        max_frame = 100
        slider(ax, ax2, fig)

    plt.show()


if __name__ == "__main__":
    main()
