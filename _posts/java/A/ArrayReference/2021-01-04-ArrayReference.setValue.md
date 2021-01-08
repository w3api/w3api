---
title: ArrayReference.setValue()
permalink: Java/ArrayReference/setValue
date: 2021-01-04
key: JavaJava.A.ArrayReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayReference.metodos valor="setValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setValue(int index, Value value) throws InvalidTypeException, ClassNotLoadedException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **Value value**,  {% include w3api/param_description.html metodo=_data parametro="Value value" %}

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
