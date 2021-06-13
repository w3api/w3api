---
title: FXCollections.concat()
permalink: /Java/FXCollections/concat/
date: 2021-01-11
key: Java.F.FXCollections
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="concat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> ObservableList<E> concat(ObservableList<E>... lists)
~~~

## Parámetros
* **ObservableList&lt;E&gt;... lists**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<E>... lists" %}

## Clase Padre
[FXCollections](/Java/FXCollections/)

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
