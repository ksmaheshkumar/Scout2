#!/usr/bin/env python2

class Filter(object):

    def __init__(self, description, entity, callback, callback_args):
        self.description = description
        self.entity = entity
        self.callback = callback
        self.callback_args = callback_args
        self.items = []

    def addItem(self, item, macro_item = None):
        if not macro_item:
            if item not in self.items:
                self.items.append(item)
        else:
            self.items.append(item)
            self.macro_items.append(macro_item)

    #
    # Call to that function when iterating over items or macro_items will create
    # invalid results.
    #
    def removeItem(self, item, macro_item = None):
        try:
            target = self.items.index(item)
            del self.items[target]
            if macro_item:
                del self.macro_items[target]
        except Exception, e:
            print e
            pass
