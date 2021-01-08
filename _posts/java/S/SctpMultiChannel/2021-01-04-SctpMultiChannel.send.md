---
title: SctpMultiChannel.send()
permalink: Java/SctpMultiChannel/send
date: 2021-01-04
key: JavaJava.S.SctpMultiChannel
category: java
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
* **ByteBuffer buffer**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer buffer" %}
* **MessageInfo messageInfo**,  {% include w3api/param_description.html metodo=_data parametro="MessageInfo messageInfo" %}

## Excepciones
[InvalidStreamException](/Java/InvalidStreamException/), [SecurityException](/Java/SecurityException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[SctpMultiChannel](/Java/SctpMultiChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SctpMultiChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
