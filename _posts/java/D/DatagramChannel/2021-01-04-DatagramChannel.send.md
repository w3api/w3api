---
title: DatagramChannel.send()
permalink: Java/DatagramChannel/send
date: 2021-01-04
key: JavaJava.D.DatagramChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int send(ByteBuffer src, SocketAddress target) throws IOException
~~~

## Parámetros
* **SocketAddress target**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress target" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer src" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
