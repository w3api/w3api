---
title: SctpChannel.open()
permalink: Java/SctpChannel/open
date: 2021-01-04
key: JavaJava.S.SctpChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SctpChannel open() throws IOException
public static SctpChannel open(SocketAddress remote, int maxOutStreams, int maxInStreams) throws IOException
~~~

## Parámetros
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress remote" %}
* **int maxInStreams**,  {% include w3api/param_description.html metodo=_data parametro="int maxInStreams" %}
* **int maxOutStreams**,  {% include w3api/param_description.html metodo=_data parametro="int maxOutStreams" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [UnresolvedAddressException](/Java/UnresolvedAddressException/), [IOException](/Java/IOException/)

## Clase Padre
[SctpChannel](/Java/SctpChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SctpChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
