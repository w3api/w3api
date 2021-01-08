---
title: BorderFactory.createEmptyBorder()
permalink: Java/BorderFactory/createEmptyBorder
date: 2021-01-04
key: JavaJava.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createEmptyBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createEmptyBorder()
public static Border createEmptyBorder(int top, int left, int bottom, int right)
~~~

## Parámetros
* **int left**,  {% include w3api/param_description.html metodo=_data parametro="int left" %}
* **int right**,  {% include w3api/param_description.html metodo=_data parametro="int right" %}
* **int top**,  {% include w3api/param_description.html metodo=_data parametro="int top" %}
* **int bottom**,  {% include w3api/param_description.html metodo=_data parametro="int bottom" %}

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
