#!/usr/bin/env python3

import subprocess
import os
from colorama import Fore, Style

# Initialize colorama
Fore.YELLOW = Style.BRIGHT + Fore.YELLOW
Fore.CYAN = Style.BRIGHT + Fore.BLUE
Fore.RESET = Style.RESET_ALL + Fore.RESET


# Function to display the banner
def display_banner():
    banner = f"""
    {Fore.CYAN}

 ██████╗ ███╗   ██╗███████╗██████╗ ██╗███████╗ ██████╗███████╗
██╔═══██╗████╗  ██║██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔════╝
██║   ██║██╔██╗ ██║█████╗  ██████╔╝██║█████╗  ██║     █████╗  
██║   ██║██║╚██╗██║██╔══╝  ██╔═══╝ ██║██╔══╝  ██║     ██╔══╝  
╚██████╔╝██║ ╚████║███████╗██║     ██║███████╗╚██████╗███████╗
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝╚══════╝
 
  
+ I know now what is the onepiece
+ Version 1.0
+ created by waeljr0x0                                                   
{Fore.RESET}                                                              
{Fore.YELLOW}
{Fore.RESET}
"""
    print(banner)

# ... rest of the script ...

# Display the banner
display_banner()

# Dictionary of repository URLs and their corresponding installation scripts (if available)
tool_categories = {
    'subdomain_enumeration ': {
        'https://github.com/OWASP/Amass.git': 'Amass_install.sh',
        'https://github.com/tomnomnom/assetfinder.git': 'assetfinder_install.sh',
        'https://github.com/projectdiscovery/subfinder.git': 'subfinder_install.sh',
        'https://github.com/nahamsec/crtndstry.git': 'crtndstry_install.sh',
        'https://github.com/Findomain/Findomain.git': 'Findomain_install.sh',
        'https://github.com/projectdiscovery/shuffledns.git': 'shuffledns_install.sh',
        'https://github.com/fleetcaptain/Turbolist3r.git': 'Turbolist3r_install.sh',
        'https://github.com/skynet0x01/tugarecon.git': 'tugarecon_install.sh',
        'https://github.com/nexxai/Substr3am.git': 'Substr3am_install.sh',
        'https://github.com/si9int/Subra.git': 'Subra_install.sh',
        'https://github.com/blechschmidt/massdns.git': 'massdns_install.sh',
        'https://github.com/Screetsec/Sudomy.git': 'Sudomy_install.sh',
        'https://github.com/cinerieus/as3nt.git': 'as3nt_install.sh',
        'https://github.com/hakluke/hakrevdns.git': 'hakrevdns_install.sh',
        'https://github.com/infosec-au/altdns.git': 'altdns_install.sh',
        'https://github.com/projectdiscovery/dnsx.git': 'dnsx_install.sh',
        'https://github.com/edoardottt/scilla.git': 'scilla_install.sh',
        'https://github.com/christophetd/censys-subdomain-finder.git': 'acensys-subdomainfinder_install.sh',
        'https://github.com/TypeError/domained.git': 'domained_install.sh',
        'https://github.com/3nock/OTE.git': 'OTE_install.sh',

        # Add more subdomain_enumeration tool repository URLs and installation script names here
    },
    'Port_Scanning ': {
        'https://github.com/nmap/nmap.git': 'nmap_install.sh',
        'https://github.com/robertdavidgraham/masscan.git': 'masscan_install.sh',
        'https://github.com/RustScan/RustScan.git': 'RustScan_install.sh',
        'https://github.com/projectdiscovery/naabu.git': 'naabu_install.sh',
        'https://github.com/trimstray/sandmap.git': 'sandmap_install.sh',
        'https://github.com/johnnyxmas/ScanCannon.git': 'ScanCannon_install.sh',



        # Add more POrt_scanning tool repository URLs and installation script names here
    },
    
       'screenShoots ': {
        'https://github.com/RedSiege/EyeWitness.git': 'EyeWitness_install.sh',
        'https://github.com/michenriksen/aquatone.git': 'aquatone_install.sh',
        'https://github.com/vladocar/screenshoteer.git': 'screenshoteer_install.sh',
        'https://github.com/sensepost/gowitness.git': 'gowitness_install.sh',
        'https://github.com/byt3bl33d3r/WitnessMe.git': 'WitnessMe_install.sh',
        'https://github.com/BishopFox/eyeballer.git': 'eyeballer_install.sh',
        'https://github.com/nccgroup/scrying.git': 'scrying_install.sh',
        'https://github.com/spipm/Depix.git': 'Depix_install.sh',
        'https://github.com/breenmachine/httpscreenshot.git': 'httpscreenshot_install.sh',


        # Add more screenshots tool repository URLs and installation script names here
    },
    
    
      'Fuzzing ': {
        'https://github.com/xmendez/wfuzz.git': 'wfuzz_install.sh',
        'https://github.com/ffuf/ffuf.git': 'ffuf_install.sh',
        'https://github.com/fuzzdb-project/fuzzdb.git': 'fuzzdb_install.sh',
        'https://github.com/1N3/IntruderPayloads.git': 'IntruderPayloads_install.sh',
        'https://github.com/Bo0oM/fuzz.txt.git': 'fuzz.txt_install.sh',
        'https://github.com/googleprojectzero/fuzzilli.git': 'fuzzilli_install.sh',
        'https://github.com/Fuzzapi/fuzzapi.git': 'fuzzapi_install.sh',
        'https://github.com/ameenmaali/qsfuzz.git': 'qsfuzz_install.sh',
        'https://github.com/d4rckh/vaf.git': 'vaf_install.sh',
        'https://github.com/hithmast/script_collect.git': 'script_collect_install.sh',


        # Add more fuzzing tool repository URLs and installation script names here
    },

     'Content_Discovery ': {
        'https://github.com/OJ/gobuster.git': 'gobuster_install.sh',
        'https://github.com/C-Sto/recursebuster.git': 'recursebuster_install.sh',
        'https://github.com/epi052/feroxbuster.git': 'feroxbuster_install.sh',
        'https://github.com/digination/dirbuster-ng.git': 'dirbuster-ng_install.sh',
        'https://github.com/jaeles-project/gospider.git': 'gospider_install.sh',
        'https://github.com/s0rg/crawley.git': 'crawley_install.sh',
        'https://github.com/hakluke/hakrawler.git': 'hakrawler_install.sh',
        'https://github.com/stefanoj3/dirstalk.git': 'dirstalk_install.sh',
        'https://github.com/henshin/filebuster.git': 'filebuster_install.sh',
        'https://github.com/maurosoria/dirsearch.git': 'dirsearch_install.sh',
        'https://github.com/projectdiscovery/katana.git': 'katana_install.sh',



        # Add more Content_Discovery tool repository URLs and installation script names here
    },
    
  'Technologies ': {
        'https://github.com/praetorian-inc/fingerprintx.git': 'fingerprintx_install.sh',
        'https://github.com/projectdiscovery/httpx.git': 'httpx_install.sh',
        'https://github.com/RetireJS/retire.js.git': 'retire_install.sh',
        'https://github.com/urbanadventurer/whatweb.git': 'whatweb_install.sh',
        'https://github.com/claymation/python-builtwith.git': 'python-builtwith_install.sh',
        'https://github.com/rverton/webanalyze.git': 'webanalyze_install.sh',
        'https://github.com/AliasIO/wappalyzer.git': 'wappalyzer_install.sh',
       


        # Add more Technologies tool repository URLs and installation script names here
    },

    
  'Links ': {
        'https://github.com/tomnomnom/waybackurls.git': 'waybackurls_install.sh',
        'https://github.com/lc/gau.git': 'gau_install.sh',
        'https://github.com/GerbenJavado/LinkFinder.git': 'LinkFinder_install.sh',
        'https://github.com/IAmStoxe/urlgrab.git': 'urlgrab_install.sh',
       


        # Add more Links tool repository URLs and installation script names here
    },
    
 'Scanners ': {
        'https://github.com/projectdiscovery/nuclei.git': 'nuclei_install.sh',
        'https://github.com/1N3/Sn1per.git': 'Sn1per_install.sh',
        'https://github.com/sullo/nikto.git': 'nikto_install.sh',
    
       


        # Add more Scanners tool repository URLs and installation script names here
    },
 'Parameters': {
        'https://github.com/maK-/parameth.git': 'parameth_install.sh',
        'https://github.com/s0md3v/Arjun.git': 'Arjun_install.sh',
        'https://github.com/Bo0oM/ParamPamPam.git': 'ParamPamPam_install.sh',
    
       


        # Add more Parameters tool repository URLs and installation script names here
    },

 'BruteForce': {
        'https://github.com/vanhauser-thc/thc-hydra.git': 'thc-hydra_install.sh',
        'https://github.com/1N3/BruteX.git': 'BruteX_install.sh',
        'https://github.com/lanjelot/patator.git': 'patator_install.sh',
    
       


        # Add more BruteForce tool repository URLs and installation script names here
    },

 'exploitation': {
        'https://github.com/sqlmapproject/sqlmap.git': 'sqlmap_install.sh',
        'https://github.com/r0oth3x49/ghauri.git': 'ghauri_install.sh',
        'https://github.com/SAPT01/HBSQLI.git': 'HBSQLI_install.sh',
    
       


        # Add more exploitation tool repository URLs and installation script names here
    },

    
    
    
    
    
    # Add more categories here
}


