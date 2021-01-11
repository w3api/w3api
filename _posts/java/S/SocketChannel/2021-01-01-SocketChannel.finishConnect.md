---
title: SocketChannel.finishConnect()
permalink: Java/SocketChannel/finishConnect
date: 2021-01-11
key: JavaJava.S.SocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="finishConnect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean finishConnect() throws IOException
~~~

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NoConnectionPendingException](/Java/NoConnectionPendingException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

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
