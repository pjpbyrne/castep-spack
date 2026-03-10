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

    # Add  versions here.
    version("25.11", sha256="3cefc4f8cc218c5b2d24cc9efc65896b2aa2386518c24105124398bc0e6e24b7")
    version("26.11", sha256="4905591d3ea1bd6ec622bf9e5f64eae310f03466e54bf564eb34ec5fa2f19372")

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

    # Optional dependencies
    depends_on("mpi", when="+mpi")
    depends_on("libquip", when="+quip")

    def cmake_args(self):
        args = [
            "-DBUILD=fast",
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_LIBXC", "libXC"),
            self.define_from_variant("WITH_OpenMP", "OpenMP"),
            self.define_from_variant("WITH_GRIMMED3", "GrimmeD3"),
            self.define_from_variant("WITH_GRIMMED4", "GrimmeD4"),
            self.define_from_variant("WITH_DLMG", "DLMG"),
        ]
        return args

    # Not implemented
    # Make
    # FOXCML
    # QUIP
