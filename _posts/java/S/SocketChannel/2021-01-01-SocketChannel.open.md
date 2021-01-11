---
title: SocketChannel.open()
permalink: Java/SocketChannel/open
date: 2021-01-11
key: JavaJava.S.SocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SocketChannel open() throws IOException
public static SocketChannel open(SocketAddress remote) throws IOException
~~~

## Parámetros
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress remote" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [UnresolvedAddressException](/Java/UnresolvedAddressException/), [IOException](/Java/IOException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [SecurityException](/Java/SecurityException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

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
