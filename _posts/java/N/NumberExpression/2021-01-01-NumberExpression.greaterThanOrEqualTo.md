---
title: NumberExpression.greaterThanOrEqualTo()
permalink: /Java/NumberExpression/greaterThanOrEqualTo/
date: 2021-01-11
key: Java.N.NumberExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberExpression.metodos valor="greaterThanOrEqualTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BooleanBinding greaterThanOrEqualTo(double other)
BooleanBinding greaterThanOrEqualTo(float other)
BooleanBinding greaterThanOrEqualTo(int other)
BooleanBinding greaterThanOrEqualTo(long other)
BooleanBinding greaterThanOrEqualTo(ObservableNumberValue other)
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
