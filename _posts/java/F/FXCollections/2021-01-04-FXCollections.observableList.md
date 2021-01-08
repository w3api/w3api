---
title: FXCollections.observableList()
permalink: Java/FXCollections/observableList
date: 2021-01-04
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
* **Observable[]&gt; extractor**,  {% include w3api/param_description.html metodo=_data parametro="Observable[]> extractor" %}
* **List&lt;E&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<E> list" %}
* **Callback&lt;E**,  {% include w3api/param_description.html metodo=_data parametro="Callback<E" %}

## Clase Padre
[FXCollections](/Java/FXCollections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FXCollections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
