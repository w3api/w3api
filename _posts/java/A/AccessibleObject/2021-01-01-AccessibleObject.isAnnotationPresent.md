---
title: AccessibleObject.isAnnotationPresent()
permalink: Java/AccessibleObject/isAnnotationPresent
date: 2021-01-11
key: JavaJava.A.AccessibleObject
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessibleObject.metodos valor="isAnnotationPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isAnnotationPresent(Class<? extends Annotation> annotationClass)
~~~

## Parámetros
* **Class&lt;? extends Annotation&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Annotation> annotationClass" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
