import json
import os


def merge_from_parent_dir(output_filename="networks.json"):
    master_list = []

    # Get the directory one level above the script's location
    script_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(script_dir, ".."))

    exclusion_keyword = "generated"

    print(f"Script Directory: {script_dir}")
    print(f"Scanning Parent Directory: {parent_dir}")
    print(f"Excluding files containing: '{exclusion_keyword}'")
    print("-" * 60)

    # Walk through the parent directory
    for root, dirs, files in os.walk(parent_dir):
        # Optional: Prevent the script from scanning the script's own folder
        # if you want to keep 'source' and 'output' strictly separate.
        if os.path.abspath(root) == script_dir:
            continue

        for filename in files:
            if filename.endswith(".json") and exclusion_keyword not in filename:
                file_path = os.path.join(root, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                        if isinstance(data, list) and len(data) > 0:
                            sample = data[0]
                            required_keys = {"department", "as_id", "ip_range"}

                            if required_keys.issubset(sample.keys()):
                                # Use relative path from the parent_dir for the source tag
                                rel_path = os.path.relpath(file_path, parent_dir)
                                for record in data:
                                    record["source_origin"] = rel_path

                                master_list.extend(data)
                                print(f"✅ Merged: {rel_path}")

                except (json.JSONDecodeError, Exception) as e:
                    print(f"❌ Error processing {filename}: {e}")

    # Save the master file in the script's CURRENT directory
    output_path = os.path.join(script_dir, output_filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_list, f, indent=2)

    print("-" * 60)
    print(f"Success! Master file created at: {output_path}")
    print(f"Total aggregate records: {len(master_list)}")


if __name__ == "__main__":
    merge_from_parent_dir()