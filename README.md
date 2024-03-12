Hydrogen Atom Wave Function Animation
=====================================

This repository contains a Python script for calculating and animating the wave function of a hydrogen atom. It uses the `numpy`, `matplotlib`, and `scipy` libraries to perform the calculations and create the plot.

Radial and Angular Parts of the Wave Function
--------------------------------------------

The radial part of the wave function is given by the formula:

$$R_{n,l}(r) = \sqrt{ \left( \frac{2}{n a_0} \right)^3 \frac{(n-l-1)!}{2n[(n+l)!]^3} } e^{-\frac{r}{na_0}} \left( \frac{2r}{na_0} \right)^l L_{n-l-1}^{2l+1} \left( \frac{2r}{na_0} \right)$$

where $n$ is the principal quantum number, $l$ is the orbital angular momentum quantum number, $a_0$ is the Bohr radius, and $L_{n-l-1}^{2l+1}$ is the associated Laguerre polynomial.

The angular part of the wave function is given by the spherical harmonic functions:

$$Y_{l,m}(θ, ϕ) = (-1)^m \sqrt{ \frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_l^m(\cos(θ)) e^{i m \phi}$$

where $l$ is the orbital angular momentum quantum number, $m$ is the magnetic quantum number, $θ$ is the polar angle, $ϕ$ is the azimuthal angle, and $P_l^m$ is the associated Legendre polynomial.

Calculating the Wave Function and Probability Density
-------------------------------------------------------

The `compute_wave_function` function computes the wave function for a given set of quantum numbers $n$, $l$, and $m$ and a scale factor for the Bohr radius. It then calculates the probability density using the `compute_probability_density` function.

Plotting the Wave Function
--------------------------

The `plot_wave_function` function plots the probability density using `matplotlib`'s `imshow` function, which creates a 2D image of the 3D probability density. The `update` function is an animation function that updates the plot at each frame by computing the wave function and probability density for a given set of quantum numbers and a scale factor for the Bohr radius.

Running the Script
------------------

To run the script, simply execute the `main` function in a Python environment. The script will display a 3D plot of the wave function and probability density for the given set of quantum numbers and the Bohr radius scale factor. The plot will be animated with a time-dependent wave function.

Dependencies
------------

This script requires the following Python libraries:

* `numpy`
* `matplotlib`
* `scipy`

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for details.

Acknowledgments
---------------

The script includes the Bohr radius value from the `physical_constants` module of the `scipy` library. The `genlaguerre` and `lpmv` functions from the `scipy` library are used to calculate the associated Laguerre and Legendre polynomials, respectively. The `imshow` function from the `matplotlib` library is used to create the 2D image of the 3D probability density.
