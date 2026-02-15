import json
from pathlib import Path

def divide_into_batches():
    """Divide all_metadata.json into batches of 20 records each"""
    
    input_file = Path(__file__).parent / "all_metadata.json"
    batch_dir = Path(__file__).parent / "batches"
    batch_dir.mkdir(exist_ok=True)
    
    print("Loading JSON file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_records = len(data)
    batch_size = 20
    total_batches = (total_records + batch_size - 1) // batch_size
    
    print(f"Total records: {total_records}")
    print(f"Batch size: {batch_size}")
    print(f"Total batches: {total_batches}")
    print(f"\nCreating batches in: {batch_dir}")
    print("-" * 60)
    
    for i in range(total_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, total_records)
        batch_data = data[start_idx:end_idx]
        
        batch_file = batch_dir / f"batch_{i+1:03d}.json"
        
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        
        print(f"Created {batch_file.name} - Records {start_idx+1} to {end_idx}")
    
    print("-" * 60)
    print(f"\n✓ Successfully created {total_batches} batch files!")
    print(f"✓ Each batch contains up to {batch_size} records")
    print(f"\nNext step: Review batch_001.json and decide what to keep/remove")

if __name__ == "__main__":
    divide_into_batches()
