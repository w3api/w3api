---
title: SctpMultiChannel.send()
permalink: /Java/SctpMultiChannel/send/
date: 2021-01-11
key: Java.S.SctpMultiChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int send(ByteBuffer buffer, MessageInfo messageInfo) throws IOException
~~~

## Parámetros
* **MessageInfo messageInfo**,  {% include w3api/param_description.html metodo=_dato parametro="MessageInfo messageInfo" %}
* **ByteBuffer buffer**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer buffer" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [InvalidStreamException](/Java/InvalidStreamException/), [SecurityException](/Java/SecurityException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

## Clase Padre
[SctpMultiChannel](/Java/SctpMultiChannel/)

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
