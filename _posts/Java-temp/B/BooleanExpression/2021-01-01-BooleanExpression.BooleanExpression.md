---
title: BooleanExpression.booleanExpression()
permalink: /Java/BooleanExpression/booleanExpression/
date: 2021-01-11
key: Java.B.BooleanExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BooleanExpression.metodos valor="booleanExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BooleanExpression booleanExpression(ObservableBooleanValue value)
public static BooleanExpression booleanExpression(ObservableValue<Boolean> value)
~~~

## Parámetros
* **ObservableValue&lt;Boolean&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean> value" %}
* **ObservableBooleanValue value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableBooleanValue value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BooleanExpression](/Java/BooleanExpression/)

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
