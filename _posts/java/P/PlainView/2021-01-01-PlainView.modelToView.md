---
title: PlainView.modelToView()
permalink: /Java/PlainView/modelToView/
date: 2021-01-11
key: Java.P.PlainView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlainView.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Shape modelToView(int pos, Shape a, Position.Bias b) throws BadLocationException
~~~

## Parámetros
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias b" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_dato parametro="Shape a" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[PlainView](/Java/PlainView/)

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
