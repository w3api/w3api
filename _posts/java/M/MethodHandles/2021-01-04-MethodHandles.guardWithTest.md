---
title: MethodHandles.guardWithTest()
permalink: Java/MethodHandles/guardWithTest
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="guardWithTest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle guardWithTest(MethodHandle test, MethodHandle target, MethodHandle fallback)
~~~

## Parámetros
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle target" %}
* **MethodHandle fallback**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle fallback" %}
* **MethodHandle test**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle test" %}

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
