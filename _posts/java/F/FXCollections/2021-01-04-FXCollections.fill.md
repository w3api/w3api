---
title: FXCollections.fill()
permalink: Java/FXCollections/fill
date: 2021-01-04
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="fill" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> void fill(ObservableList<? super T> list, T obj)
~~~

## Parámetros
* **ObservableList&lt;? super T&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<? super T> list" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

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
