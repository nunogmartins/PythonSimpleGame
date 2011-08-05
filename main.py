from GameEngine import GameEngine

import sys

if __name__ == '__main__':
	engine = GameEngine()
	engine.load()
	engine.update()
	engine.save()
