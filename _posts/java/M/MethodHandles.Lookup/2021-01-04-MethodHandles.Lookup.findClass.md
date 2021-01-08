---
title: MethodHandles.Lookup.findClass()
permalink: Java/MethodHandles/Lookup/findClass
date: 2021-01-04
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="findClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Class<?> findClass(String targetName) throws ClassNotFoundException, IllegalAccessException
~~~

## Parámetros
* **String targetName**,  {% include w3api/param_description.html metodo=_data parametro="String targetName" %}

## Excepciones
[IllegalAccessException](/Java/IllegalAccessException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [SecurityException](/Java/SecurityException/)

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
