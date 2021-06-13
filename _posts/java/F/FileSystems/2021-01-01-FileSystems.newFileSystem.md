---
title: FileSystems.newFileSystem()
permalink: /Java/FileSystems/newFileSystem/
date: 2021-01-11
key: Java.F.FileSystems
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystems.metodos valor="newFileSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static FileSystem newFileSystem(URI uri, Map<String,?> env) throws IOException
public static FileSystem newFileSystem(URI uri, Map<String,?> env, ClassLoader loader) throws IOException
public static FileSystem newFileSystem(Path path, ClassLoader loader) throws IOException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [ProviderNotFoundException](/Java/ProviderNotFoundException/), [SecurityException](/Java/SecurityException/), [FileSystemAlreadyExistsException](/Java/FileSystemAlreadyExistsException/)

## Clase Padre
[FileSystems](/Java/FileSystems/)

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
