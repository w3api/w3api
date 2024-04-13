---
title: DocAttributeSet.addAll()
permalink: /Java/DocAttributeSet/addAll/
date: 2021-01-11
key: Java.D.DocAttributeSet
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocAttributeSet.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean addAll(AttributeSet attributes)
~~~

## Parámetros
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnmodifiableSetException](/Java/UnmodifiableSetException/)

## Clase Padre
[DocAttributeSet](/Java/DocAttributeSet/)

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
