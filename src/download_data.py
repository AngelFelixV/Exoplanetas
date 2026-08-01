import requests
import pathlib

URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    "select+pl_name,hostname,discoverymethod,disc_year,disc_facility,"
    "pl_orbper,pl_orbsmax,pl_rade,pl_bmasse,pl_orbeccen,pl_eqt,"
    "st_teff,st_rad,st_mass,sy_dist+from+pscomppars&format=csv"
)


def download():
    out_path = pathlib.Path("data/raw/exoplanets_raw.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(URL, timeout=60)
    resp.raise_for_status()
    out_path.write_bytes(resp.content)
    print(f"Guardado en {out_path}")


if __name__ == "__main__":
    download()