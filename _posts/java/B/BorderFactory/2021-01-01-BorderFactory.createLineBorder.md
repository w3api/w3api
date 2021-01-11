---
title: BorderFactory.createLineBorder()
permalink: Java/BorderFactory/createLineBorder
date: 2021-01-11
key: JavaJava.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createLineBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createLineBorder(Color color)
public static Border createLineBorder(Color color, int thickness)
public static Border createLineBorder(Color color, int thickness, boolean rounded)
~~~

## Parámetros
* **Color color**,  {% include w3api/param_description.html metodo=_dato parametro="Color color" %}
* **boolean rounded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean rounded" %}
* **int thickness**,  {% include w3api/param_description.html metodo=_dato parametro="int thickness" %}

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
