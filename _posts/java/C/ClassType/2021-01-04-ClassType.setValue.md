---
title: ClassType.setValue()
permalink: Java/ClassType/setValue
date: 2021-01-04
key: JavaJava.C.ClassType
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassType.metodos valor="setValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setValue(Field field, Value value) throws InvalidTypeException, ClassNotLoadedException
~~~

## Parámetros
* **Value value**,  {% include w3api/param_description.html metodo=_data parametro="Value value" %}
* **Field field**,  {% include w3api/param_description.html metodo=_data parametro="Field field" %}

## Excepciones
[ClassNotLoadedException](/Java/ClassNotLoadedException/), [InvalidTypeException](/Java/InvalidTypeException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ClassType](/Java/ClassType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
