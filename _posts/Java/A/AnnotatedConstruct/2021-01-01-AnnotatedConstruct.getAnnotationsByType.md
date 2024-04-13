---
title: AnnotatedConstruct.getAnnotationsByType()
permalink: /Java/AnnotatedConstruct/getAnnotationsByType/
date: 2021-01-11
key: Java.A.AnnotatedConstruct
category: Java
tags: ['java se', 'javax.lang.model', 'java.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotatedConstruct.metodos valor="getAnnotationsByType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A extends Annotation>A[] getAnnotationsByType(Class<A> annotationType)
~~~

## Parámetros
* **Class&lt;A&gt; annotationType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<A> annotationType" %}

## Clase Padre
[AnnotatedConstruct](/Java/AnnotatedConstruct/)

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