def is_tool_installed(tool_name):
    return subprocess.run(['which', tool_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).returncode == 0

def install_tool(repo_url, install_script):
    tool_name = repo_url.split('/')[-1].split('.')[0]
    install_dir = os.path.expanduser(f'~/Downloads/{tool_name}')

    if is_tool_installed(tool_name):
        print(f"Tool '{tool_name}' is already installed.")
        return

    if os.path.exists(install_dir):
        print(f"Tool '{tool_name}' is already present in the installation directory. Skipping installation.")
        return


     # Check if the tool is available as a package in apt-get
    apt_package_name = tool_name.lower()  # Package names are usually lowercase
    apt_return_code = subprocess.run(['sudo', 'apt-get', 'install', '-y', '--dry-run', apt_package_name],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode

    if apt_return_code == 0:
        # The tool is available as a package, install it using apt-get
        subprocess.run(['sudo', 'apt-get', 'install', '-y', apt_package_name])
        print(f"Tool '{tool_name}' installation complete (via apt-get).")
    else:
        # The tool is not available as a package, clone the repository and execute the script
        subprocess.run(['git', 'clone', repo_url, install_dir])
        install_script_path = os.path.join(install_dir, install_script)
        if os.path.isfile(install_script_path):
            subprocess.run(['sudo', 'bash', install_script_path])
            print(f"Tool '{tool_name}' installation complete (via git clone).")
        else:
            print(f"Installation script '{install_script}' not found for '{tool_name}'. Installation failed.")

    install_script_path = os.path.join(install_dir, install_script)
    if os.path.isfile(install_script_path):
        subprocess.run(['sudo', 'bash', install_script_path])


    print(f"Tool '{tool_name}' installation complete.")


# Update package lists
subprocess.run(['sudo', 'apt-get', 'update'])

# Ask user for choice
while True:
    try:
        print("Choose an option:")
        print("1. Install all tools in a specific category")
        print("2. Install a specific tool from a specific category")
        choice = input("Enter the number of the action you want to perform (or 'exit' to quit): ")

        if choice.lower() == 'exit':
            print("Exiting.")
            break

        if choice == '1':
            print("Available categories:")
            for i, category in enumerate(tool_categories.keys(), start=1):
                print(f"{i}. {category}")

            category_choice = input("Enter the number of the category you want to install tools from: ")
            if category_choice.isdigit():
                index = int(category_choice)
                if 1 <= index <= len(tool_categories):
                    selected_category = list(tool_categories.keys())[index - 1]
                    selected_tools = tool_categories[selected_category]
                    for repo_url, install_script in selected_tools.items():
                        install_tool(repo_url, install_script)
                else:
                    print("Invalid number.")
            else:
                print("Invalid input. Please enter a valid number or 'exit'.")
        elif choice == '2':
            print("Available categories:")
            for i, category in enumerate(tool_categories.keys(), start=1):
                print(f"{i}. {category}")

            category_choice = input("Enter the number of the category you want to install tools from: ")
            if category_choice.isdigit():
                index = int(category_choice)
                if 1 <= index <= len(tool_categories):
                    selected_category = list(tool_categories.keys())[index - 1]
                    selected_tools = tool_categories[selected_category]
                    print(f"Available tools in '{selected_category}':")
                    for i, repo_url in enumerate(selected_tools.keys(), start=1):
                        tool_name = repo_url.split('/')[-1].split('.')[0]
                        print(f"{i}. {tool_name}")

                    tool_indices = input("Enter the numbers of the tools you want to install (separated by spaces): ")
                    tool_indices = tool_indices.split()
                    for index in tool_indices:
                        index = int(index)
                        if 1 <= index <= len(selected_tools):
                            selected_repo, selected_install_script = list(selected_tools.items())[index - 1]
                            install_tool(selected_repo, selected_install_script)
                        else:
                            print(f"Invalid tool number: {index}")
                else:
                    print("Invalid number.")
            else:
                print("Invalid input. Please enter a valid number or 'exit'.")
        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")
    except ValueError:
        print("Invalid input. Please enter a number, tool name, or 'exit'.")
