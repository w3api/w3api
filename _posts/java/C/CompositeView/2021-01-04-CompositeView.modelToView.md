---
title: CompositeView.modelToView()
permalink: Java/CompositeView/modelToView
date: 2021-01-04
key: JavaJava.C.CompositeView
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeView.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Shape modelToView(int pos, Shape a, Position.Bias b) throws BadLocationException
public Shape modelToView(int p0, Position.Bias b0, int p1, Position.Bias b1, Shape a) throws BadLocationException
~~~

## Parámetros
* **Position.Bias b1**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b1" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}
* **int p1**,  {% include w3api/param_description.html metodo=_data parametro="int p1" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b" %}
* **int p0**,  {% include w3api/param_description.html metodo=_data parametro="int p0" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Position.Bias b0**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b0" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeView](/Java/CompositeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
