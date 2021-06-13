---
title: BorderFactory.createDashedBorder()
permalink: /Java/BorderFactory/createDashedBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createDashedBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createDashedBorder(Paint paint)
public static Border createDashedBorder(Paint paint, float length, float spacing)
public static Border createDashedBorder(Paint paint, float thickness, float length, float spacing, boolean rounded)
~~~

## Parámetros
* **float length**,  {% include w3api/param_description.html metodo=_dato parametro="float length" %}
* **float thickness**,  {% include w3api/param_description.html metodo=_dato parametro="float thickness" %}
* **float spacing**,  {% include w3api/param_description.html metodo=_dato parametro="float spacing" %}
* **Paint paint**,  {% include w3api/param_description.html metodo=_dato parametro="Paint paint" %}
* **boolean rounded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean rounded" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
