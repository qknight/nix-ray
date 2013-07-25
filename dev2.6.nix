{ }:

with import <nixpkgs> {};

let
  python = python26;
  pythonPackages = python26Packages;
  base = import ./base.nix {
    inherit python pythonPackages;
    pythonDocs = pythonDocs.html.python26;
  };

in

buildEnv {
  name = "dev-env";
  ignoreCollisions = true;
  paths = [
    pythonPackages.genzshcomp
    pythonPackages.plumbum
  ] ++ base.paths;
}