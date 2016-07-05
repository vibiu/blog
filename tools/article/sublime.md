# Python Coding in Sublime
## Package Control
> Ctrl + `

```
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
see [packagecontrol](https://packagecontrol.io/installation#st3)

## Preference User
```json
{
    "auto_complete": true,
    "color_scheme": "Packages/Color Scheme - Default/Solarized (Dark).tmTheme",
    "ensure_newline_at_eof_on_save": true,
    "file_exclude_patterns":
    [
        ".DS_Store",
        "*.pid",
        "*.pyc"
    ],
    "folder_exclude_patterns":
    [
        ".git",
        "__pycache__"
    ],
    "font_size": 12,
    "highlight_line": true,
    "ignored_packages":
    [
        "Vintabe"
    ],
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true
}
```
see [Develop Python Using Sublime Text](http://sw897.github.io/2014/02/13/sublime-text-3-for-python/)

## Packages
see [Build Python IDLE using Sublime Text](http://python.jobbole.com/81312/)

see [Ncuhome Backend-guide](https://github.com/ncuhome/backend-guide)
### Anaconda
[Anaconda Guide](https://rhinstaller.github.io/anaconda/)

```json
{
    "anaconda_linting": false,
}
```

### GitGutter
[jisaacks/GitGutter](https://github.com/jisaacks/GitGutter)

### Python PEP8 Autoformat
[Python PEP8 Autoformat](https://bitbucket.org/StephaneBunel/pythonpep8autoformat)

### Flake8Lint
[Flake8Lint](https://github.com/dreadatour/Flake8Lint)

### Markdown Preview
[Markdown Preview](https://github.com/revolunet/sublimetext-markdown-preview)

preference > user-key-binding

```json
{ "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"} }
```

### Terminal
[Terminal](https://packagecontrol.io/packages/Terminal)

default key-binding:

```
Ctrl+Alt+Shift+t(open terminal here)
Ctrl+Alt+t(open system terminal)
```

### AdvancedNewFile
[AdvancedNewFile](https://github.com/skuroda/Sublime-AdvancedNewFile)

I don't use it now.

### Sidebar enhancements
[Sidebar enhancements](https://github.com/titoBouzout/SideBarEnhancements/tree/st3)
