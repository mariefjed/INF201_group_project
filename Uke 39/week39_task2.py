from pathlib import Path
import pandas as pd


def func_sequencing_manifest(sequencing_folder, project_folder):
    summary = []

    for file in Path(sequencing_folder).glob("*"): # her blri file en sequencing file som kan gås igjennom en av gangen
        if not file.is_file():
            continue

        study_id = None
        patient_id = None

        with open(file, "r") as f:
            for line in f:
                if not line.startswith("##"): # Stopper iterering når linja ikke starter med ##
                    break

                if line.startswith("##study_id"): # Finn study ID
                    study_id = line.split("=")[1].strip()
                    

                if line.startswith("##patient_id"): # Finn pasient ID
                    patient_id = line.split("=")[1].strip()
                    

        patient_str = str(patient_id).zfill(4)  # fyller inn nuller før nummer
        unique_id = f"{study_id}_P{patient_str}"

        relative_file_path = file.relative_to(project_folder)

        summary.append(
            {"unique_id": unique_id,
            "study_id": study_id,
            "patient_id": patient_id,
            "sequencing_file_path": str(relative_file_path),
            }

            )

    sequencing_manifest = pd.DataFrame(summary)

    sequencing_manifest_file_path = project_folder / "sequencing_manifest.csv"
    sequencing_manifest.to_csv(sequencing_manifest_file_path, index=False)

    return print(sequencing_manifest)


# Tester funksjonen:
project_folder = Path("/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201")
sequencing_folder = project_folder / "Studies"

func_sequencing_manifest(sequencing_folder, project_folder)

# Koden lager en csv med denne infoen: 
# unique_id,study_id,patient_id,sequencing_file_path
# A12_P0132,A12,132,Studies/folder
# som er helt riktig


  