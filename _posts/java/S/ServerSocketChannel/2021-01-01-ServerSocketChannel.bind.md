---
title: ServerSocketChannel.bind()
permalink: Java/ServerSocketChannel/bind
date: 2021-01-11
key: JavaJava.S.ServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocketChannel.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final ServerSocketChannel bind(SocketAddress local) throws IOException
public abstract ServerSocketChannel bind(SocketAddress local, int backlog) throws IOException
~~~

## Parámetros
* **SocketAddress local**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress local" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ServerSocketChannel](/Java/ServerSocketChannel/)

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
