---
title: RoundEnvironment.getElementsAnnotatedWith()
permalink: Java/RoundEnvironment/getElementsAnnotatedWith
date: 2021-01-11
key: Java.R.RoundEnvironment
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoundEnvironment.metodos valor="getElementsAnnotatedWith" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Set<? extends Element> getElementsAnnotatedWith(Class<? extends Annotation> a)
Set<? extends Element> getElementsAnnotatedWith(TypeElement a)
~~~

## Parámetros
* **TypeElement a**,  {% include w3api/param_description.html metodo=_dato parametro="TypeElement a" %}
* **Class&lt;? extends Annotation&gt; a**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Annotation> a" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RoundEnvironment](/Java/RoundEnvironment/)

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
