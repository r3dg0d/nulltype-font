# NullType design notes

NullType is a **600-unit monospace** (cap 700, x-height 500, line cell 1200) built from stroke skeletons with 45° chamfered corners.

* Every segment is swept by an upright rectangular pen. Stems are 18 units at Thin, 72 at Regular, 140 at Black.
* **Bars thin relative to stems** above Regular (92% → 80%) to keep horizontal counters (`e a s 8 B`) open. This is a weight-dependent contrast model, not a uniform offset.
* The stem-centre box is **inset by half a stem** at every weight, so heavy weights don't eat sidebearings and every weight fills the same cell. `m` gets a 75% middle stem.
* **Italics** shear the skeleton 10° around mid-x-height while the pen stays upright, so stem widths stay constant.
* The default zero is **dotted** (the “null dot”). `zero` gives slashed and `ss01` plain. `0 O o`, `1 l I |`, and `5 S` are distinct in every weight (see the confusables sheet).

## Variable font
Built from all 9 masters per slope. Pen width/height interpolate linearly, so every intermediate weight is a valid stroke font.

## Engine
polyline skeleton on an 8×14 grid → upright rectangular pen (Minkowski hexagons) → pathops union
