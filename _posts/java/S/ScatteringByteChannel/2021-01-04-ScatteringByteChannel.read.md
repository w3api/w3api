---
title: ScatteringByteChannel.read()
permalink: Java/ScatteringByteChannel/read
date: 2021-01-04
key: JavaJava.S.ScatteringByteChannel
category: java
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] dsts" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[NonReadableChannelException](/Java/NonReadableChannelException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[ScatteringByteChannel](/Java/ScatteringByteChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScatteringByteChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
