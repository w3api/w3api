---
title: ComponentView.viewToModel()
permalink: /Java/ComponentView/viewToModel/
date: 2021-01-11
key: Java.C.ComponentView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentView.metodos valor="viewToModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int viewToModel(float x, float y, Shape a, Position.Bias[] bias)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_dato parametro="Shape a" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **Position.Bias[] bias**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias[] bias" %}

## Clase Padre
[ComponentView](/Java/ComponentView/)

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
