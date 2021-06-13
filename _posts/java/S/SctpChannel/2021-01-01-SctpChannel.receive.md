---
title: SctpChannel.receive()
permalink: /Java/SctpChannel/receive/
date: 2021-01-11
key: Java.S.SctpChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="receive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> MessageInfo receive(ByteBuffer dst, T attachment, NotificationHandler<T> handler)
~~~

## Parámetros
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **T attachment**,  {% include w3api/param_description.html metodo=_dato parametro="T attachment" %}
* **NotificationHandler&lt;T&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationHandler<T> handler" %}

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
