---
title: FXCollections.observableSet()
permalink: Java/FXCollections/observableSet
date: 2021-01-04
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
* **Set&lt;E&gt; set**,  {% include w3api/param_description.html metodo=_data parametro="Set<E> set" %}
* **E... elements**,  {% include w3api/param_description.html metodo=_data parametro="E... elements" %}

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
