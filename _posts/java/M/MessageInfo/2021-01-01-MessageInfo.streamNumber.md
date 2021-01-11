---
title: MessageInfo.streamNumber()
permalink: Java/MessageInfo/streamNumber
date: 2021-01-11
key: JavaJava.M.MessageInfo
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageInfo.metodos valor="streamNumber" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int streamNumber()
public abstract MessageInfo streamNumber(int streamNumber)
~~~

## Parámetros
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
