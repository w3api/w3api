---
title: FXCollections.copy()
permalink: Java/FXCollections/copy
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="copy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> void copy(ObservableList<? super T> dest, List<? extends T> src)
~~~

## Parámetros
* **List&lt;? extends T&gt; src**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends T> src" %}
* **ObservableList&lt;? super T&gt; dest**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<? super T> dest" %}

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
