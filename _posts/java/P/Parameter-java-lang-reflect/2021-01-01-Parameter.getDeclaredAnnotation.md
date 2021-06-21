---
title: Parameter.getDeclaredAnnotation()
permalink: /Java/Parameter-java-lang-reflect/getDeclaredAnnotation/
date: 2021-01-11
key: Java.P.Parameter-java-lang-reflect
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Parameter-java-lang-reflect.metodos valor="getDeclaredAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends Annotation>T getDeclaredAnnotation(Class<T> annotationClass)
~~~

## Parámetros
* **Class&lt;T&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> annotationClass" %}

## Clase Padre
[Parameter](/Java/Parameter-java-lang-reflect/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
