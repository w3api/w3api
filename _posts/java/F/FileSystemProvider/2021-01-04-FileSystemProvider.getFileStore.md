---
title: FileSystemProvider.getFileStore()
permalink: Java/FileSystemProvider/getFileStore
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="getFileStore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract FileStore getFileStore(Path path) throws IOException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}

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
{%- for _ldc in site.data.Java.F.FileSystemProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
