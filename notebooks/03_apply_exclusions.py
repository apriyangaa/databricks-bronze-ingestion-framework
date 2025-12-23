# Columns that should not be propagated to Bronze
EXCLUDED_COLUMNS = [
    "debug_flag",
    "internal_notes"
]

# Drop columns only if they exist (defensive coding)
final_df = df_std.drop(
    *[col for col in EXCLUDED_COLUMNS if col in df_std.columns]
)

final_df.display()
