---
title: ServerSocketChannel.getLocalAddress()
permalink: Java/ServerSocketChannel/getLocalAddress
date: 2021-01-11
key: JavaJava.S.ServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocketChannel.metodos valor="getLocalAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SocketAddress getLocalAddress() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
