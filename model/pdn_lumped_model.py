"""
Lumped RLC model of the PDN, used to cross-check the Ansys SIwave results.

The board is reduced to one node at the BGA (U1), fed from the regulator
(J3) through the plane path, with the local decoupling capacitors attached
at the BGA. Values were calibrated against the SIwave Z11 curves.

Run:  python pdn_lumped_model.py
Needs: numpy, matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(4, 9, 4000)          # 10 kHz to 1 GHz, same as the SIwave sweep
w = 2 * np.pi * f
Z_TARGET = 15e-3                     # 30 mV ripple / 2 A transient


def pdn_impedance(l_mount_1u, l_path=3.0e-9):
    """|Z| seen by U1.

    l_mount_1u : mounting inductance of each 1 uF capacitor (H)
    l_path     : plane inductance between J3 and U1 (H)
    """
    r_path = 2.5e-3                  # plane resistance J3 -> U1 (matches DC IR result)
    c_plane = 430e-12                # PWR-GND plane capacitance
    l_vrm = 0.47e-9                  # regulator modelled as 0.47 nH across J3

    # Regulator in parallel with 2 x 100 uF bulk capacitors at J3
    z_vrm = 1j * w * l_vrm
    z_bulk = 2.5e-3 + 1j * w * 1e-9 + 1 / (1j * w * 200e-6)
    z_src = z_vrm * z_bulk / (z_vrm + z_bulk)

    y = 1 / (r_path + 1j * w * l_path + z_src) + 1j * w * c_plane
    # 4 x 10 uF, ESR 15 mOhm, ESL 0.5 nH, mounting 1.0 nH
    y += 4 / (15e-3 + 1j * w * (0.5e-9 + 1.0e-9) + 1 / (1j * w * 10e-6))
    # 4 x 1 uF, ESR 10 mOhm, ESL 0.5 nH, mounting set by placement
    y += 4 / (10e-3 + 1j * w * (0.5e-9 + l_mount_1u) + 1 / (1j * w * 1e-6))
    return np.abs(1 / y)


def crossing(z):
    """First frequency above 5 MHz where |Z| exceeds the target."""
    m = (f > 5e6) & (z > Z_TARGET)
    return f[m][0]


cases = {
    "1 uF caps beside the BGA (mounting 1.0 nH)": pdn_impedance(1.0e-9),
    "1 uF caps under the BGA (mounting ~0.45 nH)": pdn_impedance(0.45e-9),
}

plt.figure(figsize=(8, 5))
for name, z in cases.items():
    i100 = np.argmin(abs(f - 1e8))
    print(f"{name}: 15 mOhm crossing {crossing(z) / 1e6:.1f} MHz, "
          f"|Z| at 100 MHz {z[i100] * 1e3:.0f} mOhm")
    plt.loglog(f, z * 1e3, label=name)
plt.axhline(Z_TARGET * 1e3, color="k", ls="--", lw=1, label="Target 15 mOhm")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Z| (mOhm)")
plt.title("Lumped PDN model")
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("pdn_lumped_model.png", dpi=150)
print("Saved pdn_lumped_model.png")
