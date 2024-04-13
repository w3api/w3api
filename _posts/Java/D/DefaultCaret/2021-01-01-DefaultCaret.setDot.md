---
title: DefaultCaret.setDot()
permalink: /Java/DefaultCaret/setDot/
date: 2021-01-11
key: Java.D.DefaultCaret
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultCaret.metodos valor="setDot" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDot(int dot)
public void setDot(int dot, Position.Bias dotBias)
~~~

## Parámetros
* **Position.Bias dotBias**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias dotBias" %}
* **int dot**,  {% include w3api/param_description.html metodo=_dato parametro="int dot" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DefaultCaret](/Java/DefaultCaret/)

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
