---
title: BorderFactory.createEmptyBorder()
permalink: /Java/BorderFactory/createEmptyBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: Java
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
* **int bottom**,  {% include w3api/param_description.html metodo=_dato parametro="int bottom" %}
* **int right**,  {% include w3api/param_description.html metodo=_dato parametro="int right" %}
* **int left**,  {% include w3api/param_description.html metodo=_dato parametro="int left" %}
* **int top**,  {% include w3api/param_description.html metodo=_dato parametro="int top" %}

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
