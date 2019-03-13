import sqlite3
DB_FILE = 'payroll_dc_small.db'
conn = sqlite3.connect(DB_FILE)

def main():
    print('a6 - standard report 2')
    strsql = """select 
                    supervist, 
                    max(salary), 
                    avg(salary), 
                    min(salary), 
                    max(los), 
                    avg(los) los_avg, 
                    count(supervist)
                from factdata_mar2016, super
                where factdata_mar2016.supervis = super.supervis
                group by supervist
                order by los_avg asc
                limit 20;
            
        """
    cursor = conn.execute(strsql)
    # the formating string for each row of the report
    report_string_format = '{0:<40}\t{1:<10}{2:<10}{3:<10}'
    # printing the header of the report. 
    print(
        report_string_format.format(
            'supervist', 'sal_max', 'avg_sal', 'sal_min', 'max_los', 'los_avg' 'count_supervist'
            )
        )

    for row in cursor:  
        supervist, sal_max, avg_sal, sal_min, max_los, los_avg, count_supervist = row
        print(
            report_string_format.format(
                supervist, sal_max, avg_sal, sal_min, max_los, los_avg, count_supervist
                )
            )

    cursor.close()      # close cursor
    conn.close()       # close connection to the db

if __name__ == "__main__":
    main()
