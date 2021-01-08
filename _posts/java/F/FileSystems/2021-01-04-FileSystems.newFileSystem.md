---
title: FileSystems.newFileSystem()
permalink: Java/FileSystems/newFileSystem
date: 2021-01-04
key: JavaJava.F.FileSystems
category: java
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
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_data parametro="?> env" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileSystemAlreadyExistsException](/Java/FileSystemAlreadyExistsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ProviderNotFoundException](/Java/ProviderNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[FileSystems](/Java/FileSystems/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystems.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
