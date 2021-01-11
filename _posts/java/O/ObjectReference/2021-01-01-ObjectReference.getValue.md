---
title: ObjectReference.getValue()
permalink: Java/ObjectReference/getValue
date: 2021-01-11
key: JavaJava.O.ObjectReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectReference.metodos valor="getValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Value getValue(Field sig)
~~~

## Parámetros
* **Field sig**,  {% include w3api/param_description.html metodo=_dato parametro="Field sig" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ObjectReference](/Java/ObjectReference/)

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
