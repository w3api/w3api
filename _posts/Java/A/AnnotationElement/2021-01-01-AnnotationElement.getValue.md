---
title: AnnotationElement.getValue()
permalink: /Java/AnnotationElement/getValue/
date: 2021-01-11
key: Java.A.AnnotationElement
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationElement.metodos valor="getValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getValue(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

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
