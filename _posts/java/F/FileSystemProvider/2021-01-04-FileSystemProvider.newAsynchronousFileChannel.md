---
title: FileSystemProvider.newAsynchronousFileChannel()
permalink: Java/FileSystemProvider/newAsynchronousFileChannel
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newAsynchronousFileChannel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AsynchronousFileChannel newAsynchronousFileChannel(Path path, Set<? extends OpenOption> options, ExecutorService executor, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends OpenOption> options" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_data parametro="FileAttribute<?>... attrs" %}
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_data parametro="ExecutorService executor" %}
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}

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
