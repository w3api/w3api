---
title: MethodHandles.tryFinally()
permalink: Java/MethodHandles/tryFinally
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
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
* **MethodHandle cleanup**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle cleanup" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle target" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [catchException(MethodHandle, Class, MethodHandle)](/Java/catchException(MethodHandle, Class, MethodHandle)/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
