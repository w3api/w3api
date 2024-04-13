---
title: AnnotationElement.getAnnotation()
permalink: /Java/AnnotationElement/getAnnotation/
date: 2021-01-11
key: Java.A.AnnotationElement
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationElement.metodos valor="getAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A> A getAnnotation(Class<? extends Annotation> annotationType)
~~~

## Parámetros
* **Class&lt;? extends Annotation&gt; annotationType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Annotation> annotationType" %}

## Clase Padre
[AnnotationElement](/Java/AnnotationElement/)

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
