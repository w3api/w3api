---
title: MethodHandles.whileLoop()
permalink: Java/MethodHandles/whileLoop
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="whileLoop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle whileLoop(MethodHandle init, MethodHandle pred, MethodHandle body)
~~~

## Parámetros
* **MethodHandle pred**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle pred" %}
* **MethodHandle body**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle body" %}
* **MethodHandle init**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle init" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
