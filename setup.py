from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension(
        name="pygenalg.algorithm",
        sources=["bindings/pygenalg/algorithm.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.core.fitness",
        sources=["bindings/pygenalg/core/fitness.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.core.termination",
        sources=["bindings/pygenalg/core/termination.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.core.options",
        sources=["bindings/pygenalg/core/options.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.operators.crossover",
        sources=["bindings/pygenalg/operators/crossover.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.operators.mutation",
        sources=["bindings/pygenalg/operators/mutation.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.operators.selection",
        sources=["bindings/pygenalg/operators/selection.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.population",
        sources=["bindings/pygenalg/population.pyx"],
        include_dirs=["src"]
    ),
    Extension(
        name="pygenalg.individual",
        sources=["bindings/pygenalg/individual.pyx"],
        include_dirs=["src"]
    )
]

setup(
    name="py-genalg",
    version="0.0.1",
    ext_modules=cythonize(extensions),
    python_requires=">=3.8"
)
