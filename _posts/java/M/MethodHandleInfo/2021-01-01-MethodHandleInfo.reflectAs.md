---
title: MethodHandleInfo.reflectAs()
permalink: Java/MethodHandleInfo/reflectAs
date: 2021-01-11
key: JavaJava.M.MethodHandleInfo
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandleInfo.metodos valor="reflectAs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Member>T reflectAs(Class<T> expected, MethodHandles.Lookup lookup)
~~~

## Parámetros
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup lookup" %}
* **Class&lt;T&gt; expected**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> expected" %}

## Clase Padre
[MethodHandleInfo](/Java/MethodHandleInfo/)

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
