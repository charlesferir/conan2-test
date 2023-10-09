from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.env import VirtualBuildEnv

class Hello(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    requires = "spdlog/1.12.0"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()
        ms = VirtualBuildEnv(self)
        ms.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
