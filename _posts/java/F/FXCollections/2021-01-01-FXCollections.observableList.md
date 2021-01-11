---
title: FXCollections.observableList()
permalink: Java/FXCollections/observableList
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="observableList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> ObservableList<E> observableList(List<E> list)
static <E> ObservableList<E> observableList(List<E> list, Callback<E,Observable[]> extractor)
~~~

## Parámetros
* **Observable[]&gt; extractor**,  {% include w3api/param_description.html metodo=_dato parametro="Observable[]> extractor" %}
* **Callback&lt;E**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<E" %}
* **List&lt;E&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<E> list" %}

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
