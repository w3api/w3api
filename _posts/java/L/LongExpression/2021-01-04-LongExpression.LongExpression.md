---
title: LongExpression.longExpression()
permalink: Java/LongExpression/longExpression
date: 2021-01-04
key: JavaJava.L.LongExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongExpression.metodos valor="longExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LongExpression longExpression(ObservableLongValue value)
static <T extends Number>LongExpression longExpression(ObservableValue<T> value)
~~~

## Parámetros
* **ObservableLongValue value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableLongValue value" %}
* **ObservableValue&lt;T&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<T> value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LongExpression](/Java/LongExpression/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
