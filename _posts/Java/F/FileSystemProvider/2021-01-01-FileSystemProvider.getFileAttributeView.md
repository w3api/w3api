---
title: FileSystemProvider.getFileAttributeView()
permalink: /Java/FileSystemProvider/getFileAttributeView/
date: 2021-01-11
key: Java.F.FileSystemProvider
category: Java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="getFileAttributeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <V extends FileAttributeView>V getFileAttributeView(Path path, Class<V> type, LinkOption... options)
~~~

## Parámetros
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="LinkOption... options" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}
* **Class&lt;V&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> type" %}

## Clase Padre
[FileSystemProvider](/Java/FileSystemProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
