---
title: FXCollections.checkedObservableList()
permalink: /Java/FXCollections/checkedObservableList/
date: 2021-01-11
key: Java.F.FXCollections
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="checkedObservableList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> ObservableList<E> checkedObservableList(ObservableList<E> list, Class<E> type)
~~~

## Parámetros
* **Class&lt;E&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<E> type" %}
* **ObservableList&lt;E&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<E> list" %}

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
