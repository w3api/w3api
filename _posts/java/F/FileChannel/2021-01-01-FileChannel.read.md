---
title: FileChannel.read()
permalink: /Java/FileChannel/read/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int read(ByteBuffer dst) throws IOException
public final long read(ByteBuffer[] dsts) throws IOException
public abstract long read(ByteBuffer[] dsts, int offset, int length) throws IOException
public abstract int read(ByteBuffer dst, long position) throws IOException
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] dsts" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [NonReadableChannelException](/Java/NonReadableChannelException/)

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
