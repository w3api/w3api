---
title: EventType.getAnnotation()
permalink: /Java/EventType-jdk-jfr/getAnnotation/
date: 2021-01-11
key: Java.E.EventType-jdk-jfr
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventType-jdk-jfr.metodos valor="getAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A extends Annotation>A getAnnotation(Class<A> annotationClass)
~~~

## Parámetros
* **Class&lt;A&gt; annotationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<A> annotationClass" %}

## Clase Padre
[EventType](/Java/EventType-jdk-jfr/)

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
