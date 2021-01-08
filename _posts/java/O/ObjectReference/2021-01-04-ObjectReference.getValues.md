---
title: ObjectReference.getValues()
permalink: Java/ObjectReference/getValues
date: 2021-01-04
key: JavaJava.O.ObjectReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectReference.metodos valor="getValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map<Field,Value> getValues(List<? extends Field> fields)
~~~

## Parámetros
* **List&lt;? extends Field&gt; fields**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Field> fields" %}

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
{%- for _ldc in site.data.Java.O.ObjectReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
