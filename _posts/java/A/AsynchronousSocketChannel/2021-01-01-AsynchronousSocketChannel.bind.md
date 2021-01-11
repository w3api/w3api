---
title: AsynchronousSocketChannel.bind()
permalink: Java/AsynchronousSocketChannel/bind
date: 2021-01-11
key: JavaJava.A.AsynchronousSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AsynchronousSocketChannel bind(SocketAddress local) throws IOException
~~~

## Parámetros
* **SocketAddress local**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress local" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ConnectionPendingException](/Java/ConnectionPendingException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[AsynchronousSocketChannel](/Java/AsynchronousSocketChannel/)

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
