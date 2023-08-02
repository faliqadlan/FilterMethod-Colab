## Filter Method for Solving Schrödinger Equation

The Filter Method is a numerical approach used to solve the stationary Schrödinger equation for quantum systems. It allows for the simultaneous computation of eigenfunctions and eigenvalues on a grid without the need for boundary-value conditions.

### Description

The paper "Filter method without boundary-value condition for simultaneous calculation of eigenfunction and eigenvalue of a stationary Schrödinger equation on a grid" presents the Filter Method. The method efficiently computes the eigenfunctions and eigenvalues of a given quantum system using a tridiagonal matrix and iterative filtering.

This implementation provided in the code examples is based on the Kronig-Penney potential, which is a model used to study the behavior of electrons in a periodic structure. It also includes an example for a single harmonic potential.

### Code Example - Kronig-Penney Potential

The first code example demonstrates how to calculate and plot the Kronig-Penney potential. It uses the `kronig_penney_potential` function to define the potential and then plots the potential versus x.

### Code Example - Energy Spectrum

The second code example shows how to calculate the energy spectrum of the Kronig-Penney potential. It uses the `eigenState` function to compute the eigenstates and eigenenergies for a range of energy values. The energy spectrum is then plotted, and the corresponding wave functions and probability distributions are visualized.

### Code Example - Single Harmonic Potential

The third code example illustrates how to calculate and plot the wave function, probability distribution, and energy level for a single harmonic potential. It uses the `eigenState` function with a single harmonic potential defined in the `potensial_harmonik` function.

### Usage in Google Colab

To run the code examples in Google Colab, you can use the provided Colab notebook: [Filter Method Colab Notebook](https://colab.research.google.com/github/faliqadlan/FilterMethod-Colab/blob/main/Filter_method_1_dimension.ipynb?authuser=3#scrollTo=H1sBDmVSlaOi). The notebook allows you to execute the code interactively and visualize the results.

Remember to set up the necessary environment and libraries in the Colab notebook before running the code.

### References

- [Filter Method journal](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.96.033302#:~:text=The%20paper%20presents%20a%20method%20for%20simultaneous%20computation,packet%20at%20the%20rate%20comparable%20to%20%CE%B4%20function.) (Filter method without boundary-value condition for simultaneous calculation of eigenfunction and eigenvalue of a stationary Schrödinger equation on a grid)