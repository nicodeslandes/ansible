# usage: source ./hacking/env-setup.ps1 [-q]
#    modifies environment for running Ansible from checkout

$HACKING_DIR = [IO.Path]::GetDirectoryName($MyInvocation.MyCommand.Path)
$ANSIBLE_HOME =  [IO.Path]::GetDirectoryName($HACKING_DIR)


$PREFIX_PYTHONPATH="$ANSIBLE_HOME/lib"
$PREFIX_PATH="$ANSIBLE_HOME/bin"
$PREFIX_MANPATH="$ANSIBLE_HOME/docs/man"

if ($env:PYTHONPATH -notcontains $PREFIX_PYTHONPATH) {
	$env:PYTHONPATH = "$PREFIX_PYTHONPATH;$env:PYTHONPATH"
}

if ($env:PATH -notcontains $PREFIX_PATH) {
	$env:PATH = "$PREFIX_PATH;$env:PATH"
}

$env:ANSIBLE_LIBRARY="$ANSIBLE_HOME/library;$(python $HACKING_DIR/get_library.py)"
#[[ $MANPATH != ${PREFIX_MANPATH}* ]] && export MANPATH=$PREFIX_MANPATH:$MANPATH


# Print out values unless -q is set

#if [ $# -eq 0 -o "$1" != "-q" ] ; then
    echo ""
    echo "Setting up Ansible to run out of checkout..."
    echo ""
    echo "PATH=$env:PATH"
    echo "PYTHONPATH=$env:PYTHONPATH"
    echo "ANSIBLE_LIBRARY=$env:ANSIBLE_LIBRARY"
    echo "MANPATH=$env:MANPATH"
    echo ""
    
    echo "Remember, you may wish to specify your host file with -i"
    echo ""
    echo "Done!"
    echo ""

