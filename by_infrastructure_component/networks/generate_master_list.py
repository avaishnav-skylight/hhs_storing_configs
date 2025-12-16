import json
import os


def recursive_merge_protected(output_filename="master-generated.json"):
    master_list = []
    root_dir = os.getcwd()
    exclusion_keyword = "generated"

    print(f"Starting recursive scan in: {root_dir}")
    print(f"Excluding files containing: '{exclusion_keyword}'")
    print("-" * 50)

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            # 1. Only process .json files
            # 2. Ignore any file with "-generated" in the name (including our master)
            if filename.endswith(".json") and exclusion_keyword not in filename:
                file_path = os.path.join(root, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                        # Validate structure: must be a list with specific keys
                        if isinstance(data, list) and len(data) > 0:
                            sample = data[0]
                            required_keys = {"department", "as_id", "ip_range"}

                            if required_keys.issubset(sample.keys()):
                                # Tag the source for traceability
                                rel_path = os.path.relpath(file_path, root_dir)
                                for record in data:
                                    record["source_origin"] = rel_path

                                master_list.extend(data)
                                print(f"✅ Merged: {rel_path}")

                except (json.JSONDecodeError, Exception) as e:
                    print(f"❌ Error processing {filename}: {e}")

    # Save the master file with the exclusion keyword in the name
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(master_list, f, indent=2)

    print("-" * 50)
    print(f"Success! Master file created: {output_filename}")
    print(f"Total aggregate records: {len(master_list)}")


if __name__ == "__main__":
    recursive_merge_protected()