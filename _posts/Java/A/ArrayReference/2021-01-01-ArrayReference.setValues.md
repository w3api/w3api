---
title: ArrayReference.setValues()
permalink: /Java/ArrayReference/setValues/
date: 2021-01-11
key: Java.A.ArrayReference
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayReference.metodos valor="setValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setValues(int index, List<? extends Value> values, int srcIndex, int length) throws InvalidTypeException, ClassNotLoadedException
void setValues(List<? extends Value> values) throws InvalidTypeException, ClassNotLoadedException
~~~

## Parámetros
* **int srcIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int srcIndex" %}
* **List&lt;? extends Value&gt; values**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Value> values" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [InvalidTypeException](/Java/InvalidTypeException/), [ClassNotLoadedException](/Java/ClassNotLoadedException/)

## Clase Padre
[ArrayReference](/Java/ArrayReference/)

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
