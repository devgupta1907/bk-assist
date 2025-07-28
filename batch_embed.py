import os
from new_embedder import embed_json_to_chroma

DATA_FOLDER = "data"

def run_batch_embedding(data_folder):
    # List all JSON files
    json_files = [f for f in os.listdir(data_folder) if f.endswith(".json")]
    
    if not json_files:
        print("❌ No JSON files found in data/ folder.")
        return

    for file_name in json_files:
        file_path = os.path.join(data_folder, file_name)
        try:
            print(f"🔄 Embedding: {file_path}")
            embed_json_to_chroma(file_path)
            print(f"✅ Done: {file_name}\n")
        except Exception as e:
            print(f"❌ Failed to embed {file_name}: {e}\n")

if __name__ == "__main__":
    run_batch_embedding(DATA_FOLDER)
