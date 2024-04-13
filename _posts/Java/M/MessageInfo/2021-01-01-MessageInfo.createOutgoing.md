---
title: MessageInfo.createOutgoing()
permalink: /Java/MessageInfo/createOutgoing/
date: 2021-01-11
key: Java.M.MessageInfo
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageInfo.metodos valor="createOutgoing" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MessageInfo createOutgoing(Association association, SocketAddress address, int streamNumber)
public static MessageInfo createOutgoing(SocketAddress address, int streamNumber)
~~~

## Parámetros
* **SocketAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress address" %}
* **Association association**,  {% include w3api/param_description.html metodo=_dato parametro="Association association" %}
* **int streamNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int streamNumber" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MessageInfo](/Java/MessageInfo/)

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
