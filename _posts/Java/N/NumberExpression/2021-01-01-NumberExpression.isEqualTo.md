---
title: NumberExpression.isEqualTo()
permalink: /Java/NumberExpression/isEqualTo/
date: 2021-01-11
key: Java.N.NumberExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberExpression.metodos valor="isEqualTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BooleanBinding isEqualTo(double other, double epsilon)
BooleanBinding isEqualTo(float other, double epsilon)
BooleanBinding isEqualTo(int other)
BooleanBinding isEqualTo(int other, double epsilon)
BooleanBinding isEqualTo(long other)
BooleanBinding isEqualTo(long other, double epsilon)
BooleanBinding isEqualTo(ObservableNumberValue other)
BooleanBinding isEqualTo(ObservableNumberValue other, double epsilon)
~~~

## Parámetros
* **double epsilon**,  {% include w3api/param_description.html metodo=_dato parametro="double epsilon" %}
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
