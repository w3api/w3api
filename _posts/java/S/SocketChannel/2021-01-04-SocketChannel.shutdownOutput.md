---
title: SocketChannel.shutdownOutput()
permalink: Java/SocketChannel/shutdownOutput
date: 2021-01-04
key: JavaJava.S.SocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="shutdownOutput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SocketChannel shutdownOutput() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [NotYetConnectedException](/Java/NotYetConnectedException/), [IOException](/Java/IOException/)

## Clase Padre
[SocketChannel](/Java/SocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
