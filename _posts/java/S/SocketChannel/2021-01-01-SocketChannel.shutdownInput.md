---
title: SocketChannel.shutdownInput()
permalink: Java/SocketChannel/shutdownInput
date: 2021-01-11
key: JavaJava.S.SocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="shutdownInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SocketChannel shutdownInput() throws IOException
~~~

## Excepciones
[NotYetConnectedException](/Java/NotYetConnectedException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
