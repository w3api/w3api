---
title: FXCollections.shuffle()
permalink: Java/FXCollections/shuffle
date: 2021-01-04
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="shuffle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void shuffle(ObservableList<?> list)
public static void shuffle(ObservableList list, Random rnd)
~~~

## Parámetros
* **ObservableList&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<?> list" %}
* **ObservableList list**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList list" %}
* **Random rnd**,  {% include w3api/param_description.html metodo=_data parametro="Random rnd" %}

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
