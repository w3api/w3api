---
title: PropertyEditor.setAsText()
permalink: /Java/PropertyEditor/setAsText/
date: 2021-01-11
key: Java.P.PropertyEditor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyEditor.metodos valor="setAsText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAsText(String text) throws IllegalArgumentException
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PropertyEditor](/Java/PropertyEditor/)

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
