# Inkscape Purge Short Lines

This Inkscape extension lets you delete lines shorter than a given threshold.

The extension was made to clean up heavy PDFs exported from SketchUp, but can
probably be used in various other situations too.

## Install for usage

Copy the content in src/ into your Inkscape extension directory. The extension
directory path can be found in _Edit > Preferences > System_ inside of Inkscape.

## Installation for development

1. Fork and clone the repo to your computer (to other location than Inkscape
extension directory).
2. Set up symlinks in the Inkscape extension directory pointing to the extension
files.

Developing directly in the Inkscape extension directory is not recommended. When
doing so different extensions projects can't be in different repositories, as
Inkscape loads all extensions from the same directory. Instead develop in a
separate directory and use symlinks pointing to the repository files from the
extension directory. On Windows the [Link Shell Extension](http://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html) can be used.
