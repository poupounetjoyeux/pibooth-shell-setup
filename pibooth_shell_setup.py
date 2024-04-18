"""Plugin to execute shell commands among pibooth workflow"""
import os
import pibooth
from pibooth.utils import LOGGER

__version__ = "1.0.0"

def __execute_script(script):
    if script:
        LOGGER.debug(f'Executing shell script {script}')
        os.system(script)
        
def __get_script(cfg, hook_name):
    if cfg.has_section('SCRIPTS') and cfg.has_option('SCRIPTS', hook_name):
        return cfg.getpath('SCRIPTS', hook_name)
    return None

def __get_and_execute_script(cfg, hook_name):
    __execute_script(__get_script(cfg, hook_name))

@pibooth.hookimpl
def pibooth_configure(cfg):
    __get_and_execute_script(cfg, 'pibooth_configure')

@pibooth.hookimpl
def pibooth_reset(cfg, hard):
    __get_and_execute_script(cfg, 'pibooth_reset')

@pibooth.hookimpl
def pibooth_startup(cfg, app):
    app.cleanup_script = __get_script(cfg, 'pibooth_cleanup')
    __get_and_execute_script(cfg, 'pibooth_startup')

@pibooth.hookimpl
def pibooth_cleanup(app):
    __execute_script(app.cleanup_script)

@pibooth.hookimpl
def state_failsafe_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_failsafe_enter')

@pibooth.hookimpl
def state_failsafe_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_failsafe_do')

@pibooth.hookimpl
def state_failsafe_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_failsafe_exit')

@pibooth.hookimpl
def state_wait_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_wait_enter')

@pibooth.hookimpl
def state_wait_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_wait_do')

@pibooth.hookimpl
def state_wait_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_wait_exit')

@pibooth.hookimpl
def state_choose_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_choose_enter')

@pibooth.hookimpl
def state_choose_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_choose_do')

@pibooth.hookimpl
def state_choose_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_choose_exit')

@pibooth.hookimpl
def state_chosen_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_chosen_enter')

@pibooth.hookimpl
def state_chosen_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_chosen_do')

@pibooth.hookimpl
def state_chosen_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_chosen_exit')

@pibooth.hookimpl
def state_preview_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_preview_enter')

@pibooth.hookimpl
def state_preview_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_preview_do')

@pibooth.hookimpl
def state_preview_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_preview_exit')

@pibooth.hookimpl
def state_capture_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_capture_enter')

@pibooth.hookimpl
def state_capture_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_capture_do')

@pibooth.hookimpl
def state_capture_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_capture_exit')

@pibooth.hookimpl
def state_processing_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_processing_enter')

@pibooth.hookimpl
def state_processing_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_processing_do')

@pibooth.hookimpl
def state_processing_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_processing_exit')

@pibooth.hookimpl
def state_print_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_print_enter')

@pibooth.hookimpl
def state_print_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_print_do')

@pibooth.hookimpl
def state_print_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_print_exit')

@pibooth.hookimpl
def state_finish_enter(cfg, app, win):
    __get_and_execute_script(cfg, 'state_finish_enter')

@pibooth.hookimpl
def state_finish_do(cfg, app, win, events):
    __get_and_execute_script(cfg, 'state_finish_do')

@pibooth.hookimpl
def state_finish_exit(cfg, app, win):
    __get_and_execute_script(cfg, 'state_finish_exit')