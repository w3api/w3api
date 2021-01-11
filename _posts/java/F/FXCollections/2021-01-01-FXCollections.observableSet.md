---
title: FXCollections.observableSet()
permalink: Java/FXCollections/observableSet
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="observableSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> ObservableSet<E> observableSet(E... elements)
static <E> ObservableSet<E> observableSet(Set<E> set)
~~~

## Parámetros
* **E... elements**,  {% include w3api/param_description.html metodo=_dato parametro="E... elements" %}
* **Set&lt;E&gt; set**,  {% include w3api/param_description.html metodo=_dato parametro="Set<E> set" %}

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
