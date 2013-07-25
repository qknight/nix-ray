{ python, pythonPackages, pythonDocs ? null }:

with import <nixpkgs> {};

let
  attrValues = lib.attrValues;
  optionals = lib.optionals;
  isPy26 = python.majorVersion == "2.6";
  isPy27 = python.majorVersion == "2.7";
in
{
  paths = [ python ] ++
          (optionals (pythonDocs != null) [ pythonDocs ]) ++
          (with pythonPackages;
           [ coverage
             elpy
             flake8
             ipdb
             ipdbplugin
             ipython
             jedi
             nose
             nose-cprof
             pylint
             recursivePthLoader
             sqlite3
             virtualenv
           ] ++
           (optionals isPy26
            [ ordereddict
              unittest2
            ]) ++
           (optionals isPy27
            [ ])) ++
           attrValues python.modules;
}
