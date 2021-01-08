---
title: DefaultCaret.moveDot()
permalink: Java/DefaultCaret/moveDot
date: 2021-01-04
key: JavaJava.D.DefaultCaret
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultCaret.metodos valor="moveDot" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void moveDot(int dot)
public void moveDot(int dot, Position.Bias dotBias)
~~~

## Parámetros
* **Position.Bias dotBias**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias dotBias" %}
* **int dot**,  {% include w3api/param_description.html metodo=_data parametro="int dot" %}

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
{%- for _ldc in site.data.Java.D.DefaultCaret.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
