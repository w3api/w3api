---
title: NumberExpression.greaterThanOrEqualTo()
permalink: Java/NumberExpression/greaterThanOrEqualTo
date: 2021-01-04
key: JavaJava.N.NumberExpression
category: java
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
* **long other**,  {% include w3api/param_description.html metodo=_data parametro="long other" %}
* **int other**,  {% include w3api/param_description.html metodo=_data parametro="int other" %}
* **float other**,  {% include w3api/param_description.html metodo=_data parametro="float other" %}
* **ObservableNumberValue other**,  {% include w3api/param_description.html metodo=_data parametro="ObservableNumberValue other" %}
* **double other**,  {% include w3api/param_description.html metodo=_data parametro="double other" %}

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
{%- for _ldc in site.data.Java.N.NumberExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
