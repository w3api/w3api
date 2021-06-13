---
title: SctpChannel.connect()
permalink: /Java/SctpChannel/connect/
date: 2021-01-11
key: Java.S.SctpChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean connect(SocketAddress remote) throws IOException
public abstract boolean connect(SocketAddress remote, int maxOutStreams, int maxInStreams) throws IOException
~~~

## Parámetros
* **int maxInStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxInStreams" %}
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress remote" %}
* **int maxOutStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxOutStreams" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [UnresolvedAddressException](/Java/UnresolvedAddressException/), [IOException](/Java/IOException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ConnectionPendingException](/Java/ConnectionPendingException/), [SecurityException](/Java/SecurityException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [AlreadyConnectedException](/Java/AlreadyConnectedException/)

## Clase Padre
[SctpChannel](/Java/SctpChannel/)

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
