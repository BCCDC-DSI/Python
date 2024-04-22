
<details>
<summary>Connection - R</summary>  

```
library("dplyr")
library("tidyr")
library("purrr")
library("lubridate")
library("stringr")
library("ggplot2")
library("openxlsx")
library("RODBC")
library("RODBCext")
library("rmarkdown")
library("knitr")
library("kableExtra")

connect_to_phrdw_database <- function(database_server, database_name)
{
  odbc_connection_string = sprintf("driver={SQL Server};server=%s;database=%s;trusted_connection=true",database_server, database_name)
  
  phrdw_db_connection <- odbcDriverConnect(odbc_connection_string)
  
  rm(odbc_connection_string)
  
  return(phrdw_db_connection)
  
  
}

close_connection_to_phrdw_database <- function(database_connection)
{
  close(database_connection) 
  rm(database_connection)  
}
```


</details>
