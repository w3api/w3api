---
title: BorderFactory.createDashedBorder()
permalink: Java/BorderFactory/createDashedBorder
date: 2021-01-04
key: JavaJava.B.BorderFactory
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
* **float length**,  {% include w3api/param_description.html metodo=_data parametro="float length" %}
* **Paint paint**,  {% include w3api/param_description.html metodo=_data parametro="Paint paint" %}
* **boolean rounded**,  {% include w3api/param_description.html metodo=_data parametro="boolean rounded" %}
* **float thickness**,  {% include w3api/param_description.html metodo=_data parametro="float thickness" %}
* **float spacing**,  {% include w3api/param_description.html metodo=_data parametro="float spacing" %}

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
{%- for _ldc in site.data.Java.B.BorderFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
