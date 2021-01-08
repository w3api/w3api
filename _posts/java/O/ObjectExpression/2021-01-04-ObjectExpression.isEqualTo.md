---
title: ObjectExpression.isEqualTo()
permalink: Java/ObjectExpression/isEqualTo
date: 2021-01-04
key: JavaJava.O.ObjectExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectExpression.metodos valor="isEqualTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BooleanBinding isEqualTo(Object other)
public BooleanBinding isEqualTo(ObservableObjectValue<?> other)
~~~

## Parámetros
* **Object other**,  {% include w3api/param_description.html metodo=_data parametro="Object other" %}
* **ObservableObjectValue&lt;?&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="ObservableObjectValue<?> other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObjectExpression](/Java/ObjectExpression/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
