---
title: FileSystemProvider.isSameFile()
permalink: /Java/FileSystemProvider/isSameFile/
date: 2021-01-11
key: Java.F.FileSystemProvider
category: Java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="isSameFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean isSameFile(Path path, Path path2) throws IOException
~~~

## Parámetros
* **Path path2**,  {% include w3api/param_description.html metodo=_dato parametro="Path path2" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

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
