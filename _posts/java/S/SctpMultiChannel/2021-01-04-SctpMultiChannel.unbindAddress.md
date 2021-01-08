---
title: SctpMultiChannel.unbindAddress()
permalink: Java/SctpMultiChannel/unbindAddress
date: 2021-01-04
key: JavaJava.S.SctpMultiChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="unbindAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpMultiChannel unbindAddress(InetAddress address) throws IOException
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress address" %}

## Excepciones
[NotYetBoundException](/Java/NotYetBoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalUnbindException](/Java/IllegalUnbindException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
