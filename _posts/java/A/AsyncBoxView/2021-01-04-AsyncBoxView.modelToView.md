---
title: AsyncBoxView.modelToView()
permalink: Java/AsyncBoxView/modelToView
date: 2021-01-04
key: JavaJava.A.AsyncBoxView
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsyncBoxView.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Shape modelToView(int pos, Shape a, Position.Bias b) throws BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AsyncBoxView](/Java/AsyncBoxView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsyncBoxView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
