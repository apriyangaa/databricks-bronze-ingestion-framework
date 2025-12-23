# Target Delta path
TARGET_PATH = "abfss://bronze@storage/account/hr/dim_employee"

(
    final_df.write
    .format("delta")
    .mode("overwrite")  # Idempotent write for repeatable runs
    .save(TARGET_PATH)
)

print("✅ Bronze Delta write completed")
