---
title: Executable.getAnnotationsByType()
permalink: Java/Executable/getAnnotationsByType
date: 2021-01-04
key: JavaJava.E.Executable
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executable.metodos valor="getAnnotationsByType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Annotation>T[] getAnnotationsByType(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> annotationClass" %}

## Clase Padre
[Executable](/Java/Executable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Executable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
