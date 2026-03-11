# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install libmace
#
# You can edit this file again by typing:
#
#     spack edit libmace
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libmace(CMakePackage):
    """Fast and accurate machine learning interatomic potentials with higher order equivariant message passing. """

    homepage = "https://github.com/ACEsuit/mace"
    url = "https://github.com/stenczelt/libmace/archive/refs/tags/v25.04.1.tar.gz"

    maintainers("pjpbyrne")
    license("MIT", checked_by="pjpbyrne")

    version("25.04.1", sha256="a34496738e7aafe570b5b0ecca28e054efe61f06ac9e5d53e1ec3afe52b77272")
    version("25.03.2-libtorch2.6.0", sha256="a353ae6eaec9f42d725d649103fa0308d4c41ddeb4ff8298abdb99e7e14af923")
    version("25.03.2-libtorch2.4.1", sha256="777d1cfce97749fabde1a7461a35d908ca0ea1e6b14cad53ecbbf3f5b4fecdb2")
    version("25.03.2", sha256="ccddc5d963771deaf1dc3df8ab1a662c750f1287457b78049a791e8f9902c14a")
    version("25.03.1-libtorch2.6.0", sha256="396152fb91cec5ef68709f5bda4867a4e146c51c94bfaa756263aa7c9f554268")
    version("25.03.1-libtorch2.4.1", sha256="4441223619c537102c3d45150320c7cf9140dcf17ed210abf919ca207e1e090f")
    version("25.03.1", sha256="5c473b9c0aaafef3ae2a3ea928ee5697b6c243b5525c83dceb06f0bdbb2f2b73")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("py-torch")    
    
