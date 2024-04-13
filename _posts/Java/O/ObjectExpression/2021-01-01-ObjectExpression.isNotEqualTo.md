---
title: ObjectExpression.isNotEqualTo()
permalink: /Java/ObjectExpression/isNotEqualTo/
date: 2021-01-11
key: Java.O.ObjectExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectExpression.metodos valor="isNotEqualTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BooleanBinding isNotEqualTo(Object other)
public BooleanBinding isNotEqualTo(ObservableObjectValue<?> other)
~~~

## Parámetros
* **ObservableObjectValue&lt;?&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableObjectValue<?> other" %}
* **Object other**,  {% include w3api/param_description.html metodo=_dato parametro="Object other" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
