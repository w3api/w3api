---
title: FileChannel.transferFrom()
permalink: Java/FileChannel/transferFrom
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="transferFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract long transferFrom(ReadableByteChannel src, long position, long count) throws IOException
~~~

## Parámetros
* **long count**,  {% include w3api/param_description.html metodo=_data parametro="long count" %}
* **ReadableByteChannel src**,  {% include w3api/param_description.html metodo=_data parametro="ReadableByteChannel src" %}
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}

## Excepciones
[NonWritableChannelException](/Java/NonWritableChannelException/), [NonReadableChannelException](/Java/NonReadableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
