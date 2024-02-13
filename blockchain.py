from classes.block import Block
from classes.stack import Stack
from classes.file import File

#instances
stack = Stack()
genesis_block = Block.genesis_block('genesis', 'the first block')
second_block = Block.create_block('second', genesis_block, 'its a little test :)')

#stack process
stack.empiler(genesis_block)
stack.empiler(second_block)

print((stack.exposed_stack())[0].hash)


