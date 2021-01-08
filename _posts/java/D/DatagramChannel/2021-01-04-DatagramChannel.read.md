---
title: DatagramChannel.read()
permalink: Java/DatagramChannel/read
date: 2021-01-04
key: JavaJava.D.DatagramChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int read(ByteBuffer dst) throws IOException
public final long read(ByteBuffer[] dsts) throws IOException
public abstract long read(ByteBuffer[] dsts, int offset, int length) throws IOException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer dst" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] dsts" %}
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
