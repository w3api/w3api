---
title: AbstractLayoutCache.getNodeDimensions()
permalink: Java/AbstractLayoutCache/getNodeDimensions
date: 2021-01-04
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
* **int depth**,  {% include w3api/param_description.html metodo=_data parametro="int depth" %}
* **Rectangle placeIn**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle placeIn" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_data parametro="boolean expanded" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[AbstractLayoutCache](/Java/AbstractLayoutCache/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractLayoutCache.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
