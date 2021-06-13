---
title: DatagramChannel.write()
permalink: /Java/DatagramChannel/write/
date: 2021-01-11
key: Java.D.DatagramChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int write(ByteBuffer src) throws IOException
public final long write(ByteBuffer[] srcs) throws IOException
public abstract long write(ByteBuffer[] srcs, int offset, int length) throws IOException
~~~

## Parámetros
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] srcs" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[NotYetConnectedException](/Java/NotYetConnectedException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

## Clase Padre
[DatagramChannel](/Java/DatagramChannel/)

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
