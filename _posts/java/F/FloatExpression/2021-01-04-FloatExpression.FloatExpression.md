---
title: FloatExpression.floatExpression()
permalink: Java/FloatExpression/floatExpression
date: 2021-01-04
key: JavaJava.F.FloatExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatExpression.metodos valor="floatExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static FloatExpression floatExpression(ObservableFloatValue value)
static <T extends Number>FloatExpression floatExpression(ObservableValue<T> value)
~~~

## Parámetros
* **ObservableFloatValue value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableFloatValue value" %}
* **ObservableValue&lt;T&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<T> value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[FloatExpression](/Java/FloatExpression/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FloatExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
