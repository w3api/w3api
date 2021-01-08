---
title: FileSystemProvider.newFileChannel()
permalink: Java/FileSystemProvider/newFileChannel
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newFileChannel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileChannel newFileChannel(Path path, Set<? extends OpenOption> options, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends OpenOption> options" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_data parametro="FileAttribute<?>... attrs" %}
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
