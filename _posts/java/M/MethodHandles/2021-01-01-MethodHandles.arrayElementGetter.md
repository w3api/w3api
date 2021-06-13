---
title: MethodHandles.arrayElementGetter()
permalink: /Java/MethodHandles/arrayElementGetter/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="arrayElementGetter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle arrayElementGetter(Class<?> arrayClass) throws IllegalArgumentException
~~~

## Parámetros
* **Class&lt;?&gt; arrayClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> arrayClass" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
