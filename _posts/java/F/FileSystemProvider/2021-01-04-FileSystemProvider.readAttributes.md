---
title: FileSystemProvider.readAttributes()
permalink: Java/FileSystemProvider/readAttributes
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="readAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <A extends BasicFileAttributes>A readAttributes(Path path, Class<A> type, LinkOption... options)
public abstract Map<String,Object> readAttributes(Path path, String attributes, LinkOption... options) throws IOException
~~~

## Parámetros
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_data parametro="LinkOption... options" %}
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}
* **String attributes**,  {% include w3api/param_description.html metodo=_data parametro="String attributes" %}
* **Class&lt;A&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<A> type" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
