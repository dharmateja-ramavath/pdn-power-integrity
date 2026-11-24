# Ansys SIwave projects (2025 R1)

- `Diff_pair_PI.siw`: original placement (DC IR drop and the impedance runs)
- `PCB_under_BGA.siw`: 1 uF capacitors under the BGA

Result folders (`*.siwaveresults`) are excluded by `.gitignore`, because they are large and can be regenerated. The plots are in `../images`.

Model settings used in both projects:

| Item | Value |
|---|---|
| 10 uF capacitors (C3 to C6) | 10 uF, ESL 0.5 nH, ESR 15 mOhm |
| 1 uF capacitors (C7 to C10) | 1 uF, ESL 0.5 nH, ESR 10 mOhm |
| Bulk capacitors (C1, C2) | 100 uF, ESL 0.5 nH, ESR 5 mOhm |
| Regulator, AC runs | 0.47 nH inductor across J3 |
| Regulator, DC run | 1.0 V source at J3 |
| Port | U1 VDD pin group to U1 GND pin group |
| SYZ sweep | 10 kHz to 1 GHz |
