---
title: FileSystemProvider.getFileSystem()
permalink: Java/FileSystemProvider/getFileSystem
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="getFileSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract FileSystem getFileSystem(URI uri)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [FileSystemNotFoundException](/Java/FileSystemNotFoundException/)

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
