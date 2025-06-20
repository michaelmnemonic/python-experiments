{
  description = "Experiements with python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    # Define 'forAllSystems' for properties that shall be build for x86_64 *and* aarch64
    systems = ["x86_64-linux" "aarch64-linux"];
    forAllSystems = nixpkgs.lib.genAttrs systems;
    pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
  in {

    devShells = forAllSystems (system: {
      default = pkgs.${system}.mkShell {
        buildInputs = with pkgs.${system}; [
          gitMinimal
          python3
          pyright
          ruff
          python312Packages.ipykernel
        ];
      };
    });
  };
}
