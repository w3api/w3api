---
title: DatagramChannel.write()
permalink: Java/DatagramChannel/write
date: 2021-01-04
key: JavaJava.D.DatagramChannel
category: java
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] srcs" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [NotYetConnectedException](/Java/NotYetConnectedException/), [IOException](/Java/IOException/)

## Clase Padre
[DatagramChannel](/Java/DatagramChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
