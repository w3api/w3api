---
title: SctpMultiChannel.receive()
permalink: Java/SctpMultiChannel/receive
date: 2021-01-04
key: JavaJava.S.SctpMultiChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="receive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> MessageInfo receive(ByteBuffer buffer, T attachment, NotificationHandler<T> handler)
~~~

## Parámetros
* **ByteBuffer buffer**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer buffer" %}
* **T attachment**,  {% include w3api/param_description.html metodo=_data parametro="T attachment" %}
* **NotificationHandler&lt;T&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="NotificationHandler<T> handler" %}

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
