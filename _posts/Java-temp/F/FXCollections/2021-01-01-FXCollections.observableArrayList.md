---
title: FXCollections.observableArrayList()
permalink: /Java/FXCollections/observableArrayList/
date: 2021-01-11
key: Java.F.FXCollections
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="observableArrayList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> ObservableList<E> observableArrayList()
static <E> ObservableList<E> observableArrayList(E... items)
static <E> ObservableList<E> observableArrayList(Collection<? extends E> col)
static <E> ObservableList<E> observableArrayList(Callback<E,Observable[]> extractor)
~~~

## Parámetros
* **E... items**,  {% include w3api/param_description.html metodo=_dato parametro="E... items" %}
* **Observable[]&gt; extractor**,  {% include w3api/param_description.html metodo=_dato parametro="Observable[]> extractor" %}
* **Callback&lt;E**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<E" %}
* **Collection&lt;? extends E&gt; col**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> col" %}

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
