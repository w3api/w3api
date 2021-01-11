---
title: SctpMultiChannel.bindAddress()
permalink: Java/SctpMultiChannel/bindAddress
date: 2021-01-11
key: JavaJava.S.SctpMultiChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="bindAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpMultiChannel bindAddress(InetAddress address) throws IOException
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [NotYetBoundException](/Java/NotYetBoundException/)

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
