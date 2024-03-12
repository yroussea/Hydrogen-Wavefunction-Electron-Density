# Hydrogen Atom Wave Function Animation

![Figure_1](https://github.com/at0m741/Hydrogen-Wavefunction-Electron-Density/assets/20189027/d64d0e4d-aca2-4b16-b106-f2c9f9b3acdd)


This repository contains a Python script for calculating and animating the wave function of a hydrogen atom in a 3D plot. It utilizes the `numpy`, `matplotlib`, and `scipy` libraries for calculations and visualization.

The wave function of a quantum system describes its state and provides the probability distribution for observable measurements. For a hydrogen atom, the wave function can be expressed as a product of radial and angular parts:

$$[ \Psi(r, \theta, \phi) = R(r) Y(\theta, \phi) \]$$

where $(r)$, $(\theta)$, and $(\phi)$ are spherical coordinates, $(R(r))$ is the radial part, and $(Y(\theta, \phi))$ is the angular part.

## Radial and Angular Parts of the Wave Function

The radial part is given by:

$$[ R_{n,l}(r) = \sqrt{ \left( \frac{2}{n a_0} \right)^3 \frac{(n-l-1)!}{2n[(n+l)!]^3} } e^{-\frac{r}{na_0}} \left( \frac{2r}{na_0} \right)^l L_{n-l-1}^{2l+1} \left( \frac{2r}{na_0} \right) \]$$

where $\( n \)$ is the principal quantum number, $\( l \)$ is the orbital angular momentum quantum number, $\( a_0 \)$ is the Bohr radius, and $( L_{n-l-1}^{2l+1} \)$ is the associated Laguerre polynomial.

The angular part is given by spherical harmonic functions:

$$[ Y_{l,m}(\theta, \phi) = (-1)^m \sqrt{ \frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_l^m(\cos(\theta)) e^{i m \phi} \]$$

where $\( l \)$ is the orbital angular momentum quantum number, $\( m \)$is the magnetic quantum number, $\( \theta \)$ is the polar angle, $\( \phi \)$ is the azimuthal angle, and $\( P_l^m \)$ is the associated Legendre polynomial.

## Calculating the Wave Function and Probability Density

The `compute_wave_function` function calculates the wave function for specified quantum numbers $\( n, l, \)$ and $\( m \)$, along with a Bohr radius scale factor. It then computes the probability density using the `compute_probability_density` function.

## Plotting the Wave Function

The `plot_wave_function` function plots the probability density using `matplotlib`'s `imshow` function, creating a 2D image of the 3D probability density. The `update` function animates the plot by updating it at each frame with the wave function and probability density for given quantum numbers and a Bohr radius scale factor.

## Running the Script

Execute the `main` function in a Python environment to run the script. The output is a 3D plot of the wave function and probability density for the specified quantum numbers and Bohr radius scale factor. The plot is animated with a time-dependent wave function.

## Dependencies

This script requires the following Python libraries:

- `numpy`
- `matplotlib`
- `scipy`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

The script includes the Bohr radius value from the `physical_constants` module of the `scipy` library. The `genlaguerre` and `lpmv` functions from `scipy` are used to calculate associated Laguerre and Legendre polynomials, respectively. The `imshow` function from `matplotlib` is used to create the 2D image of the 3D probability density.
