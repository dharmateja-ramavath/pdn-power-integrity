# Altium Designer project

Two copies of the same project. Only the PCB differs between them.

```
altium/
├── original_placement/        1 uF capacitors C7 to C10 on the top side, beside U1
│   ├── Diff_Pair.PrjPcb
│   ├── Diff_Pair.SchDoc
│   ├── Diff_Pair.PcbDoc
│   └── Diff_Pair_ODB++.zip    ODB++ export imported into SIwave
└── under_bga/                 C7 to C10 moved to the bottom side, under U1
    ├── Diff_Pair.PrjPcb
    ├── Diff_Pair.SchDoc
    ├── Diff_Pair.PcbDoc
    └── Diff_Pair_ODB++.zip
```

Open either `Diff_Pair.PrjPcb` in Altium Designer. The footprints, including the custom 81-ball BGA, are stored inside the PCB file. The source libraries (`Launch` and `PI_LOAD`) are not included, so Altium may warn that they are missing; the design still opens.

Generated folders (`History/`, `__Previews/`, `Project Logs for ...`, `Project Outputs for ...`) are excluded by `.gitignore`.
