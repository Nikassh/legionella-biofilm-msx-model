class EPANETMSXWriter:
    """
    EPANET-MSX File Exporter for Biofilm and Pathogen Reactive Transport.
    """
    @staticmethod
    def generate_msx_content(k_inact: float = 0.5, k_detach: float = 0.1) -> str:
        msx_str = f"""[TITLE]
Legionella-Pseudomonas Multi-Species Biofilm Reactive Transport Model

[SPECIES]
BULK Xfree 0.01 mg/L
WALL Xwall 0.05 mg/m2

[PARAMETERS]
k_inact {k_inact}
k_detach {k_detach}

[REACTIONS]
BULK Xfree - k_inact * Cl * Xfree
WALL Xwall - k_detach * Xwall

[END]
"""
        return msx_str
