
from pathlib import Path
import pandas as pd

# Laster inn og definerer filsti der filen skal ligge
data = Path(
    "/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201/psa_clinical_data.csv"
)
print(data)

# Lager en rotmappe for alle undermappene
rot_mappe = data.parent / "Studies"
rot_mappe.mkdir(parents=True, exist_ok=True) # scriptet feiler ikke hvsi mappen allerede finnes

# Leser inn CSV filen
df = pd.read_csv(data, sep=",", header=0)

# Gjør om datoer til datetime for beregninger
df["surgery_date_dt"] = pd.to_datetime(df["surgery_date"])
df["psa_date_dt"] = pd.to_datetime(df["psa_date"])

# Grupperer dataene per studie
for study_id, study_df in df.groupby("study_id"):

    # Lager undermappe for studiene
    study_folder = rot_mappe / str(study_id)
    study_folder.mkdir(parents=True, exist_ok=True) # scriptet feiler ikke hvis mappene allerede finnes

    # Liste for å samle rader til <study_id>_summary.csv
    summary_rows = []

    # Lager undermappe per pasient i studiene
    for patient_id, patient_df in study_df.groupby("patient_id"):

        # Lager unik ID for hver pasient
        patient_str = str(patient_id).zfill(4)  # fyller inn nuller før nummer
        unique_id = f"{study_id}_P{patient_str}"

        # Lager undermapper
        patient_folder = study_folder / unique_id
        patient_folder.mkdir(parents=True, exist_ok=True)

        # Sorterer etter psa_date kronologisk
        patient_df_sorted = patient_df.sort_values("psa_date_dt").copy()

        # Siste registrerte psa_date for denne pasienten
        siste_psa_dato = patient_df_sorted["psa_date_dt"].max()
        surgery_dato = patient_df_sorted["surgery_date_dt"].iloc[0]

        # Differanse i dager mellom operasjon og seneste PSA-måling
        follow_up_days = (siste_psa_dato - surgery_dato).days

        # Antall blodprøver registrert
        number_of_psa_measurements = len(patient_df_sorted)

        # Fjern datetime-hjelpekolonnene (behold opprinnelig psa_date og surgery_date)
        export_df = patient_df_sorted.drop(
            columns=["surgery_date_dt", "psa_date_dt", "study_id", "patient_id"]
        )

        # Lagre pasientens individuelle oppføringer
        patient_file_path = patient_folder / f"{unique_id}_records.csv"
        export_df.to_csv(patient_file_path, index=False) # skriver over evt gamle csv filer

        # Beregn verdier for summary filen
        dob = patient_df["date_of_birth"].iloc[0]
        surgery_date_str = patient_df["surgery_date"].iloc[0]

        # Relativ sti til pasientmappen
        relative_patient_path = patient_folder.relative_to(study_folder)

        # Legg til i summary liste
        summary_rows.append(
            {
                "unique_id": unique_id,
                "date_of_birth": dob,
                "surgery_date": surgery_date_str,
                "follow_up_days": follow_up_days,
                "number_of_psa_measurements": number_of_psa_measurements,
                "patient_folder_path": str(relative_patient_path),
            }
        )

    # Opprett og lagre summary-fil per studie
    summary_df = pd.DataFrame(summary_rows)
    summary_df = summary_df.sort_values("unique_id")

    summary_file_path = study_folder / f"{study_id}_summary.csv"
    summary_df.to_csv(summary_file_path, index=False)

    print(
        f"Fullført for studie {study_id}: {len(summary_rows)} pasienter prosessert."
    )