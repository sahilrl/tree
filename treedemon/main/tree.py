"""
Modified Preorder Tree Traversal
"""

from main.models import TreeModel


class Tree:
    def __init__(self, item):
        self.item = item
        self.lft = 1
        self.rgt = 2


class BuildingTree:
    def __init__(self, item):
        if not isinstance(item, Tree):
            self.root = Tree(item)

    def add_item(self, item, node=None):
        if node:
            pass

        if not isinstance(item, Tree):
            self.item = Tree(item)
        self.item.lft = self.root.rgt
        self.item.rgt = self.item.lft + 1
        self.root.rgt = self.item.rgt + 1
        return self.item

    
    def save_item(self):
        treemodel = TreeModel.objects.update_or_create(item=self.root.item, lft=self.root.lft, defaults={'rgt': self.root.rgt})
        print(treemodel)
        if self.item:
            treemodel = TreeModel(item=self.item.item, lft=self.item.lft, rgt=self.item.rgt)
            print(treemodel)
            treemodel.save()

