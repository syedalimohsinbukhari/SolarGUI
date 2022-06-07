# SolarGUI

A program which contains information about the solar system planets, moon, pluto, Sun, and more.

![GitHub top language](https://img.shields.io/github/languages/top/AstrophysicsAndPython/SolarGUI)
![Lines of code](https://img.shields.io/tokei/lines/github/AstrophysicsAndPython/SolarGUI)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/AstrophysicsAndPython/SolarGUI)
![GitHub](https://img.shields.io/github/license/AstrophysicsAndPython/SolarGUI)
## What it is?

The SolarGUI is a fun little project aimed to gather planetary (and other) information. See the values of various
physical parameters in standard (SI, CGS) units and celestial equivalencies.

### Support

Currently, the SolarGUI application is tested with **Python** `v3.7`, `3.8` and `3.9`.

## How to install?

### pip

The SolarGUI is available via `pip`. Simply use the command,

`pip install SolarGUI==0.1.4`

### wheel file

The wheel can also be downloaded from
this [wheel](https://github.com/AstrophysicsAndPython/SolarGUI/releases/download/v0.1.4/SolarGUI-0.1.4-py3-none-any.whl)
link and installed via

`pip install [download_directory]/SolarGUI-0.1.4-py3-none-any.whl`

Once the SolarGUI has been installed, you can simply launch it from the terminal/installation environment via,

`SolarGUI`

The frontend of SolarGUI provides several buttons for stars, planets, moons, and other celestial objects.

![img.png](images/SolarGUI__frontEnd.png)

Each button will open a new window with access to physical and orbital buttons which contain information regarding the
particular objects' parameters,

![img.png](images/SolarGUI__propertyView.png)

Clicking on the desired button will trigger a frame for the particular properties of the celestial object.

For example, if the user selects `Physical Parameters`, the following parameters will be listed

1. age,
2. mass,
3. radius,
4. volume,
5. density,
6. surface area,
7. surface gravity, and
8. escape velocity.

![img.png](images/SolarGUI__physicalParameters.png)

Similarly, clicking on the `Orbital Parameters` will trigger the frame with orbital parameters in it, such as

1. Semi-major axis
2. Eccentricity
3. Perihelion distance
4. Apehelian distance
5. Orbital period
6. Average orbital speed
7. Mean anomaly
8. Inclination
9. Longitude of ascending node
10. Argument of perihelion, and
11. Axial tilt.

![img.png](images/SolarGUI__orbitalParameters.png)

The dropdown menus will show various other units of measures. The equivalencies button on the top right can be used to
see the equivalent values for other celestial objects.

![img.png](images/SolarGUI__equivalencies.png)

## TODO

- [x] Add Sun, Pluto and Moon with the Solar planets.
- [ ] Calculate physical properties via formulae, e.g., volume, density, surface_area, surface_gravity.
  - [x] volume
  - [x] density
  - [x] surface_area
  - [x] surface_gravity
  - [ ] others
- [x] Add a comparison button/dropdown menu to check the values with respect to Earth/Jupiter/Sun.
  - [x] Add planet level equivalencies.
- [x] Segregate moons, dwarf planets, planets and other type of celestial objects.
- [x] Design adjustments of the GUI
  - [x] Adjust column widths in GUI.
  - [x] Adjust the minimize/maximize window and widgets.
- [x] Separate button/menu for physical/orbital and other parameters.
- [ ] Some interesting plots (optional).
- [ ] Random facts button.
- [ ] Add citations
- [ ] Add a section of papers that study different properties of the celestial objects.
