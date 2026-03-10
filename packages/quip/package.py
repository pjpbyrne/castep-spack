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
#     spack install quip
#
# You can edit this file again by typing:
#
#     spack edit quip
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path

class Quip(MakefilePackage):
    """The QUIP package is a collection of software tools to carry out molecular dynamics simulations. It implements a variety of interatomic potentials and tight binding quantum mechanics, and is also able to call external packages, and serve as plugins to other software such as LAMMPS, CP2K and also the python framework ASE."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/libAtoms/QUIP"
    url = "https://github.com/libAtoms/QUIP/archive/refs/tags/v0.9.14.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.9.14", sha256="587f7acce6c0538ec50f5d725db146f217fa16564e6851bc3f11e217cc048656")
    version("0.9.13", sha256="71c868adb516dd4da645320f59b52808191c032fb790a5f7d6b61ccb96493ee2")
    version("0.9.12", sha256="df228d5e9799adc30111962e4cdc7e3a95124fe68b9ac9bf654957543327e281")
    version("0.9.11", sha256="aa12458973de2cc69aa8f5a68fd3e6b3ad57d04ee74ccb923419f2c2597803ab")
    version("0.9.10", sha256="c03505779634459ea0ba3f7ddc120ac17f0546d44dc9b5096f008f1c3c6620ef")

    variant("mpi", description="Compile with MPI parallelisation", default=True)
    
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("git", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("lapack")
    depends_on("blas")
    
    def edit(self, spec, prefix):
        # arch/Makefile.spack
        config = {
            "CC":spack_cc, 
            "CXX":spack_cxx,
            "CPLUSPLUS":spack_cxx,
            "F77":spack_f77,
            "F90":spack_fc,
            "F95":spack_fc,
            "LINKER":spack_fc, # ldd?
            "FPP": f"{spack_fc} -E -x f95-cpp-input",
            "DEBUG": "",
            "OPTIM": "-O3",
            #"export DEFAULT_MATH_LINKOPTS": spec["blas"].libs.ld_flag + " " + spec["lapack"].libs.ld_flag,
            "export DEFAULT_MATH_LINKOPTS": "-llapack -lblas",
        }
        
        self.write_make_vars("arch/Makefile.spack", config)

        # arch/build/spack/Makefile.inc settings
        config_settings = {
            "MATH_LINKOPTS":"-llapack -lblas",
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

        Path("arch/build/spack").mkdir(parents=True, exist_ok=True)
        self.write_make_vars("arch/build/spack/Makefile.inc", config_settings)

    def write_make_vars(self, filename, vars):
        with open(filename,"w") as fd:
            for key, val in vars.items():
                fd.write(f"{key} = {val}\n")


        
    def setup_build_environment(self, env) -> None:
        env.set("QUIP_ARCH", "spack")
        env.set("QUIP_ROOT", ".")
