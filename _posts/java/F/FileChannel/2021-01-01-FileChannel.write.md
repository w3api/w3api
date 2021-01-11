---
title: FileChannel.write()
permalink: Java/FileChannel/write
date: 2021-01-11
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int write(ByteBuffer src) throws IOException
public final long write(ByteBuffer[] srcs) throws IOException
public abstract long write(ByteBuffer[] srcs, int offset, int length) throws IOException
public abstract int write(ByteBuffer src, long position) throws IOException
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] srcs" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

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
