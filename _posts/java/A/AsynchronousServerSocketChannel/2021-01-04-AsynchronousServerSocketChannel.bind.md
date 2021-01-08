---
title: AsynchronousServerSocketChannel.bind()
permalink: Java/AsynchronousServerSocketChannel/bind
date: 2021-01-04
key: JavaJava.A.AsynchronousServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousServerSocketChannel.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final AsynchronousServerSocketChannel bind(SocketAddress local) throws IOException
public abstract AsynchronousServerSocketChannel bind(SocketAddress local, int backlog) throws IOException
~~~

## Parámetros
* **SocketAddress local**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress local" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_data parametro="int backlog" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[AsynchronousServerSocketChannel](/Java/AsynchronousServerSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousServerSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
