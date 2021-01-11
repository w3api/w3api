---
title: DoubleExpression.doubleExpression()
permalink: Java/DoubleExpression/doubleExpression
date: 2021-01-11
key: JavaJava.D.DoubleExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleExpression.metodos valor="doubleExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DoubleExpression doubleExpression(ObservableDoubleValue value)
static <T extends Number>DoubleExpression doubleExpression(ObservableValue<T> value)
~~~

## Parámetros
* **ObservableValue&lt;T&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<T> value" %}
* **ObservableDoubleValue value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableDoubleValue value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DoubleExpression](/Java/DoubleExpression/)

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
