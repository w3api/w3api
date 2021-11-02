---
title: importlib
permalink: /Python/importlib
date: 2021-01-01
key: Python.I.importlib
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.I.importlib.description }}

## Funciones
* [all_suffixes](/Python/importlib/all_suffixes/)
* [as_file](/Python/importlib/as_file/)
* [cache_from_source](/Python/importlib/cache_from_source/)
* [contents](/Python/importlib/contents/)
* [decode_source](/Python/importlib/decode_source/)
* [files](/Python/importlib/files/)
* [find_loader](/Python/importlib/find_loader/)
* [find_spec](/Python/importlib/find_spec/)
* [import_module](/Python/importlib/import_module/)
* [invalidate_caches](/Python/importlib/invalidate_caches/)
* [is_resource](/Python/importlib/is_resource/)
* [module_for_loader](/Python/importlib/module_for_loader/)
* [module_from_spec](/Python/importlib/module_from_spec/)
* [open_binary](/Python/importlib/open_binary/)
* [open_text](/Python/importlib/open_text/)
* [path](/Python/importlib/path/)
* [read_binary](/Python/importlib/read_binary/)
* [read_text](/Python/importlib/read_text/)
* [reload](/Python/importlib/reload/)
* [resolve_name](/Python/importlib/resolve_name/)
* [set_loader](/Python/importlib/set_loader/)
* [set_package](/Python/importlib/set_package/)
* [source_from_cache](/Python/importlib/source_from_cache/)
* [source_hash](/Python/importlib/source_hash/)
* [spec_from_file_location](/Python/importlib/spec_from_file_location/)
* [spec_from_loader](/Python/importlib/spec_from_loader/)
* [__import__](/Python/importlib/__import__/)

## Clases
* [BuiltinImporter](/Python/importlib/BuiltinImporter/)
* [ExecutionLoader](/Python/importlib/ExecutionLoader/)
* [ExtensionFileLoader](/Python/importlib/ExtensionFileLoader/)
* [FileFinder](/Python/importlib/FileFinder/)
* [FileLoader](/Python/importlib/FileLoader/)
* [Finder](/Python/importlib/Finder/)
* [FrozenImporter](/Python/importlib/FrozenImporter/)
* [importlib.machinery](/Python/importlib/importlib.machinery/)
* [importlib.util](/Python/importlib/importlib.util/)
* [InspectLoader](/Python/importlib/InspectLoader/)
* [LazyLoader](/Python/importlib/LazyLoader/)
* [Loader](/Python/importlib/Loader/)
* [MetaPathFinder](/Python/importlib/MetaPathFinder/)
* [ModuleSpec](/Python/importlib/ModuleSpec/)
* [PathEntryFinder](/Python/importlib/PathEntryFinder/)
* [PathFinder](/Python/importlib/PathFinder/)
* [ResourceLoader](/Python/importlib/ResourceLoader/)
* [ResourceReader](/Python/importlib/ResourceReader/)
* [SourceFileLoader](/Python/importlib/SourceFileLoader/)
* [SourcelessFileLoader](/Python/importlib/SourcelessFileLoader/)
* [SourceLoader](/Python/importlib/SourceLoader/)
* [Traversable](/Python/importlib/Traversable/)
* [TraversableResources](/Python/importlib/TraversableResources/)
* [WindowsRegistryFinder](/Python/importlib/WindowsRegistryFinder/)

## Constantes
* [Package](/Python/importlib/Package/)
* [Resource](/Python/importlib/Resource/)

## Ejemplo
~~~python
{{ site.data.Python.I.importlib.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.I.importlib.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
