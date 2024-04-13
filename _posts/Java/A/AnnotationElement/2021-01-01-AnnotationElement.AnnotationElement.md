---
title: AnnotationElement.AnnotationElement()
permalink: /Java/AnnotationElement/AnnotationElement/
date: 2021-01-11
key: Java.A.AnnotationElement
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationElement.constructores valor="AnnotationElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AnnotationElement(Class<? extends Annotation> annotationType)
public AnnotationElement(Class<? extends Annotation> annotationType, Object value)
public AnnotationElement(Class<? extends Annotation> annotationType, Map<String,Object> values)
~~~

## Parámetros
* **Class&lt;? extends Annotation&gt; annotationType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Annotation> annotationType" %}
* **Object&gt; values**,  {% include w3api/param_description.html metodo=_dato parametro="Object> values" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
