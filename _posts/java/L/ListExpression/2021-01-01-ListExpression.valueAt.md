---
title: ListExpression.valueAt()
permalink: Java/ListExpression/valueAt
date: 2021-01-11
key: JavaJava.L.ListExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.ListExpression.metodos valor="valueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectBinding<E> valueAt(int index)
public ObjectBinding<E> valueAt(ObservableIntegerValue index)
~~~

## Parámetros
* **ObservableIntegerValue index**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableIntegerValue index" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ListExpression](/Java/ListExpression/)

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
