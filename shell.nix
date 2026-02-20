let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.hatchling
    pkgs.python312Packages.uv
    pkgs.python312Packages.torch
    pkgs.python312Packages.datasets
    pkgs.python312Packages.torchvision
    pkgs.python312Packages.pygame
  ];
  shellHook = ''
    python -m venv .venv
    source .venv/bin/activate
    pip install hatch
    hatch build -t wheel
    python -m run-aliens
    '';
}

