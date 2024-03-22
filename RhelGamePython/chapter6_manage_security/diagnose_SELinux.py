import CommandGenerator



troubleshoot_server = CommandGenerator.CommandGenerator(
action = 'install setroubleshoot-server',
correct_command = 'dnf install setroubleshoot-server',
hint = 'Hint: Use "dnf install setroubleshoot-server" to install setroubleshoot-server',
command_output = 
[
"""
$ sudo dnf install setroubleshoot-server
Last metadata expiration check: <timestamp>
Dependencies resolved.
================================================================================
 Package                 Arch       Version                Repository     Size
================================================================================
Installing:
 setroubleshoot-server   x86_64     <version>              <repository>  <size>

Transaction Summary
================================================================================
Install  1 Package

Total download size: <size>
Installed size: <size>
Is this ok [y/N]: y
Downloading Packages:
setroubleshoot-server-<version>.x86_64.rpm   <===========================> 100%
[------------------------------------->] eta
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                       1/1
  Installing       : setroubleshoot-server-<version>.x86_64                 1/1
  Running scriptlet: setroubleshoot-server-<version>.x86_64                 1/1
  Verifying        : setroubleshoot-server-<version>.x86_64                 1/1
Installed products updated.

Installed:
  setroubleshoot-server-<version>.x86_64

Complete!
""",
],
command_aspects = 
[
"""
 dnf: This is the package management tool used in Red Hat-based Linux distributions, such as Fedora and CentOS. It stands for "Dandified Yum", and it's a modernized version of the yum package manager.
 install: This is the subcommand of dnf used to install packages. It instructs dnf to download and install the specified package(s) and any dependencies required.
 setroubleshoot-server: This is the name of the package to be installed. In this case, it's the setroubleshoot-server package, which provides tools and utilities for troubleshooting SELinux-related issues on the server.
""",
],
command_options = 
[
"""
- Package Name: This is the name of the package(s) you want to install. You can specify one or more package names separated by spaces.
- -y, --assumeyes: Automatically answer yes to all prompts. This option is useful for automating installations without needing to manually confirm each package installation.
- -q, --quiet: Suppress output except for errors and warnings. This option is useful for reducing the amount of output when installing packages.
- --refresh: Refresh package metadata before installing packages. This option ensures that dnf retrieves the latest package information from the repositories before attempting to install packages.
- --enablerepo=REPO: Enable a specific repository for installation. This option allows you to specify a repository by name or ID from which to install packages.
- --disablerepo=REPO: Disable a specific repository for installation. This option allows you to specify a repository by name or ID that should not be used for installing packages.
- --best: Install the best available version of packages. This option instructs dnf to choose the best version of a package based on the repository configuration and dependencies.
- --allowerasing: Allow dnf to erase packages if necessary to resolve conflicts. This option is useful when installing packages that conflict with existing packages.
- --setopt=OPTION: Set a configuration option for the installation process. This option allows you to specify various configuration options for dnf during package installation.
""",
],
intro_text = ['',],
outro_text = ['',],
)

