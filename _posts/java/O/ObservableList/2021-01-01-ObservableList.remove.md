---
title: ObservableList.remove()
permalink: Java/ObservableList/remove
date: 2021-01-11
key: JavaJava.O.ObservableList
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void remove(int from, int to)
~~~

## Parámetros
* **int from**,  {% include w3api/param_description.html metodo=_dato parametro="int from" %}
* **int to**,  {% include w3api/param_description.html metodo=_dato parametro="int to" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[ObservableList](/Java/ObservableList/)

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
