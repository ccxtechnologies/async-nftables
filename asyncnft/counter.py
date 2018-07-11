# Copyright: 2018, CCX Technologies

from .nft import nft


class Counter:

    initialized = False

    def __init__(
            self,
            name,
            table,
    ):
        """Counter objects are attached to tables and are identified by an
        unique name. They group counter information from rules."""

        self.name = name
        self.table = table.name
        self.family = table.family

    async def load(self):
        """Load the set, must be called before calling any other methods."""

        if self.initialized:
            return

        await nft('add', 'counter', self.family, self.table, self.name)

        self.initialized = True

    async def delete(self):
        """Delete the counter, any subsequent calls to this chain will fail."""
        if not self.initialized:
            raise RuntimeError(f"Counter {self.name} hasn't been loaded.")

        await nft('delete', 'counter', self.family, self.table, self.name)

        self.initialized = False

    async def get(self):
        """Get the value of the counter."""
        return await nft('list', 'counter', self.family, self.table, self.name)

    async def reset(self):
        """Reset the counter."""
        return await nft(
                'reset', 'counter', self.family, self.table, self.name
        )

    def __str__(self):
        if not self.initialized:
            raise RuntimeError(f"Counter {self.name} hasn't been loaded.")

        return f"counter {self.name}"