## To start

1. Clone repository: `git clone <Link to this repository>`
2. Create a virtual environment: `python3 -m venv env`
3. Activate virtual environment `source env/bin/activate`
4. To install dependencies from requirements: `pip install -r requirements.txt`
   - Use command `pip list` whilst the virtual environment is activated to check that the dependencies are installed

To exit out of env CLI type `deactivate`
To create a requirements of pip installs use `pip freeze > requirements.txt`

### What is learned

#### Establishing a canvas

The first major component of creating this project is to establish a grid like structure to support a flat view of an image. This
is done by taking 4 points on an image and calculating the width and height from all those points so that openCV can identify them.
By doing this it can isolate the relevant data within the canvas for us to use later.

The logic for creating a 2D grid is fairly simple especially with the fact that we're working with a simple 4 sided shape(rectangle). This reminds me of working with 3D grids in Unreal engine where you also have to factor in the x, y and z axis for 3D shapes.
