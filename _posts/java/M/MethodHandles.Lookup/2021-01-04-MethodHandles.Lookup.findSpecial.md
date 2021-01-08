---
title: MethodHandles.Lookup.findSpecial()
permalink: Java/MethodHandles/Lookup/findSpecial
date: 2021-01-04
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="findSpecial" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle findSpecial(Class<?> refc, String name, MethodType type, Class<?> specialCaller) throws NoSuchMethodException, IllegalAccessException
~~~

## Parámetros
* **MethodType type**,  {% include w3api/param_description.html metodo=_data parametro="MethodType type" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Class&lt;?&gt; refc**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> refc" %}
* **Class&lt;?&gt; specialCaller**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> specialCaller" %}

## Excepciones
[IllegalAccessException](/Java/IllegalAccessException/), [NoSuchMethodException](/Java/NoSuchMethodException/), [SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.Lookup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
