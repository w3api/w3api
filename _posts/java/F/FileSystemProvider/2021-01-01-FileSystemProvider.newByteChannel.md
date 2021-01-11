---
title: FileSystemProvider.newByteChannel()
permalink: Java/FileSystemProvider/newByteChannel
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newByteChannel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SeekableByteChannel newByteChannel(Path path, Set<? extends OpenOption> options, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends OpenOption> options" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_dato parametro="FileAttribute<?>... attrs" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
