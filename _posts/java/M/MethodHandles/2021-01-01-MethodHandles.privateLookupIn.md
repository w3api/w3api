---
title: MethodHandles.privateLookupIn()
permalink: /Java/MethodHandles/privateLookupIn/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="privateLookupIn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandles.Lookup privateLookupIn(Class<?> targetClass, MethodHandles.Lookup lookup) throws IllegalAccessException
~~~

## Parámetros
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup lookup" %}
* **Class&lt;?&gt; targetClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> targetClass" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalAccessException](/Java/IllegalAccessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

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
