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
    today=$( date +%s )
    num=1
    filename=$today-log.txt
    while [ -e "$filename" ]; do
      filename='$s-$01d-log.txt'"$today""$(( ++num ))"
    done
    folder="logs/"
    mkdir -p "$folder"
    python -m run-aliens > "$folder$filename" &
    '';
}

