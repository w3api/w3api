---
title: MethodHandles.Lookup.accessClass()
permalink: Java/MethodHandles/Lookup/accessClass
date: 2021-01-04
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="accessClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Class<?> accessClass(Class<?> targetClass) throws IllegalAccessException
~~~

## Parámetros
* **Class&lt;?&gt; targetClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> targetClass" %}

## Excepciones
[IllegalAccessException](/Java/IllegalAccessException/), [SecurityException](/Java/SecurityException/)

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
