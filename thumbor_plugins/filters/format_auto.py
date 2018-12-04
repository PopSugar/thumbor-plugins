#!/usr/bin/python
# -*- coding: utf-8 -*-

from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    @filter_method(BaseFilter.Boolean)
    def format_auto(self, enabled=True):
        self.context.request.auto_png_to_jpg = enabled