# Abaqus Wave Propagation Simulation

This Python script automates a 3D explicit dynamics simulation in Abaqus to model wave propagation in an aluminum plate. It is designed for studying elastic wave behavior (e.g., Lamb waves) in structural health monitoring, non-destructive testing (NDT), or acoustics applications.

## Key Features
- **Geometry**: Creates a 100x100x1 mm 3D plate and partitions it for refined analysis.
- **Material**: Uses aluminum (density = 2.5e-09 ton/mm³, Young’s modulus = 62,000 MPa, Poisson’s ratio = 0.33).
- **Loading**: Applies a dynamic concentrated force with a custom oscillatory amplitude (`Amp-1`) at the "front" vertex.
- **Boundary Conditions**: Fully constrains one face (U1=U2=U3=0).
- **Output**: Tracks displacement history at a "sensor" vertex and generates field outputs.
- **Mesh**: Uses C3D8R elements (8-node linear bricks) for efficient explicit analysis.

## Usage
1. **Requirements**: Abaqus/CAE 2021+ with Python scripting support.
2. **Run Script**: Execute via Abaqus CAE using `abaqus cae script=wave.py` or run directly in the CAE Python console.
3. **Results**: 
   - Automatically submits job `Job-1` and opens the ODB.
   - Visualizes wave propagation via contour plots (U magnitude/U1 component).
   - Sensor displacement data is saved in history outputs for post-processing.

## Customizable Parameters
- **Geometry**: Modify sketch dimensions (`s.rectangle`) or extrude depth.
- **Material**: Adjust density/elastic properties in `Material` section.
- **Load Profile**: Edit `Amp-1` data points for different excitation signals.
- **Time Step**: Control simulation duration (`timePeriod`) in `ExplicitDynamicsStep`.
- **Mesh Size**: Change seed size (`size=1.0`) in `seedPartInstance`.

## Notes
- Paths like `'Y:/Job-1.odb'` may need adjustment for your system.
- For large models, consider parallelization (adjust `numCpus` in `Job`).
- Use Abaqus Visualization module to export animations or XY data from history outputs.

![wave full (3)](https://github.com/user-attachments/assets/752b0c66-c977-4b7b-9223-79d3a80930d5)

