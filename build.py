from cpt.packager import ConanMultiPackager
from collections import defaultdict
import os


if __name__ == "__main__":
    builder = ConanMultiPackager(cppstds=[14],
                                archs=["x86_64"],
                                build_types=["Release"])
                              
    builder.add_common_builds(pure_c=False, shared_option_name=False)
    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++") # old ABI

    if os.environ['USE_MPI'] == 'with-mpi':
        builder.options['boost:without_mpi'] = False

    builder.run()

