from __future__ import annotations

import os
from typing import TYPE_CHECKING

from ... import Command, controllersConfig
from ...batoceraPaths import ROMS
from ...utils.logger import get_logger
from ..Generator import Generator

if TYPE_CHECKING:
    from ...types import HotkeysContext

eslog = get_logger(__name__)

class HurricanGenerator(Generator):

    def generate(self, system, rom, playersControllers, metadata, guns, wheels, gameResolution):
        try:
            os.chdir(ROMS / "hurrican" / "data" / "levels/")
            os.chdir(ROMS / "hurrican")
        except:
            eslog.error("ERROR: Game assets not installed. You can get them from the Batocera Content Downloader.")
        commandArray = ["hurrican"]

        return Command.Command(
            array=commandArray,
            env={
                'SDL_GAMECONTROLLERCONFIG': controllersConfig.generateSdlGameControllerConfig(playersControllers)
            })

    def getHotkeysContext(self) -> HotkeysContext:
        return {
            "name": "hurrican",
            "keys": { "exit": ["KEY_LEFTALT", "KEY_F4"] }
        }
