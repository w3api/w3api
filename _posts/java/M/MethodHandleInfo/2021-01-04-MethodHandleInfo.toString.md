---
title: MethodHandleInfo.toString()
permalink: Java/MethodHandleInfo/toString
date: 2021-01-04
key: JavaJava.M.MethodHandleInfo
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandleInfo.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static String toString(int kind, Class<?> defc, String name, MethodType type)
~~~

## Parámetros
* **Class&lt;?&gt; defc**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> defc" %}
* **MethodType type**,  {% include w3api/param_description.html metodo=_data parametro="MethodType type" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **int kind**,  {% include w3api/param_description.html metodo=_data parametro="int kind" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandleInfo](/Java/MethodHandleInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandleInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
