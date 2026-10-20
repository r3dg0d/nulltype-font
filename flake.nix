{
  description = "NullType — An original chamfered monospace for terminals and code (OFL-1.1 fonts, MIT tooling)";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" ];
      forAll = f: nixpkgs.lib.genAttrs systems (s: f nixpkgs.legacyPackages.${s});
      pyEnv = pkgs: pkgs.python3.withPackages (p: with p; [
        fonttools ufo2ft ufolib2 fontmake cu2qu brotli uharfbuzz freetype-py
        pytest pillow numpy cffsubr skia-pathops
      ]);
    in {
      packages = forAll (pkgs: rec {
        nulltype = pkgs.stdenvNoCC.mkDerivation {
          pname = "nulltype-font";
          version = "1.000";
          src = self;
          nativeBuildInputs = [ (pyEnv pkgs) ];
          SOURCE_DATE_EPOCH = "1792800000";
          buildPhase = "python3 tools/build.py";
          doCheck = true;
          checkPhase = "python3 -m pytest -q tests";
          installPhase = ''
            install -Dm644 -t $out/share/fonts/truetype fonts/ttf/*.ttf fonts/variable/*.ttf
            install -Dm644 -t $out/share/fonts/opentype fonts/otf/*.otf
            install -Dm644 -t $out/share/fonts/woff2 fonts/woff2/*.woff2 fonts/variable/*.woff2
            install -Dm644 OFL.txt $out/share/licenses/nulltype-font/OFL.txt
          '';
          meta = with pkgs.lib; {
            description = "An original chamfered monospace for terminals and code: 9 weights + italics, source-preserving ligatures, full box drawing and Powerline.";
            homepage = "https://github.com/r3dg0d/nulltype-font";
            license = licenses.ofl;
            platforms = platforms.all;
          };
        };
        default = nulltype;
      });
      devShells = forAll (pkgs: {
        default = pkgs.mkShell { packages = [ (pyEnv pkgs) pkgs.nodejs pkgs.harfbuzz pkgs.opentype-sanitizer ]; };
      });
    };
}
