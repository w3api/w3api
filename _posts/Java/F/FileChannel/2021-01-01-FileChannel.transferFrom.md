---
title: FileChannel.transferFrom()
permalink: /Java/FileChannel/transferFrom/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
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
* **long count**,  {% include w3api/param_description.html metodo=_dato parametro="long count" %}
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}
* **ReadableByteChannel src**,  {% include w3api/param_description.html metodo=_dato parametro="ReadableByteChannel src" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [NonReadableChannelException](/Java/NonReadableChannelException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

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
