from fabric.api import env, run, local
from fabric.context_managers import cd


## remember to setup your host in  ~/.ssh/config
## with format
## Host myHost
##   User app-user
##   HostName app-host-name
##   IdentityFile app-ssh-key


env.hosts = ['quizbootSandbox']
env.use_ssh_config = True

root='britecore-assessment-implementation'
docker_compose='sudo docker-compose -f dev.yml'

def goto_dir_add_execute(command, command_param=None ,location=""):
    with cd(f'{root}{location}'):
        if command_param:
            command(command_param)
        else:
            command()

def git_pull():
    run('git pull')

def docker_build():
    run(f'{docker_compose} build')    

def docker_up():
    goto_dir_add_execute(run, f'{docker_compose} up -d')

def docker_down():
    goto_dir_add_execute(run, f'{docker_compose} down')

def docker_logs():
    goto_dir_add_execute(run, f'{docker_compose} logs --follow')

def pull_and_build_image():
    git_pull()
    docker_build()

def update_app():
    goto_dir_add_execute(pull_and_build_image)

def uptime():
    run("uptime")