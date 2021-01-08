---
title: IntegerExpression.integerExpression()
permalink: Java/IntegerExpression/integerExpression
date: 2021-01-04
key: JavaJava.I.IntegerExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntegerExpression.metodos valor="integerExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static IntegerExpression integerExpression(ObservableIntegerValue value)
static <T extends Number>IntegerExpression integerExpression(ObservableValue<T> value)
~~~

## Parámetros
* **ObservableIntegerValue value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableIntegerValue value" %}
* **ObservableValue&lt;T&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<T> value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IntegerExpression](/Java/IntegerExpression/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntegerExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
