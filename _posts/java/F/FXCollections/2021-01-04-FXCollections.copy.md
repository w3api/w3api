---
title: FXCollections.copy()
permalink: Java/FXCollections/copy
date: 2021-01-04
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
* **ObservableList&lt;? super T&gt; dest**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<? super T> dest" %}
* **List&lt;? extends T&gt; src**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends T> src" %}

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
