# imports
import requests, csv, json, subprocess, time


# function to grab the list out of the garbled mess that is the program output. Seriously who adds this many print lines?
# todo ideally ask Dr.Woodford to restructure the project so I don't have to get output from a printline
def extract_list(s: str) -> list:
    start = s.index("[")
    end = s.index("]")
    list_str = s[start:end+1]
    return list(eval(list_str))


# create the resource for uploads
class Application():

    def post(self, args):
        results = ''

        # Convert the 'equil' JSON data back to a list of rows
        equil_rows = json.loads(args['equil'])

        # Convert the 'potential' JSON data back to a list of rows
        potential_rows = json.loads(args['potential'])

        # todo I'm constrained by the PyFGH library. It would be ideal to skip this entirely and feed the data in programmatically
        # Open the first CSV file in write mode
        with open('equil.csv', 'w', newline='') as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            # Write the rows to the CSV file
            for row in equil_rows:
                writer.writerow(row)

        # Open the second CSV file in write mode
        with open('potential.csv', 'w', newline='') as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            # Write the rows to the CSV file
            for row in potential_rows:
                writer.writerow(row)

        # Check to see if OpenPBS is set to be used or not
        if True:
            # Run using OpenPBS
            # todo remove debug print after testing!
            print('running with OpenPBS')

            # Create the PBS script file. Note, all of this can be customized as you prefer
            # todo I need to test this more and openpbs won't work well on my device
            with open('pyfgh_pbs.pbs', 'w') as f:
                f.write(f"""#!/bin/bash
            #
            # Set the name of the job
            #PBS -N pyfgh_job
            #
            # Set the walltime for the job. HH:MM:SS
            #PBS -l walltime=00:30:00
            #
            # Set the number of processors needed for the job
            #PBS -l nodes=1:ppn=1
            #
            # Set the output file name
            #PBS -o pyfgh_job.out
            #
            # Set the error file name
            #PBS -e pyfgh_job.err
            #
            # Use the current working directory
            #PBS -d .
            #
            # Set the email address for job notifications
            #PBS -M user@example.com
            #
            # Send email when the job aborts or terminates
            #PBS -m ae

            # Run the PyFGH script
            python pyfgh_script.py {args['n_list']} {args['l_list']} {args['d_var']} {args['eigenvalue_method']} {args['set_calculation']} {args['num_of_eigenvalues']}""")

            # Submit the PBS script to the scheduler
            qsub_output = subprocess.run(["qsub", "pyfgh_pbs.pbs"], capture_output=True)
            # Extract the job ID from the qsub output
            job_id = qsub_output.stdout.decode().strip()
            print(f"Submitted job with ID {job_id}")

            # Wait for the job to finish
            while True:
                # Check the job status
                qstat_output = subprocess.run(["qstat", "-f", job_id], capture_output=True)
                # If the job is no longer in the queue, it has finished
                if "Job Id: " not in qstat_output.stdout.decode():
                    break
                # Sleep for a short time before checking again
                time.sleep(1)

                # Read the output file produced by the PyFGH script
                with open('pyfgh_job.out', 'r') as f:
                    pyfgh_output = f.read()
                # Extract the list of eigenvalues from the PyFGH output
                results = extract_list(str(pyfgh_output)[150:])

                # Return the results to the client
                return {"id": job_id, "status": True, "data": results}
        else:
            # Using subprocess we call pyfgh script, so it can complete the operation using batching
            output = subprocess.run(["python3", "pyfgh_script.py", args['n_list'], args['l_list'], args['d_var'], args['eigenvalue_method'], args['set_calculation'], args['num_of_eigenvalues']], capture_output=True)
            # Glean the output we want
            results = extract_list(str(output)[150:])
        # todo before we return, save the output to a results csv file that can be called using get. Optional feature though only for if I have time
        return {"id": 'todo make this return a id for later get', "status": True, "data": results}
