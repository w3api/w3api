---
title: FileChannel.transferTo()
permalink: Java/FileChannel/transferTo
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="transferTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract long transferTo(long position, long count, WritableByteChannel target) throws IOException
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}
* **long count**,  {% include w3api/param_description.html metodo=_data parametro="long count" %}
* **WritableByteChannel target**,  {% include w3api/param_description.html metodo=_data parametro="WritableByteChannel target" %}

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
