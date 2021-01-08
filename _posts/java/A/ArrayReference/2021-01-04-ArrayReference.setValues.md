---
title: ArrayReference.setValues()
permalink: Java/ArrayReference/setValues
date: 2021-01-04
key: JavaJava.A.ArrayReference
category: java
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **List&lt;? extends Value&gt; values**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Value> values" %}
* **int srcIndex**,  {% include w3api/param_description.html metodo=_data parametro="int srcIndex" %}

## Excepciones
[ClassNotLoadedException](/Java/ClassNotLoadedException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [InvalidTypeException](/Java/InvalidTypeException/)

## Clase Padre
[ArrayReference](/Java/ArrayReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ArrayReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
