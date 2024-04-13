---
title: AnnotatedElement.getAnnotation()
permalink: /Java/AnnotatedElement/getAnnotation/
date: 2021-01-11
key: Java.A.AnnotatedElement
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotatedElement.metodos valor="getAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Annotation>T getAnnotation(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> annotationClass" %}

## Clase Padre
[AnnotatedElement](/Java/AnnotatedElement/)

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
