---
title: FileChannel.read()
permalink: Java/FileChannel/read
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
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
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] dsts" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer dst" %}
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}

## Excepciones
[NonReadableChannelException](/Java/NonReadableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
