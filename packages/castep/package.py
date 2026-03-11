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
#     spack install castep
#
# You can edit this file again by typing:
#
#     spack edit castep
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os
from pathlib import Path

class Castep(CMakePackage):
    """CASTEP is a leading code for calculating the properties of materials from first principles. Using density functional theory, it can simulate a wide range of properties of materials proprieties including energetics, structure at the atomic level, vibrational properties, electronic response properties etc. In particular it has a wide range of spectroscopic features that link directly to experiment, such as infra-red and Raman spectroscopies, NMR, and core level spectra."""

    homepage = "https://www.castep.org/"
    url =  "file://CASTEP-version.tar.gz"
    manual_download = True
    
    def url_for_version(self, version):
        # CASTEP-25.11.tar.gz
        abspath = Path.cwd() / "CASTEP-{}.tar.gz".format(version)
        return abspath.as_uri()
        
    maintainers("byornski")

    # Versions
    version("22.11", sha256="aca3fc2207c677561293585a4edaf233676a759c5beb8389cf938411226ef1f5")
    version("23.1",  sha256="7fba0450d3fd71586c8498ce51975bbdde923759ab298a656409280c29bf45b5")
    version("24.1",  sha256="97d77a4f3ce3f5c5b87e812f15a2c2cb23918acd7034c91a872b6d66ea0f7dbb")
    version("25.11", sha256="af6851a973ef83bbd725f6f33ff7616dd9d589bd75cf74cd106b13c3369167f6")
    version("25.12", sha256="e21177bfe4cb3f3d098b666c90771e3da2826503b002b8e325e3ca1e230cfc7d")
    version("26.11", sha256="cd38ec9e87fd92b91fe7910179acad6486ee57935832846959151ec406fb5fb6")

    # Depdencies

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("awk", type="build")

    # Perl for analysis scripts (dos.pl, dispersion.pl)
    depends_on("perl")

    # Python, for testing and utility scripts
    depends_on("python")
    depends_on("py-pip")
    depends_on("py-numpy")
    depends_on("py-scipy")
    
    # Library dependencies
    depends_on("lapack")
    depends_on("blas")
    depends_on("fftw-api@3")

    # List of the main variant options
    variant("mpi", description="Build with MPI parallelism", default=True)
    variant("libXC", description="Build with libXC support", default=False)
    variant("OpenMP", description="Use OpenMP threading", default=True)
    variant("GrimmeD3", description="Compile with support for Grimme D3 dispersion scheme", default=True)
    variant("GrimmeD4", description="Compile with support for Grimme D4 dispersion scheme", default=True)
    variant("DLMG", description="Compile with support for open boundary conditions", default=True)
    variant("quip", description="Compile with support for QUIP interatomic potentials", default=False)
    variant("tools", description="Build Castep Tools", default=True)
    variant("mace", description="Add support for MACE", default=False)
    
    # Optional dependencies
    depends_on("mpi", when="+mpi")
    depends_on("libquip", when="+quip")
    depends_on("libmace", when="+mace")
    

    # Patches
    patch("Fix-castepconv-strings-with-invalid-escape-character.patch")
    patch("Fixed-arguments-not-being-passed-to-python-scripts.patch", when="@=26.11")
    
    



    def cmake_args(self):
        args = [
            "-DBUILD=fast",
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_LIBXC", "libXC"),
            self.define_from_variant("WITH_OpenMP", "OpenMP"),
            self.define_from_variant("WITH_GRIMMED3", "GrimmeD3"),
            self.define_from_variant("WITH_GRIMMED4", "GrimmeD4"),
            self.define_from_variant("WITH_DLMG", "DLMG"),
            self.define_from_variant("WITH_MACE", "mace"),
        ]
        return args

    # Not implemented
    # Make
    # FOXCML
    # QUIP
