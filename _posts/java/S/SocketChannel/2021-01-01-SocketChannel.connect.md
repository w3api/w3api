---
title: SocketChannel.connect()
permalink: /Java/SocketChannel/connect/
date: 2021-01-11
key: Java.S.SocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean connect(SocketAddress remote) throws IOException
~~~

## Parámetros
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress remote" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [UnresolvedAddressException](/Java/UnresolvedAddressException/), [IOException](/Java/IOException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ConnectionPendingException](/Java/ConnectionPendingException/), [SecurityException](/Java/SecurityException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [AlreadyConnectedException](/Java/AlreadyConnectedException/)

## Clase Padre
[SocketChannel](/Java/SocketChannel/)

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
