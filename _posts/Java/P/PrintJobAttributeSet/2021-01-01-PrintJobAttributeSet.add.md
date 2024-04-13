---
title: PrintJobAttributeSet.add()
permalink: /Java/PrintJobAttributeSet/add/
date: 2021-01-11
key: Java.P.PrintJobAttributeSet
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintJobAttributeSet.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean add(Attribute attribute)
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attribute" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnmodifiableSetException](/Java/UnmodifiableSetException/)

## Clase Padre
[PrintJobAttributeSet](/Java/PrintJobAttributeSet/)

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
