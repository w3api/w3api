---
title: AbstractLayoutCache.getNodeDimensions()
permalink: Java/AbstractLayoutCache/getNodeDimensions
date: 2021-01-10
key: JavaJava.A.AbstractLayoutCache
category: java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractLayoutCache.metodos valor="getNodeDimensions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AbstractLayoutCache.NodeDimensions getNodeDimensions()
protected Rectangle getNodeDimensions(Object value, int row, int depth, boolean expanded, Rectangle placeIn)
~~~

## Parámetros
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **Rectangle placeIn**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle placeIn" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int depth**,  {% include w3api/param_description.html metodo=_dato parametro="int depth" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean expanded" %}

## Clase Padre
[AbstractLayoutCache](/Java/AbstractLayoutCache/)

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
