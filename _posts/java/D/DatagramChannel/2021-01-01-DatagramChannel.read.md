---
title: DatagramChannel.read()
permalink: /Java/DatagramChannel/read/
date: 2021-01-11
key: Java.D.DatagramChannel
category: Java
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
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] dsts" %}
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
