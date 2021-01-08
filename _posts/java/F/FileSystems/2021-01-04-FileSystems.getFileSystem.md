---
title: FileSystems.getFileSystem()
permalink: Java/FileSystems/getFileSystem
date: 2021-01-04
key: JavaJava.F.FileSystems
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystems.metodos valor="getFileSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static FileSystem getFileSystem(URI uri)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}

## Excepciones
[FileSystemNotFoundException](/Java/FileSystemNotFoundException/), [SecurityException](/Java/SecurityException/), [ProviderNotFoundException](/Java/ProviderNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
