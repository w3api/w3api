---
title: MethodHandles.Lookup.unreflectSpecial()
permalink: Java/MethodHandles/Lookup/unreflectSpecial
date: 2021-01-11
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="unreflectSpecial" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle unreflectSpecial(Method m, Class<?> specialCaller) throws IllegalAccessException
~~~

## Parámetros
* **Method m**,  {% include w3api/param_description.html metodo=_dato parametro="Method m" %}
* **Class&lt;?&gt; specialCaller**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> specialCaller" %}

## Excepciones
[IllegalAccessException](/Java/IllegalAccessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

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
