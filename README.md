# castep-spack
This is a collection of spack packages to build CASTEP for HPC machines.


# Adding to spack 
## Spack 1.0 and above
Add the repo directly

`spack repo add https://github.com/pjpbyrne/castep-spack.git`

## Spack <1.0
You must first clone the repo

`git clone https://github.com/pjpbyrne/castep-spack.git`

and then add it as spack repo

`spack repo add ./castep-spack`

# Building CASTEP
You need to have the CASTEP distribution (eg CASTEP-26.11.tar.gz) in the current working directory. CASTEP can then be compiled with

`spack install castep@26.11`

# Options
This is a list of options supported by the CASTEP spack recipes. If required, libQUIP will also be compiled as a seperate package. 

    DLMG [true]                 false, true
        Compile with support for open boundary conditions

    GrimmeD3 [true]             false, true
        Compile with support for Grimme D3 dispersion scheme

    GrimmeD4 [true]             false, true
        Compile with support for Grimme D4 dispersion scheme

    OpenMP [true]               false, true
        Use OpenMP threading


    libXC [false]               false, true
        Build with libXC support

    mpi [true]                  false, true
        Build with MPI parallelism

    quip [false]                false, true
        Compile with support for QUIP interatomic potentials

    tools [true]                false, true
        Build Castep Tools

