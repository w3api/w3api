---
title: BorderFactory.createStrokeBorder()
permalink: /Java/BorderFactory/createStrokeBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createStrokeBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createStrokeBorder(BasicStroke stroke)
public static Border createStrokeBorder(BasicStroke stroke, Paint paint)
~~~

## Parámetros
* **Paint paint**,  {% include w3api/param_description.html metodo=_dato parametro="Paint paint" %}
* **BasicStroke stroke**,  {% include w3api/param_description.html metodo=_dato parametro="BasicStroke stroke" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

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
