---
title: MethodHandles.arrayElementGetter()
permalink: Java/MethodHandles/arrayElementGetter
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
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
* **Class&lt;?&gt; arrayClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> arrayClass" %}

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
