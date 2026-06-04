import subprocess 

def run_system_command(command_args):

    try:

        result = subprocess.run(
            command_args,
            capture_output = True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:

        error_msg = e.stderr.strip() if e.stderrcelse else str(e)
        raise RuntimeError(f"Linux kernel erro: {error_msg}")