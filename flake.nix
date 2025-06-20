{
  description = "Experiements with python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    # Define 'forAllSystems' for properties that shall be build for x86_64 *and* aarch64
    systems = ["x86_64-linux" "aarch64-linux"];
    forAllSystems = nixpkgs.lib.genAttrs systems;
    pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
  in {
    packages = forAllSystems (system: {
      pyflame = pkgs.${system}.python3Packages.buildPythonPackage rec {
        pname = "pyflame";
        version = "0.3.2";
        pyproject = true;

        src = pkgs.${system}.fetchPypi {
          inherit pname;
          inherit version;
          hash = "sha256-j15RRngb3e84ezMXCyfPxb6Qf64BeVFttWSnI/MOUSE=";
        };

        nativeBuildInputs = [pkgs.${system}.python3Packages.setuptools];

        dontCheckRuntimeDeps = true;
        doCheck = false;
      };
    });

    devShells = forAllSystems (system: {
      default = pkgs.${system}.mkShell {
        buildInputs = with pkgs.${system}; [
          # basics
          gitMinimal

          #python
          python3
          pyright
          ruff
          python3Packages.ipykernel
          python3Packages.matplotlib
          self.packages.${system}.pyflame

          # nix
          nil
          alejandra
        ];
      };
    });
  };
}
