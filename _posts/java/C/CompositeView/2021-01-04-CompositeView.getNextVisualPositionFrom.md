---
title: CompositeView.getNextVisualPositionFrom()
permalink: Java/CompositeView/getNextVisualPositionFrom
date: 2021-01-04
key: JavaJava.C.CompositeView
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeView.metodos valor="getNextVisualPositionFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getNextVisualPositionFrom(int pos, Position.Bias b, Shape a, int direction, Position.Bias[] biasRet) throws BadLocationException
~~~

## Parámetros
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] biasRet" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeView](/Java/CompositeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
