---
title: Constructor.getAnnotation()
permalink: /Java/Constructor/getAnnotation/
date: 2021-01-11
key: Java.C.Constructor
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Constructor.metodos valor="getAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Annotation>T getAnnotation(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> annotationClass" %}

## Clase Padre
[Constructor](/Java/Constructor/)

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
