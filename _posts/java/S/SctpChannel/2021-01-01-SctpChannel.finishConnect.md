---
title: SctpChannel.finishConnect()
permalink: Java/SctpChannel/finishConnect
date: 2021-01-11
key: JavaJava.S.SctpChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="finishConnect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean finishConnect() throws IOException
~~~

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NoConnectionPendingException](/Java/NoConnectionPendingException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

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
