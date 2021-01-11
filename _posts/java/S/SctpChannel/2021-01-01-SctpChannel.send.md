---
title: SctpChannel.send()
permalink: Java/SctpChannel/send
date: 2021-01-11
key: JavaJava.S.SctpChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int send(ByteBuffer src, MessageInfo messageInfo) throws IOException
~~~

## Parámetros
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **MessageInfo messageInfo**,  {% include w3api/param_description.html metodo=_dato parametro="MessageInfo messageInfo" %}

## Excepciones
[NotYetConnectedException](/Java/NotYetConnectedException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [InvalidStreamException](/Java/InvalidStreamException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

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
