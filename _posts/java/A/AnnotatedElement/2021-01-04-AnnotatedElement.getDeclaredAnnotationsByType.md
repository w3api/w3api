---
title: AnnotatedElement.getDeclaredAnnotationsByType()
permalink: Java/AnnotatedElement/getDeclaredAnnotationsByType
date: 2021-01-04
key: JavaJava.A.AnnotatedElement
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotatedElement.metodos valor="getDeclaredAnnotationsByType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default <T extends Annotation>T[] getDeclaredAnnotationsByType(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> annotationClass" %}

## Clase Padre
[AnnotatedElement](/Java/AnnotatedElement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AnnotatedElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
