---
title: NumberExpression.subtract()
permalink: Java/NumberExpression/subtract
date: 2021-01-11
key: JavaJava.N.NumberExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberExpression.metodos valor="subtract" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NumberBinding subtract(double other)
NumberBinding subtract(float other)
NumberBinding subtract(int other)
NumberBinding subtract(long other)
NumberBinding subtract(ObservableNumberValue other)
~~~

## Parámetros
* **ObservableNumberValue other**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableNumberValue other" %}
* **long other**,  {% include w3api/param_description.html metodo=_dato parametro="long other" %}
* **double other**,  {% include w3api/param_description.html metodo=_dato parametro="double other" %}
* **int other**,  {% include w3api/param_description.html metodo=_dato parametro="int other" %}
* **float other**,  {% include w3api/param_description.html metodo=_dato parametro="float other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NumberExpression](/Java/NumberExpression/)

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
