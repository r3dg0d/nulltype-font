# Development shell. `nix-shell` (or `nix develop` via flake.nix) provides the full toolchain.
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (p: with p; [
      fonttools ufo2ft ufolib2 fontmake cu2qu brotli uharfbuzz freetype-py
      pytest pillow numpy cffsubr skia-pathops
    ]))
    pkgs.nodejs
    pkgs.harfbuzz
  ];
}
