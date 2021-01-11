---
title: AccessibleObject.getAnnotationsByType()
permalink: Java/AccessibleObject/getAnnotationsByType
date: 2021-01-10
key: JavaJava.A.AccessibleObject
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessibleObject.metodos valor="getAnnotationsByType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Annotation>T[] getAnnotationsByType(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> annotationClass" %}

## Clase Padre
[AccessibleObject](/Java/AccessibleObject/)

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
