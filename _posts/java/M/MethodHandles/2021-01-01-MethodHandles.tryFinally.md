---
title: MethodHandles.tryFinally()
permalink: Java/MethodHandles/tryFinally
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="tryFinally" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle tryFinally(MethodHandle target, MethodHandle cleanup)
~~~

## Parámetros
* **MethodHandle cleanup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle cleanup" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [catchException(MethodHandle, Class, MethodHandle)](/Java/catchException(MethodHandle, Class, MethodHandle)/), [NullPointerException](/Java/NullPointerException/)

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
