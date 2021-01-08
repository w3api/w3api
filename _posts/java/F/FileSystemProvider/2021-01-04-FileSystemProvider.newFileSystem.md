---
title: FileSystemProvider.newFileSystem()
permalink: Java/FileSystemProvider/newFileSystem
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newFileSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract FileSystem newFileSystem(URI uri, Map<String,?> env) throws IOException
public FileSystem newFileSystem(Path path, Map<String,?> env) throws IOException
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_data parametro="?> env" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileSystemAlreadyExistsException](/Java/FileSystemAlreadyExistsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[FileSystemProvider](/Java/FileSystemProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystemProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
