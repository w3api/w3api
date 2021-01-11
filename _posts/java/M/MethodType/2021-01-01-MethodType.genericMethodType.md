---
title: MethodType.genericMethodType()
permalink: Java/MethodType/genericMethodType
date: 2021-01-11
key: JavaJava.M.MethodType
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="genericMethodType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodType genericMethodType(int objectArgCount)
public static MethodType genericMethodType(int objectArgCount, boolean finalArray)
~~~

## Parámetros
* **int objectArgCount**,  {% include w3api/param_description.html metodo=_dato parametro="int objectArgCount" %}
* **boolean finalArray**,  {% include w3api/param_description.html metodo=_dato parametro="boolean finalArray" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodType](/Java/MethodType/)

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
