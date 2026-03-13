# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libquip
#
# You can edit this file again by typing:
#
#     spack edit libquip
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path

class Libquip(MakefilePackage):
    """The QUIP package is a collection of software tools to carry out molecular dynamics simulations. It implements a variety of interatomic potentials and tight binding quantum mechanics, and is also able to call external packages, and serve as plugins to other software such as LAMMPS, CP2K and also the python framework ASE."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/libAtoms/QUIP"
    git = "https://github.com/libAtoms/QUIP.git"

    maintainers("pjpbyrne")
    license("UNKNOWN", checked_by="github_user1")

    version("0.10.2", tag="v0.10.2", commit="0d3372b3ae1472db3447dfa2b0c225f60333758a", submodules=True)

    variant("mpi", description="Compile with MPI parallelisation", default=True)
    
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("git", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("lapack")
    depends_on("blas")

    parallel = False
    targets = ['libquip']

    def edit(self, spec, prefix):
        lapack_blas = spec["lapack"].libs + spec["blas"].libs

        fortran = f"{spack_fc} -ffree-line-length-none"

        # arch/Makefile.spack
        config = {
            "CC": spack_cc, 
            "CXX": spack_cxx,
            "CPLUSPLUS": spack_cxx,
            "F77": fortran,
            "F90": fortran,
            "F95": fortran,
            "LINKER": fortran, # ldd?
            "FPP": f"{fortran} -E -x f95-cpp-input",
            "DEBUG": "",
            "OPTIM": "-O3",
            "export DEFAULT_MATH_LINKOPTS": lapack_blas.ld_flags,
            "AR_ADD": "src",
            #"export DEFAULT_MATH_LINKOPTS": "-llapack -lblas",
        }
        
        self.write_make_vars("arch/Makefile.spack", config)

        # arch/build/spack/Makefile.inc settings
        config_settings = {
            "MATH_LINKOPTS": lapack_blas.ld_flags, 
            "PYTHON":"/home/pb944/venv-excalibur/bin/python",
            "PIP":"/home/pb944/venv-excalibur/bin/pip",
            "EXTRA_LINKOPTS":"",
            "HAVE_CP2K":"0",
            "HAVE_VASP":"0",
            "HAVE_TB":"0",
            "HAVE_PRECON":"1",
            "HAVE_LOTF":"0",
            "HAVE_ONIOM":"0",
            "HAVE_LOCAL_E_MIX":"0",
            "HAVE_QC":"0",
            "HAVE_GAP":"1",
            "HAVE_DESCRIPTORS_NONCOMMERCIAL":"0",
            "HAVE_QR":"1",
            "HAVE_SCALAPACK":"0",
            "HAVE_THIRDPARTY":"0",
            "HAVE_FX":"0",
            "HAVE_SCME":"0",
            "HAVE_MTP":"0",
            "HAVE_MBD":"0",
            "HAVE_TTM_NF":"0",
            "HAVE_CH4":"0",
            "HAVE_NETCDF4":"0",
            "HAVE_MDCORE":"0",
            "HAVE_ASAP":"0",
            "HAVE_CGAL":"0",
            "HAVE_METIS":"0",
            "HAVE_LMTO_TBE":"0",
            "SIZEOF_FORTRAN_T":"2",
        }

        Path("./build/linux_x86_64_gfortran").mkdir(parents=True, exist_ok=True)
        self.write_make_vars("./build/linux_x86_64_gfortran/Makefile.inc", config_settings)

        makefile = FileFilter("Makefile")
        makefile.filter(r"\${PWD}",r"${QUIP_ROOT}")

    def write_make_vars(self, filename, vars):
        with open(filename,"w") as fd:
            for key, val in vars.items():
                fd.write(f"{key} = {val}\n")


        
    def setup_build_environment(self, env) -> None:
        env.set("QUIP_ARCH", "linux_x86_64_gfortran")
        env.set("QUIP_ROOT", self.build_directory)
