---
title: ScatteringByteChannel.read()
permalink: /Java/ScatteringByteChannel/read/
date: 2021-01-11
key: Java.S.ScatteringByteChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScatteringByteChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long read(ByteBuffer[] dsts) throws IOException
long read(ByteBuffer[] dsts, int offset, int length) throws IOException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] dsts" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [NonReadableChannelException](/Java/NonReadableChannelException/)

## Clase Padre
[ScatteringByteChannel](/Java/ScatteringByteChannel/)

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
