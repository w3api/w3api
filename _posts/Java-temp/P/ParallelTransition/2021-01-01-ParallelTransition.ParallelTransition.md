---
title: ParallelTransition.ParallelTransition()
permalink: /Java/ParallelTransition/ParallelTransition/
date: 2021-01-11
key: Java.P.ParallelTransition
category: Java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParallelTransition.constructores valor="ParallelTransition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ParallelTransition()
public ParallelTransition(Animation... children)
public ParallelTransition(Node node)
public ParallelTransition(Node node, Animation... children)
~~~

## Parámetros
* **Animation... children**,  {% include w3api/param_description.html metodo=_dato parametro="Animation... children" %}
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}

## Clase Padre
[ParallelTransition](/Java/ParallelTransition/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
