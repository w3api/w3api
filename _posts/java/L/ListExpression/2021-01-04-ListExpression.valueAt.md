---
title: ListExpression.valueAt()
permalink: Java/ListExpression/valueAt
date: 2021-01-04
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
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **ObservableIntegerValue index**,  {% include w3api/param_description.html metodo=_data parametro="ObservableIntegerValue index" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ListExpression](/Java/ListExpression/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
