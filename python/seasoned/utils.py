import polars as pol

rows_at_a_time=1000
curindx=0

while True:
    df = pol.read_sql(f"SELECT * from TABLENAME limit {curindx},{rows_at_a_time}", connection_string) 
    if df.shape[0]==0:
        break
    df.write_parquet(f"output{curindx}.parquet")
    curindx+=rows_at_a_time
ldf=pol.concat([pol.scan_parquet(x) for x in os.listdir(".") if "output" in x and "parquet" in x])

