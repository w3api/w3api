---
title: FXCollections.replaceAll()
permalink: Java/FXCollections/replaceAll
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="replaceAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> boolean replaceAll(ObservableList<T> list, T oldVal, T newVal)
~~~

## Parámetros
* **ObservableList&lt;T&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> list" %}
* **T oldVal**,  {% include w3api/param_description.html metodo=_dato parametro="T oldVal" %}
* **T newVal**,  {% include w3api/param_description.html metodo=_dato parametro="T newVal" %}

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
